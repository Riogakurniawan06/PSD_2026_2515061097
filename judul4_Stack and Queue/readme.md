TUGAS JUDUL 4 MENUMPUKKAN PIRING MENGGUNAKAN STACK LINGKED LIST

Program ini secara umum berfungsi untuk mengelola data dengan konsep stack menggunakan linked list. Stack adalah struktur data yang bekerja dengan prinsip LIFO (Last In, First Out), artinya data yang terakhir dimasukkan akan menjadi data pertama yang keluar. Program ini menyediakan menu interaktif agar pengguna bisa menambahkan data ke dalam stack (push), menghapus data teratas (pop), melihat data teratas (peek), menampilkan semua isi stack (display), menghitung jumlah data, dan keluar dari program. Dengan begitu, program ini menjadi simulasi sederhana bagaimana stack bekerja dalam bentuk kode Python.

Algoritma yang diterapkan adalah struktur data stack berbasis linked list. Linked list digunakan untuk menyimpan data secara dinamis, di mana setiap elemen (Node) berisi nilai data dan pointer ke Node berikutnya. Stack mengatur operasi dengan aturan LIFO, sehingga setiap kali dilakukan push, data baru ditempatkan di atas, dan setiap kali dilakukan pop, data teratas yang dihapus. Kombinasi ini membuat program fleksibel dalam menambah dan menghapus data tanpa batasan ukuran tetap, karena linked list memungkinkan penambahan dan penghapusan elemen secara dinamis.


PENJELASAN KODINGAN

<img width="238" height="93" alt="image" src="https://github.com/user-attachments/assets/8f29e060-0286-4217-8bff-fb872c0685c0" />

Bagian ini bikin class Node. Node itu semacam elemen kecil yang tugasnya nyimpen data. Saat kita bikin Node baru, nilai yang kita masukin akan disimpan di self.data. Lalu ada self.next = None yang artinya Node ini belum terhubung ke Node lain.


<img width="243" height="69" alt="image" src="https://github.com/user-attachments/assets/0acb2a8c-ddb3-47f3-b79b-f9c49ec0af56" />

Ini bikin class StackLinkedList. Di dalamnya ada self.top_ptr = None yang nunjukin kalau stack masih kosong, belum ada data di atas.


<img width="284" height="49" alt="image" src="https://github.com/user-attachments/assets/7ea895d8-483c-4b15-b356-2d582784e0cc" />

Fungsi ini buat ngecek apakah stack kosong. Kalau top_ptr masih None, berarti belum ada data sama sekali.


<img width="397" height="105" alt="image" src="https://github.com/user-attachments/assets/906c391c-76e5-4966-aa8d-82acf17cb08e" />

Fungsi push dipakai buat masukin data baru ke stack. Pertama bikin Node baru dengan Node(x). Lalu Node baru diarahkan ke Node yang sebelumnya ada di atas lewat new_node.next = self.top_ptr. Setelah itu, self.top_ptr = new_node bikin Node baru jadi posisi paling atas. Terakhir ada print(...) buat nunjukin kalau data berhasil ditambah.


<img width="444" height="143" alt="image" src="https://github.com/user-attachments/assets/c4e865db-8169-4133-add0-9de9ee37f131" />

Fungsi pop dipakai buat ngeluarin data paling atas. Kalau stack kosong, langsung keluar pesan. Kalau ada, data teratas disimpan dulu di temp, terus ditampilkan dengan print(...). Setelah itu, self.top_ptr = self.top_ptr.next bikin posisi atas pindah ke Node berikutnya.


<img width="409" height="113" alt="image" src="https://github.com/user-attachments/assets/79dd3b3a-920b-45b4-94ee-ba8ecc961be8" />

Fungsi peek dipakai buat ngintip data paling atas tanpa ngeluarin. Kalau kosong, keluar pesan. Kalau ada, langsung ditampilkan nilai data di atas.


<img width="461" height="204" alt="image" src="https://github.com/user-attachments/assets/2b1c17d5-8012-4ddd-af15-add5b3f52aec" />

Fungsi display dipakai buat nunjukin semua isi stack dari atas sampai bawah. Pertama dicek kosong atau nggak. Kalau ada isi, mulai dari Node teratas (current = self.top_ptr) lalu ditampilkan satu-satu pakai looping while. Setiap data dicetak, lalu pindah ke Node berikutnya dengan current = current.next.


<img width="372" height="221" alt="image" src="https://github.com/user-attachments/assets/cde660b2-56b3-4b20-8aec-1db7ed69d595" />

Fungsi main ini jadi program utama. Pertama bikin stack kosong dengan stack = StackLinkedList(). Variabel pilih dipakai buat simpan pilihan menu. Lalu ada looping while pilih != 6: supaya menu terus muncul sampai user pilih keluar.


<img width="269" height="94" alt="image" src="https://github.com/user-attachments/assets/2e73360e-a623-4ae1-a5ba-c6498a02f537" />

Bagian ini buat baca input dari user. Kalau input bisa diubah jadi angka, disimpan ke pilih. Kalau salah ketik (misalnya huruf), langsung keluar pesan “Input tidak valid”.


<img width="222" height="53" alt="image" src="https://github.com/user-attachments/assets/3bedf98d-b25f-401a-91de-c07552b4a19f" />

Baris terakhir ini buat ngecek apakah file dijalankan langsung. Kalau iya, program utama main() akan dijalankan.

OUTPUT

<img width="296" height="714" alt="image" src="https://github.com/user-attachments/assets/3c514798-4bac-4524-9cdb-0afd5b9f5867" />
<img width="333" height="715" alt="image" src="https://github.com/user-attachments/assets/59027ba3-fbb1-49ca-a628-fbf27b7ce052" />

Jika dijalankan output program ini akan menampilkan urutan proses sesuai menu yang dipilih. Misalnya, ketika pengguna memilih Push dan memasukkan “merah” lalu “biru”, program akan menuliskan pesan bahwa piring merah dan biru berhasil ditambahkan ke rak. Saat memilih Display, program menampilkan isi rak dari atas ke bawah, sehingga terlihat urutan piring biru di atas merah. Jika pengguna memilih Peek, program akan menampilkan piring teratas yaitu biru. Ketika dilakukan Pop, piring biru diambil dari rak dan ditampilkan sebagai data yang dihapus. Setelah itu, jika kembali memilih Display, isi rak hanya menampilkan piring merah. Menu Hitung akan menampilkan jumlah piring yang tersisa, dalam kasus ini satu. Terakhir, saat memilih Keluar, program akan menghapus semua piring yang tersisa satu per satu, menampilkan pesan setiap kali piring diambil, lalu menutup program dengan pesan “Program selesai.”

Link vidio youtube : https://youtu.be/MPSEAPYJCiY
