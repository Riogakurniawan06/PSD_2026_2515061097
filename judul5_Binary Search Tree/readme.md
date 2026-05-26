TUGAS AKHIR JUDUL 5 BINARY SEARCH TREE

Kodingan Lemari Buku (BST Lanjutan) ini pada dasarnya adalah penerapan struktur data Binary Search Tree untuk menyimpan dan mengatur buku berdasarkan ID. Setiap buku direpresentasikan sebagai sebuah node dengan atribut ID, judul, serta pointer ke kiri dan kanan. Aturan penyimpanannya sederhana: jika ID lebih kecil dari node saat ini, buku ditempatkan di kiri; jika lebih besar, ditempatkan di kanan. Dengan cara ini, buku otomatis tersusun rapi sehingga pencarian, penambahan, maupun penghapusan bisa dilakukan lebih cepat dan terstruktur.

Selain itu, program menyediakan berbagai fungsi tambahan seperti menghitung tinggi pohon untuk mengetahui seberapa dalam susunan rak, menampilkan isi lemari dengan traversal level-order agar terlihat urutan buku dari atas ke bawah, serta mencari successor dan predecessor untuk mengetahui buku yang posisinya tepat setelah atau sebelum ID tertentu. Semua fungsi ini dihubungkan dengan menu interaktif di bagian main(), sehingga pengguna bisa memilih operasi yang diinginkan dengan mudah. Jadi kodingan ini bukan hanya latihan algoritma, tetapi juga simulasi nyata bagaimana sebuah lemari buku bisa diatur secara otomatis menggunakan konsep pohon biner.


PENJELASAN KODINGAN


<img width="345" height="131" alt="image" src="https://github.com/user-attachments/assets/6eb897b4-6f07-43c6-b5dc-b7142bcbbe25" />

Bagian ini bikin class Buku. Class ini ibarat cetakan untuk setiap buku yang akan disimpan di lemari. Saat kita bikin objek baru, ID buku dan judul akan disimpan di variabel self.id_buku dan self.judul. Lalu ada self.kiri dan self.kanan yang awalnya bernilai None, artinya buku ini belum terhubung ke rak kiri atau kanan.

<img width="209" height="63" alt="image" src="https://github.com/user-attachments/assets/4caf674c-34e2-44ff-8f09-ea3f493e5412" />

Ini bikin class LemariBuku. Di dalamnya ada self.root yang nunjukin akar dari lemari. Kalau root masih None, berarti lemari masih kosong, belum ada buku sama sekali.


<img width="575" height="167" alt="image" src="https://github.com/user-attachments/assets/f5ee76d6-5899-47d0-b458-ce86d481edab" />

Fungsi ini dipakai buat masukin buku baru ke lemari. Kalau rak kosong, buku langsung ditaruh di situ. Kalau ID buku lebih kecil dari ID yang ada, maka buku diarahkan ke rak kiri. Kalau lebih besar, diarahkan ke rak kanan. Dengan aturan ini, buku otomatis tersusun rapi sesuai urutan ID.


<img width="512" height="47" alt="image" src="https://github.com/user-attachments/assets/32990cb7-a12a-4c69-9bcd-d22f4c287006" />

Fungsi ini memanggil proses penambahan mulai dari akar lemari. Jadi setiap kali kita menambah buku, prosesnya selalu dimulai dari root.


<img width="518" height="107" alt="image" src="https://github.com/user-attachments/assets/076b85f6-72e3-411c-9802-79b1605c97dc" />

Fungsi ini mencari buku dengan ID terkecil. Caranya dengan terus bergerak ke rak kiri sampai tidak ada lagi. Fungsi ini penting saat kita ingin menghapus buku, karena sering kali kita butuh pengganti dari rak kanan dengan ID terkecil.

<img width="641" height="399" alt="image" src="https://github.com/user-attachments/assets/6d5860f1-5c63-48c5-bcf2-175c6e2dbf9f" />

Fungsi ini dipakai buat menghapus buku dari lemari. Kalau buku tidak punya anak, langsung dihapus. Kalau hanya punya satu anak, anak itu menggantikan posisinya. Kalau punya dua anak, maka dicari pengganti dari rak kanan dengan ID terkecil, lalu dipindahkan ke posisi buku yang dihapus.


<img width="429" height="133" alt="image" src="https://github.com/user-attachments/assets/a7469e78-0090-4a99-b123-ff1078ebb4de" />

Fungsi ini menghitung tinggi lemari. Kalau kosong nilainya -1. Kalau ada buku, dihitung kedalaman dari rak kiri dan rak kanan, lalu diambil yang paling besar. Jadi kita bisa tahu seberapa tinggi struktur lemarinya.


<img width="542" height="266" alt="image" src="https://github.com/user-attachments/assets/8744f4f2-bd5d-4315-bbde-f824dc578005" />

Fungsi ini menampilkan isi lemari dari atas ke bawah. Caranya pakai antrian, sehingga buku ditampilkan sesuai urutan level rak. Hasilnya terlihat rapi seperti kita melihat lemari nyata dari rak atas ke rak bawah.


<img width="479" height="349" alt="image" src="https://github.com/user-attachments/assets/b2c08e1c-235c-45c3-9613-f3c51973fbfc" />

Fungsi ini mencari successor, yaitu buku dengan ID lebih besar tepat setelah ID tertentu. Kalau ID lebih kecil, successor bisa jadi buku saat ini. Kalau lebih besar, bergerak ke kanan. Kalau ditemukan, successor diambil dari rak kanan dengan ID terkecil.


<img width="470" height="408" alt="image" src="https://github.com/user-attachments/assets/0041ce56-de8d-4526-8b41-b634a8b15d2d" />

Fungsi ini mencari predecessor, yaitu buku dengan ID lebih kecil tepat sebelum ID tertentu. Kalau ID lebih besar, predecessor bisa jadi buku saat ini. Kalau lebih kecil, bergerak ke kiri. Kalau ditemukan, predecessor diambil dari rak kiri dengan ID terbesar.


<img width="433" height="243" alt="image" src="https://github.com/user-attachments/assets/bdbeb7a3-6288-43a4-beed-1922b03528f6" />

Bagian ini membuat menu interaktif agar pengguna bisa memilih operasi yang diinginkan. Ada pilihan untuk menambah buku, menghapus buku, menampilkan isi lemari, menghitung tinggi lemari, mencari successor, mencari predecessor, atau keluar dari program.


<img width="274" height="94" alt="image" src="https://github.com/user-attachments/assets/40718c76-b007-4961-9f2e-605599465f1d" />

Bagian ini memastikan input berupa angka. Kalau input tidak valid, program akan menolak dan meminta ulang.


<img width="441" height="158" alt="image" src="https://github.com/user-attachments/assets/7739a8ec-a906-4b9d-b2a9-6c17da7be4a2" />

Kalau pengguna memilih angka 1, program akan meminta input berupa ID buku dan judul buku. Setelah itu, buku baru akan dimasukkan ke dalam lemari menggunakan fungsi tambah_buku. Jadi pilihan 1 ini ibarat kita menaruh buku baru ke rak sesuai urutan ID.


<img width="430" height="138" alt="image" src="https://github.com/user-attachments/assets/cf308e51-ca7e-4da6-821b-6c0f0348907a" />

Kalau pengguna memilih angka 2, program akan meminta ID buku yang ingin dihapus. Fungsi hapus_buku dipanggil untuk menghapus buku tersebut dari lemari. Jadi pilihan 2 ini ibarat kita mengambil buku dari rak dan mengosongkan posisinya.


<img width="348" height="62" alt="image" src="https://github.com/user-attachments/assets/5e56ce1e-46d8-4837-a98e-b38c4f249b95" />

Kalau pengguna memilih angka 3, program akan menampilkan isi lemari dengan cara traversal level-order. Artinya, buku ditampilkan dari rak atas ke bawah sesuai urutan level. Jadi pilihan 3 ini seperti kita melihat isi lemari secara keseluruhan, rak demi rak.


<img width="503" height="42" alt="image" src="https://github.com/user-attachments/assets/c34faae1-8c72-482b-8d1b-c9ed8df0e021" />

Kalau pengguna memilih angka 4, program akan menghitung tinggi lemari dengan memanggil fungsi tinggi_lemari. Hasilnya menunjukkan berapa tingkat rak yang ada. Jadi pilihan 4 ini ibarat kita mengukur seberapa tinggi lemari buku kita.


<img width="464" height="194" alt="image" src="https://github.com/user-attachments/assets/ac83a0d9-f44a-4583-9c34-64e1c448877f" />

Kalau pengguna memilih angka 5, program akan meminta ID buku tertentu, lalu mencari successor-nya. Successor adalah buku dengan ID lebih besar tepat setelah ID yang dimasukkan. Jadi pilihan 5 ini seperti kita bertanya: “Setelah buku ini, buku apa yang ada berikutnya di lemari?”


<img width="482" height="198" alt="image" src="https://github.com/user-attachments/assets/1877d470-a6db-4d64-8b2d-32726bb78e02" />

Kalau pengguna memilih angka 6, program akan meminta ID buku tertentu, lalu mencari predecessor-nya. Predecessor adalah buku dengan ID lebih kecil tepat sebelum ID yang dimasukkan. Jadi pilihan 6 ini seperti kita bertanya: “Sebelum buku ini, buku apa yang ada sebelumnya di lemari?”


<img width="289" height="94" alt="image" src="https://github.com/user-attachments/assets/5be55cbd-39ed-4f74-b7f5-65ff2e417dc5" />

kalau pengguna memilih angka 7, program akan berhenti dan menampilkan pesan “Program selesai.”


PENJELASAN OUTPUT


<img width="352" height="884" alt="Screenshot 2026-05-26 173455" src="https://github.com/user-attachments/assets/1866355d-e045-4b9b-a12a-4639dec01017" />
<img width="388" height="967" alt="Screenshot 2026-05-26 173527" src="https://github.com/user-attachments/assets/2b4ebed4-d69e-4ebd-b8b9-dbe1eb4d68f3" />

 pertama pengguna memasukkan beberapa buku dengan ID dan judul, misalnya ID 4 judul aa, ID 6 judul bb, ID 3 judul cc, dan ID 7 judul ff. Semua buku ini otomatis disusun dalam bentuk pohon sesuai aturan Binary Search Tree, yaitu kalau ID lebih kecil ditempatkan di kiri dan kalau lebih besar ditempatkan di kanan.

Setelah buku dimasukkan, pengguna memilih menu 3 (Tampilkan Level-order). Program menampilkan isi lemari dengan cara traversal level-order, sehingga urutannya adalah akar dulu (ID 4 - aa), lalu anak kiri (ID 3 - cc), kemudian anak kanan (ID 6 - bb), dan anak kanan dari 6 yaitu (ID 7 - ff). Hasilnya terlihat rapi seperti kita melihat isi lemari rak demi rak.

Kemudian pengguna memilih menu 4 (Tinggi Lemari). Program menghitung kedalaman pohon, dan hasilnya adalah 2. Artinya lemari punya dua tingkat dari akar sampai daun paling dalam.

Selanjutnya pengguna memilih menu 5 (Successor Buku) dengan ID 4. Program mencari buku yang posisinya tepat setelah ID 4. Karena setelah 4 ada 6, maka hasilnya adalah Successor: ID 6 - bb.

Setelah itu pengguna memilih menu 2 (Hapus Buku) dengan ID 6. Program menghapus buku berjudul bb dengan ID 6 dari lemari. Pohon otomatis menyesuaikan strukturnya agar tetap rapi.

Terakhir, pengguna memilih menu 7 (Keluar). Program menampilkan pesan “Program selesai” dan berhenti.


LINK YOUTUBE= https://youtu.be/lApETLyncYc
