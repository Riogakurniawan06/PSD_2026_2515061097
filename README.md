# PSD_2026_2515061097
PSD C_2515061097_PSTI C

Program di atas berfungsi untuk mengelola antrian pasien di rumah sakit dengan cara menambahkan pasien baru ke dalam antrian (enqueue), melayani pasien dari depan antrian (dequeue), serta menampilkan daftar pasien yang sedang menunggu. Dengan begitu, sistem ini meniru proses nyata di rumah sakit, di mana pasien dilayani sesuai urutan kedatangan.

Algoritma yang digunakan adalah struktur data Queue (FIFO – First In, First Out) yang diimplementasikan menggunakan linked list. Artinya, pasien yang pertama masuk antrian akan menjadi yang pertama dilayani. Setiap node (PatientNode) menyimpan nama pasien dan pointer ke pasien berikutnya, sedangkan HospitalQueue mengatur posisi depan (front) dan belakang (rear) dari antrian. Struktur ini efisien untuk operasi tambah dan hapus karena tidak perlu menggeser elemen seperti pada array.


1. Class PatientNode
-<img width="287" height="93" alt="Screenshot 2026-04-28 233635" src="https://github.com/user-attachments/assets/d213850f-5307-4ca7-9c7f-6fdf369cebc7" />

Bagian ini mendefinisikan struktur node untuk setiap pasien. Node adalah elemen dasar dari linked list.
-self.name menyimpan nama pasien.
-self.next adalah pointer yang menunjuk ke pasien berikutnya dalam antrian. Awalnya bernilai None karena ketika node baru dibuat, belum ada sambungan ke node lain.
Dengan cara ini, setiap pasien bisa dihubungkan satu sama lain membentuk rantai (linked list).

2. Class HospitalQueue
-<img width="241" height="92" alt="Screenshot 2026-04-28 234502" src="https://github.com/user-attachments/assets/59c37c9c-292e-42c8-a3e7-a71a6c693999" />

Bagian ini mendefinisikan struktur antrian pasien.
-front menunjuk ke pasien paling depan (yang akan dilayani pertama).
-rear menunjuk ke pasien paling belakang (yang baru masuk).
Saat pertama kali dibuat, antrian kosong sehingga front dan rear bernilai None.

3. Method enqueue (menambahkan pasien)
-<img width="383" height="149" alt="Screenshot 2026-04-28 234536" src="https://github.com/user-attachments/assets/478cb5e5-df90-481f-9a07-6479f334359b" />

Fungsi ini menambahkan pasien baru ke dalam antrian.
-Pertama, dibuat node baru dari nama pasien (new_patient).
-Jika antrian kosong (rear is None), maka pasien pertama akan menjadi front sekaligus rear.
-Jika antrian sudah ada pasien, maka pasien baru ditambahkan di belakang (rear.next = new_patient), lalu rear diperbarui menunjuk ke pasien baru.
Inilah operasi enqueue dalam queue.

4. Method dequeue (melayani pasien)
-<img width="420" height="211" alt="Screenshot 2026-04-28 234543" src="https://github.com/user-attachments/assets/2b3e4e7e-5c7d-4f24-baa7-b20e99c0fd6e" />

Fungsi ini melayani pasien dari depan antrian.
-Jika antrian kosong (front is None), tampilkan pesan bahwa tidak ada pasien.
-Jika ada pasien, ambil nama pasien depan (served).
-Geser front ke pasien berikutnya (self.front.next).
-Jika setelah digeser antrian kosong, maka rear juga dihapus (None).
-Cetak nama pasien yang dilayani, lalu kembalikan nama tersebut.
Inilah operasi dequeue dalam queue.

5. Method show_queue (menampilkan antrian)
-<img width="300" height="176" alt="Screenshot 2026-04-28 234547" src="https://github.com/user-attachments/assets/43c3033c-0673-4a90-9d74-17d21374652b" />

Fungsi ini menampilkan daftar pasien yang ada dalam antrian.
-Mulai dari pasien paling depan (front).
-Jika kosong, tampilkan pesan "Antrian kosong".
-Jika ada pasien, lakukan looping dari depan ke belakang, cetak nama pasien satu per satu, lalu pindah ke node berikutnya (current = current.next).
Dengan cara ini, seluruh isi antrian bisa ditampilkan.

6. Main Program
-<img width="605" height="249" alt="Screenshot 2026-04-28 234552" src="https://github.com/user-attachments/assets/446a907e-ac48-4136-9e09-10f864d440b3" />

Bagian ini adalah inti program yang dijalankan.
-Membuat objek queue dari kelas HospitalQueue.
-Meminta input jumlah pasien (n).
-Looping: meminta nama pasien satu per satu, lalu menambahkan ke antrian dengan enqueue.
-Menampilkan daftar pasien dengan show_queue.
-Proses pelayanan: melayani pasien pertama dengan dequeue, lalu menampilkan sisa antrian.


7. OUPUT
Input jumlah pasien  
Program pertama-tama meminta berapa banyak pasien yang ingin ditambahkan ke antrian. Misalnya kita masukkan 3.
-<img width="422" height="76" alt="Screenshot 2026-04-28 235020" src="https://github.com/user-attachments/assets/f118ff8e-2929-4937-98a7-75579f16650d" />
Setelah itu, ketiga nama pasien dimasukkan ke dalam antrian dengan berurutan.

-<img width="230" height="192" alt="Screenshot 2026-04-28 234939" src="https://github.com/user-attachments/assets/246fcbc1-4d69-4ee2-8797-45fce391506f" />
Sebelum pelayanan: semua pasien ditampilkan sesuai urutan kedatangan.
Saat pelayanan: pasien paling depan dilayani (FIFO).
Setelah pelayanan: daftar pasien diperbarui, menampilkan sisa pasien yang belum dilayani.
Dengan output ini, kita bisa melihat jelas bagaimana queue berbasis linked list bekerja: pasien pertama masuk → pasien pertama keluar (dilayani) → antrian bergeser ke pasien berikutnya.

LINK YUOTUBE = https://youtu.be/ikhPijL3U50
