# sender.py
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
    print("       DES TWO-WAY COMMUNICATION - SENDER")
    print("=" * 55)
    print(f"Tujuan : {HOST}:{PORT}")
    print("Key DES sudah diketahui bersama dan tidak dikirim.")
    print("Ketik 'exit' untuk mengakhiri.\n")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        print("Terhubung ke Receiver.\n")

        while True:
            message = input("Sender > ")

            if message.lower() == "exit":
                ciphertext = encrypt("exit", DES_KEY)
                send_ciphertext(sock, ciphertext)
                print("Koneksi ditutup.")
                break

            ciphertext = encrypt(message, DES_KEY)

            print(f"Ciphertext (HEX): {ciphertext.hex()}")
            send_ciphertext(sock, ciphertext)

            reply_ciphertext = receive_ciphertext(sock)
            if reply_ciphertext is None:
                print("Receiver menutup koneksi.")
                break

            print(f"Ciphertext balasan (HEX): {reply_ciphertext.hex()}")

            reply = decrypt(reply_ciphertext, DES_KEY).decode("utf-8")
            print(f"Receiver > {reply}\n")

            if reply.lower() == "exit":
                print("Receiver mengakhiri komunikasi.")
                break


if __name__ == "__main__":
    main()
