TUGAS JUDUL 2: MEMBUAT PROGRAM MENGURUTKAN TINGGI BADAN MAHASIWA PSTI

Program ini berfungsi untuk mengurutkan data tinggi badan mahasiswa supaya lebih teratur dan mudah dibaca. Cara kerjanya, pengguna diminta memasukkan jumlah mahasiswa dan tinggi badan masing-masing. Data yang dimasukkan pertama kali ditampilkan dalam kondisi acak, lalu diproses menggunakan algoritma Bubble Sort. Setelah proses pengurutan selesai, hasilnya ditampilkan kembali sehingga urutan tinggi badan mahasiswa terlihat dari yang paling pendek sampai yang paling tinggi. Dengan begitu, program ini membantu menyusun data agar lebih rapi dan bisa dipakai untuk analisis sederhana.  

Algoritma yang dipakai adalah Bubble Sort, yaitu salah satu algoritma pengurutan dasar dalam struktur data. Bubble Sort bekerja dengan cara membandingkan dua elemen yang berdekatan, lalu menukar posisinya jika urutannya salah. Proses ini diulang terus sampai semua data berada pada posisi yang benar. Algoritma ini sering dijadikan contoh di perkuliahan karena konsepnya mudah dipahami, meskipun dari segi kecepatan masih kalah dibanding algoritma pengurutan lain yang lebih efisien.

PENJELASAN

<img width="197" height="87" alt="Screenshot 2026-05-05 172649" src="https://github.com/user-attachments/assets/8e5ba969-e7ca-460e-878e-bd629ac47437" />
Bagian ini berfungsi untuk menukar posisi dua elemen dalam array. Nilai elemen ke-i disimpan sementara di variabel temp, lalu elemen ke-i diganti dengan elemen ke-j. Terakhir, elemen ke-j diganti dengan nilai awal elemen ke-i. Dengan cara ini, dua data bisa saling bertukar posisi.


<img width="306" height="108" alt="Screenshot 2026-05-05 173405" src="https://github.com/user-attachments/assets/a0ea0e6a-a173-4c2a-94fb-548dea52984d" />
Bagian ini berfungsi untuk mengurutkan array menggunakan algoritma Bubble Sort. Loop luar (for i in range(n - 1)) mengatur jumlah perulangan, sedangkan loop dalam (for j in range(n - i - 1)) membandingkan elemen bersebelahan. Jika elemen kiri lebih besar dari elemen kanan, maka dipanggil fungsi tukar untuk menukar posisinya. Proses ini diulang sampai seluruh data terurut.


<img width="457" height="134" alt="Screenshot 2026-05-05 173514" src="https://github.com/user-attachments/assets/d5b72ae7-167f-4d47-874c-0a7964b6c580" />
Bagian ini berfungsi sebagai fungsi utama program. Pertama, program meminta input jumlah mahasiswa. Jika input bukan angka, maka akan muncul pesan “Input tidak valid!” dan program berhenti. Dengan cara ini, data yang dimasukkan lebih terkontrol.


<img width="537" height="204" alt="Screenshot 2026-05-05 173617" src="https://github.com/user-attachments/assets/de08bdb5-a8b2-42f2-a0e5-625a135e20e5" />
Bagian ini berfungsi untuk mengisi data tinggi badan mahasiswa. List tinggi dibuat kosong terlebih dahulu. Program kemudian meminta input tinggi badan satu per satu sesuai jumlah mahasiswa. Jika input bukan angka, program akan meminta ulang sampai data valid. Setiap tinggi badan yang valid ditambahkan ke dalam list tinggi.


<img width="506" height="131" alt="Screenshot 2026-05-05 173730" src="https://github.com/user-attachments/assets/1a18f296-2c26-4ebc-bfbe-9c3d8a67e75e" />
Bagian ini berfungsi untuk menampilkan data sebelum dan sesudah diurutkan. Pertama, program mencetak list tinggi badan sebelum diurutkan. Lalu memanggil fungsi bubble_sort untuk mengurutkan data. Setelah itu, program mencetak hasil urutan tinggi badan mahasiswa dari yang paling pendek hingga paling tinggi.


<img width="224" height="56" alt="Screenshot 2026-05-05 173814" src="https://github.com/user-attachments/assets/1903e230-2565-4f17-bd74-f1c75d6cc344" />
Bagian ini berfungsi untuk menjalankan fungsi main() ketika file dijalankan langsung. Dengan cara ini, program akan otomatis meminta input dan menampilkan hasil sesuai alur yang sudah dibuat.


<img width="483" height="200" alt="Screenshot 2026-05-05 184355" src="https://github.com/user-attachments/assets/ce11fde4-5e4c-4634-ad52-bc996e38afa3" />
Ketika program dijalankan, pertama akan muncul permintaan untuk memasukkan jumlah mahasiswa. Setelah itu, pengguna diminta memasukkan tinggi badan satu per satu. Program akan menampilkan data tinggi badan sesuai urutan input (belum diurutkan). Kemudian, setelah proses Bubble Sort dijalankan, hasilnya ditampilkan kembali dalam kondisi sudah terurut dari yang paling pendek sampai yang paling tinggi.

LINK VIDIO YOUTUBE : https://youtu.be/wHizNuaftq4
