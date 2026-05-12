TUGAS JUDUL 3 = MENCARI UKURAN SEPATU

Program ini berfungsi untuk mencari ukuran sepatu tertentu di rak dengan menggunakan algoritma pencarian biner (binary search). Cara kerjanya, pengguna diminta memasukkan jumlah sepatu dan ukuran masing-masing sepatu yang sudah dalam keadaan terurut menaik. Setelah itu, pengguna memasukkan ukuran sepatu yang ingin dicari. Program kemudian akan melakukan proses pencarian dengan membagi rak menjadi dua bagian, mengecek posisi tengah, lalu menentukan apakah ukuran yang dicari ada di sebelah kiri atau kanan. Dengan metode ini, pencarian menjadi lebih cepat dibandingkan pencarian biasa karena tidak perlu mengecek satu per satu dari awal sampai akhir.

Algoritma yang dipakai adalah Binary Search, yaitu salah satu algoritma pencarian dalam struktur data. Binary Search bekerja dengan prinsip “bagi dua”, di mana data yang sudah terurut dibagi menjadi dua bagian, lalu dibandingkan dengan nilai tengah. Jika nilai tengah sama dengan yang dicari, maka pencarian selesai. Jika lebih kecil, pencarian dilanjutkan ke bagian kanan, dan jika lebih besar, pencarian dilanjutkan ke bagian kiri. Proses ini diulang sampai data ditemukan atau sampai batas pencarian habis. Algoritma ini sangat efisien karena jumlah langkah pencarian berkurang drastis dibandingkan metode pencarian linear.

<img width="414" height="81" alt="image" src="https://github.com/user-attachments/assets/bad0433f-d237-45c8-8561-f5d3460d02fe" />
Bagian ini berfungsi untuk mendefinisikan fungsi cari_sepatu yang akan mencari ukuran sepatu di dalam rak. Variabel kiri menunjuk ke indeks paling awal, kanan menunjuk ke indeks paling akhir, dan posisi diset ke -1 sebagai tanda bahwa sepatu belum ditemukan.

<img width="607" height="74" alt="image" src="https://github.com/user-attachments/assets/14801dad-0dd6-4449-aefb-4dd2eff235ad" />
Bagian ini berfungsi untuk melakukan perulangan pencarian selama batas kiri belum melewati kanan. Variabel tengah digunakan untuk menghitung posisi tengah rak, lalu program menampilkan informasi posisi tengah dan ukuran sepatu yang sedang dicek.

<img width="330" height="64" alt="image" src="https://github.com/user-attachments/assets/c88cfeb2-2514-412d-a527-535442ed05a8" />
Bagian ini berfungsi untuk mengecek apakah ukuran sepatu di posisi tengah sama dengan ukuran yang dicari. Jika sama, maka variabel posisi diisi dengan indeks tengah dan pencarian dihentikan dengan break.

<img width="472" height="66" alt="image" src="https://github.com/user-attachments/assets/3e886070-36c3-4071-81b6-07d86be40ef8" />
Bagian ini berfungsi untuk menentukan arah pencarian jika ukuran di tengah lebih kecil dari ukuran yang dicari. Program akan menampilkan pesan untuk mencari di sebelah kanan, lalu variabel kiri digeser ke tengah + 1.

<img width="504" height="83" alt="image" src="https://github.com/user-attachments/assets/6a3e48be-b874-48d7-86f6-638a9bffd3b7" />
Bagian ini berfungsi untuk menentukan arah pencarian jika ukuran di tengah lebih besar dari ukuran yang dicari. Program menampilkan pesan untuk mencari di sebelah kiri, lalu variabel kanan digeser ke tengah - 1. Setelah perulangan selesai, fungsi mengembalikan nilai posisi.

<img width="522" height="125" alt="image" src="https://github.com/user-attachments/assets/2f48bb35-b4b3-4257-958a-6376e6a83cb7" />
Bagian ini berfungsi sebagai fungsi utama. Program meminta input jumlah sepatu di rak. Jika input bukan angka, maka muncul pesan error dan program berhenti.

<img width="410" height="200" alt="image" src="https://github.com/user-attachments/assets/20958402-b783-4247-9eed-946972723645" />
Bagian ini berfungsi untuk mengisi data ukuran sepatu ke dalam list rak_sepatu. Program meminta input ukuran sepatu satu per satu sesuai jumlah yang dimasukkan. Jika input salah, program akan meminta ulang sampai benar.

<img width="291" height="32" alt="image" src="https://github.com/user-attachments/assets/eec6476d-918c-49f0-a8b3-56f483b263f3" />
Bagian ini berfungsi untuk menampilkan isi rak sepatu setelah semua data dimasukkan.

<img width="602" height="118" alt="image" src="https://github.com/user-attachments/assets/cf0c9f34-467e-4799-8e57-d5518306bcb1" />
Bagian ini berfungsi untuk meminta input ukuran sepatu yang ingin dicari. Jika input salah, program akan meminta ulang sampai benar.

<img width="645" height="107" alt="image" src="https://github.com/user-attachments/assets/0f2e5ce0-167c-4813-9271-02829a2d5443" />
Bagian ini berfungsi untuk memanggil fungsi cari_sepatu dan menyimpan hasil pencarian ke variabel posisi. Jika posisi tidak sama dengan -1, berarti sepatu ditemukan dan program menampilkan posisi rak. Jika tidak ditemukan, program menampilkan pesan bahwa sepatu tidak ada.

<img width="237" height="54" alt="image" src="https://github.com/user-attachments/assets/1b50fb4e-df01-4d79-9e8e-a3c86452a4da" />
Bagian ini berfungsi untuk menjalankan fungsi main() ketika file dijalankan langsung. Dengan cara ini, program akan otomatis meminta input dan menampilkan hasil pencarian.

PENJELASAN OUTPUT
<img width="351" height="222" alt="image" src="https://github.com/user-attachments/assets/4d4125de-b129-4400-8381-546d2c286dc6" />
Ketika program dijalankan, pertama pengguna diminta memasukkan jumlah sepatu dan ukuran masing-masing sepatu dalam urutan menaik. Program kemudian menampilkan isi rak sepatu. Setelah itu, pengguna memasukkan ukuran sepatu yang ingin dicari. Program akan menampilkan proses pencarian, mulai dari mengecek posisi tengah, lalu menentukan apakah harus mencari ke kiri atau ke kanan. Jika ukuran sepatu ditemukan, program menampilkan posisi rak tempat sepatu berada. Jika tidak ditemukan, program menampilkan pesan bahwa ukuran tersebut tidak ada di rak.
