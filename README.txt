IMPLEMENTASI DES - TWO-WAY CIPHERTEXT COMMUNICATION
Tugas Keamanan Informasi

Nama  : Dzuhrillah Hendraines
Bahasa Pemrograman : Python
Algoritma : DES (Data Encryption Standard)
Komunikasi : TCP Socket
Monitoring : Wireshark


1. DESKRIPSI PROJECT

Pada tugas ini saya membuat implementasi komunikasi dua arah menggunakan
algoritma DES (Data Encryption Standard) dengan bahasa pemrograman Python.

Saya membuat dua program yang berjalan secara terpisah, yaitu Sender dan
Receiver. Sender digunakan untuk mengirim pesan, sedangkan Receiver digunakan
untuk menerima pesan. Pesan tidak dikirim dalam bentuk plaintext, tetapi
dienkripsi terlebih dahulu menggunakan algoritma DES.

Setelah ciphertext diterima oleh Receiver, ciphertext tersebut didekripsi
menggunakan key DES yang sama sehingga Receiver dapat memperoleh kembali
plaintext yang dikirim oleh Sender.

Receiver juga dapat mengirimkan pesan balasan kepada Sender. Pesan balasan
tersebut kembali dienkripsi menggunakan DES sebelum dikirim. Dengan demikian,
komunikasi yang dibuat pada tugas ini berlangsung dua arah.


2. STRUKTUR FILE

Project ini terdiri dari beberapa file:

des.py
    Berisi implementasi algoritma DES secara manual. File ini menangani proses
    pembentukan subkey, permutation, S-box, Feistel function, enkripsi,
    dekripsi, serta padding.

common.py
    Berisi konfigurasi yang digunakan oleh Sender dan Receiver, yaitu alamat
    host, port komunikasi, dan shared key DES.

sender.py
    Berfungsi sebagai client TCP. Program ini menerima plaintext dari pengguna,
    mengenkripsinya menggunakan DES, kemudian mengirimkan ciphertext kepada
    Receiver. Sender juga menerima dan mendekripsi pesan balasan dari Receiver.

receiver.py
    Berfungsi sebagai server TCP. Program ini menunggu koneksi dari Sender,
    menerima ciphertext, melakukan dekripsi, dan menampilkan plaintext.
    Receiver juga dapat mengenkripsi pesan balasan dan mengirimkannya kembali
    kepada Sender.

README.txt
    Berisi penjelasan mengenai project, cara menjalankan program, dan cara
    melakukan pengujian menggunakan Wireshark.


3. IMPLEMENTASI ALGORITMA DES

Pada implementasi ini saya tidak menggunakan library enkripsi DES secara
langsung. Algoritma DES saya implementasikan sendiri pada file des.py.

Beberapa bagian DES yang saya implementasikan antara lain:

- Initial Permutation (IP)
- Final Permutation (FP)
- Expansion Table
- Permutation Table
- PC-1
- PC-2
- Left Rotation
- Key Schedule
- 16 Subkey DES
- 8 S-Box
- Feistel Function
- DES Encryption
- DES Decryption
- Padding dan Unpadding

DES menggunakan block size sebesar 64 bit atau 8 byte. Key yang digunakan
memiliki panjang 8 byte.


4. SHARED KEY

Sender dan Receiver menggunakan key DES yang sama.

Key yang digunakan pada project ini:

    Kunci123

Key sudah diketahui oleh Sender dan Receiver sebelum komunikasi dimulai.
Key tidak dikirim melalui jaringan.

Konfigurasi tersebut terdapat pada file common.py:

    HOST = "127.0.0.1"
    PORT = 5050
    DES_KEY = "Kunci123"

Penggunaan shared key ini membuat Receiver dapat melakukan dekripsi terhadap
ciphertext yang dikirim oleh Sender.


5. KOMUNIKASI TCP

Saya menggunakan TCP Socket untuk menghubungkan Sender dan Receiver.

Pada pengujian menggunakan satu komputer, saya menggunakan:

    IP Address : 127.0.0.1
    Port      : 5050

Receiver bertindak sebagai server dan melakukan listen pada port 5050.
Sender bertindak sebagai client dan melakukan koneksi ke Receiver.

Alur komunikasi:

    Sender
       |
       | Plaintext
       v
    DES Encryption
       |
       | Ciphertext
       v
    TCP Socket
       |
       v
    Receiver
       |
       | DES Decryption
       v
    Plaintext


6. CARA MENJALANKAN PROGRAM

Saya menggunakan Python untuk menjalankan project ini.

Untuk memastikan versi Python, saya dapat menjalankan:

    py --version

Pada Windows, saya menggunakan perintah "py" untuk menjalankan program.


7. MENJALANKAN RECEIVER

Saya membuka terminal pertama dan masuk ke folder project.

Contoh:

    cd "C:\Users\ThinkPad\OneDrive\Documents\Keamanan Informasi B 2026\Tugas 1 DES"

Kemudian saya menjalankan:

    py receiver.py

Jika berhasil, program akan menampilkan:

    =======================================================
          DES TWO-WAY COMMUNICATION - RECEIVER
    =======================================================
    Menunggu koneksi pada 127.0.0.1:5050
    Key DES sudah diketahui bersama dan tidak dikirim.

Receiver kemudian menunggu koneksi dari Sender.


8. MENJALANKAN SENDER

Saya membuka terminal kedua pada folder project yang sama.

Kemudian saya menjalankan:

    py sender.py

Jika Receiver sudah berjalan, Sender akan terhubung dan menampilkan:

    Terhubung ke Receiver.

Sender kemudian siap menerima input pesan.


9. MENGIRIM PESAN DARI SENDER

Saya memasukkan pesan pada Sender, misalnya:

    Sender > Halo Receiver

Sebelum dikirim, pesan tersebut diproses oleh DES.

Alurnya:

    "Halo Receiver"
          |
          v
    DES Encryption
          |
          v
    Ciphertext
          |
          v
    TCP Socket
          |
          v
    Receiver

Sender juga menampilkan ciphertext dalam format hexadecimal.

Contohnya:

    Ciphertext (HEX): 3eec9e2b5727e98da9dc3c2fd7009fc8


10. PROSES PADA RECEIVER

Receiver menerima ciphertext yang dikirim oleh Sender.

Ciphertext tersebut kemudian didekripsi menggunakan key DES yang sama.

Alurnya:

    Ciphertext
          |
          v
    DES Decryption
          |
          v
    Plaintext
          |
          v
    "Halo Receiver"

Dengan demikian Receiver dapat memperoleh kembali pesan asli yang
dimasukkan oleh Sender.


11. KOMUNIKASI DARI RECEIVER KE SENDER

Setelah menerima pesan, Receiver dapat memberikan balasan.

Contohnya:

    Receiver > Halo Sender

Pesan tersebut juga tidak langsung dikirim sebagai plaintext.

Receiver melakukan:

    "Halo Sender"
          |
          v
    DES Encryption
          |
          v
    Ciphertext
          |
          v
    TCP Socket
          |
          v
    Sender
          |
          v
    DES Decryption
          |
          v
    "Halo Sender"

Hal ini menunjukkan bahwa komunikasi yang dibuat berlangsung dua arah.


12. PENGGUNAAN WIRESHARK

Saya juga menggunakan Wireshark untuk melihat data yang ditransmisikan
antara Sender dan Receiver.

Karena Sender dan Receiver pada pengujian ini berjalan pada komputer yang
sama menggunakan 127.0.0.1, saya menggunakan interface:

    Adapter for loopback traffic capture

Pada Wireshark saya menggunakan display filter:

    tcp.port == 5050

Filter tersebut digunakan untuk menampilkan komunikasi TCP yang menggunakan
port 5050.


13. HASIL CAPTURE WIRESHARK

Setelah Sender mengirim pesan, Wireshark dapat menangkap paket TCP yang
melewati koneksi localhost.

Pada packet detail dapat ditemukan bagian:

    Data

Data tersebut berisi byte yang ditransmisikan oleh aplikasi.

Ciphertext dapat terlihat dalam bentuk hexadecimal, misalnya:

    9af9b147fed9a436d65dc595fd4cbab376efed2aa105718a

Ketika TCP Stream dibuka menggunakan fitur Follow TCP Stream, data hasil
enkripsi dapat terlihat sebagai karakter yang tidak terbaca sebagai
plaintext biasa.

Hal ini menunjukkan bahwa data yang dikirim melalui komunikasi bukan
plaintext secara langsung, tetapi sudah diproses menggunakan DES.


14. ALUR SISTEM SECARA KESELURUHAN

Alur dari implementasi yang saya buat adalah:

    +----------------+
    |     Sender     |
    +----------------+
            |
            | Plaintext
            v
    +----------------+
    | DES Encryption |
    +----------------+
            |
            | Ciphertext
            v
    +----------------+
    |   TCP Socket   |
    +----------------+
            |
            v
    +----------------+
    |    Receiver    |
    +----------------+
            |
            | Ciphertext
            v
    +----------------+
    | DES Decryption |
    +----------------+
            |
            | Plaintext
            v
    +----------------+
    |    Receiver    |
    +----------------+


Untuk komunikasi balik:

    +----------------+
    |    Receiver    |
    +----------------+
            |
            | Plaintext
            v
    +----------------+
    | DES Encryption |
    +----------------+
            |
            | Ciphertext
            v
    +----------------+
    |   TCP Socket   |
    +----------------+
            |
            v
    +----------------+
    |     Sender     |
    +----------------+
            |
            | DES Decryption
            v
    +----------------+
    |    Plaintext   |
    +----------------+


15. KEY MANAGEMENT

Pada implementasi ini saya menggunakan konsep pre-shared key.

Sender dan Receiver sudah mengetahui key yang sama sebelum komunikasi
dimulai.

Key tersebut tidak dikirim sebagai bagian dari pesan dan tidak ditransmisikan
melalui TCP.

Dengan demikian, data yang dikirim melalui jaringan terdiri dari informasi
yang diperlukan untuk komunikasi dan ciphertext hasil enkripsi.


16. PENGUJIAN

Pengujian yang saya lakukan meliputi:

1. Menjalankan Receiver.
2. Menjalankan Sender.
3. Menghubungkan Sender dengan Receiver.
4. Mengirim plaintext dari Sender.
5. Mengenkripsi plaintext menggunakan DES.
6. Mengirim ciphertext melalui TCP.
7. Menerima ciphertext pada Receiver.
8. Mendekripsi ciphertext pada Receiver.
9. Memastikan plaintext kembali sesuai dengan pesan awal.
10. Mengirim pesan balasan dari Receiver.
11. Mengenkripsi pesan balasan menggunakan DES.
12. Mengirim ciphertext kembali kepada Sender.
13. Mendekripsi pesan balasan pada Sender.
14. Melakukan capture komunikasi menggunakan Wireshark.


17. KESIMPULAN

Pada tugas ini saya berhasil membuat implementasi komunikasi dua arah
menggunakan algoritma DES dengan bahasa Python.

Implementasi DES dibuat secara manual tanpa menggunakan library enkripsi DES
secara langsung. Sender dan Receiver menggunakan shared key yang sama dan
key tersebut tidak dikirim melalui jaringan.

Pesan dari Sender dienkripsi menjadi ciphertext sebelum dikirim melalui TCP.
Receiver kemudian mendekripsi ciphertext tersebut menggunakan key yang sama
untuk mendapatkan plaintext kembali. Proses yang sama juga dilakukan pada
arah sebaliknya sehingga komunikasi berlangsung dua arah.

Saya juga menggunakan Wireshark untuk mengamati komunikasi TCP dan melihat
data yang ditransmisikan dalam bentuk ciphertext.


18. CATATAN

Implementasi ini dibuat untuk keperluan pembelajaran dan demonstrasi
algoritma DES serta komunikasi ciphertext.

DES merupakan algoritma kriptografi yang sudah lama dan memiliki ukuran key
efektif yang relatif kecil untuk standar keamanan modern. Oleh karena itu,
implementasi ini digunakan untuk memahami konsep DES dan bukan sebagai
implementasi keamanan untuk aplikasi nyata.