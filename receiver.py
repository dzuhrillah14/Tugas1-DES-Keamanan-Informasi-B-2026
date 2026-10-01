# receiver.py
import socket
import struct

from des import encrypt, decrypt
from common import HOST, PORT, DES_KEY


def send_ciphertext(sock, ciphertext):
    sock.sendall(struct.pack("!I", len(ciphertext)))
    sock.sendall(ciphertext)


def receive_ciphertext(sock):
    header = receive_exact(sock, 4)
    if header is None:
        return None

    length = struct.unpack("!I", header)[0]
    if length <= 0 or length > 10_000_000:
        raise ValueError("Ukuran pesan tidak valid.")

    return receive_exact(sock, length)


def receive_exact(sock, length):
    data = bytearray()

    while len(data) < length:
        chunk = sock.recv(length - len(data))
        if not chunk:
            return None
        data.extend(chunk)

    return bytes(data)


def main():
    print("=" * 55)
    print("      DES TWO-WAY COMMUNICATION - RECEIVER")
    print("=" * 55)
    print(f"Menunggu koneksi pada {HOST}:{PORT}")
    print("Key DES sudah diketahui bersama dan tidak dikirim.\n")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(1)

        conn, address = server.accept()

        with conn:
            print(f"Sender terhubung dari {address}.\n")

            while True:
                ciphertext = receive_ciphertext(conn)

                if ciphertext is None:
                    print("Sender menutup koneksi.")
                    break

                print(f"Ciphertext masuk (HEX): {ciphertext.hex()}")

                plaintext = decrypt(ciphertext, DES_KEY).decode("utf-8")
                print(f"Sender > {plaintext}")

                if plaintext.lower() == "exit":
                    print("Sender mengakhiri komunikasi.")
                    break

                reply = input("Receiver > ")

                reply_ciphertext = encrypt(reply, DES_KEY)

                print(f"Ciphertext balasan (HEX): {reply_ciphertext.hex()}")

                send_ciphertext(conn, reply_ciphertext)

                if reply.lower() == "exit":
                    print("Koneksi ditutup.")
                    break

                print()


if __name__ == "__main__":
    main()
