TUGAS AKHIR HASH MAP (LEMARI SEPATU)

Kodingan ini adalah contoh implementasi Hash Map dengan metode Open Addressing dan Linear Probing. Intinya, program membuat sebuah tabel hash yang terdiri dari slot-slot kosong. Setiap slot direpresentasikan oleh class Entry, yang menyimpan key, value, dan status slot apakah kosong, terisi, atau sudah dihapus. Fungsi hash_function dipakai untuk menentukan posisi penyimpanan berdasarkan key, lalu fungsi insert digunakan untuk menambahkan data ke tabel. Jika slot sudah terisi, program akan mencari slot berikutnya dengan cara linear probing sampai menemukan tempat kosong atau slot yang pernah dihapus. Dengan cara ini, data bisa tetap dimasukkan meskipun terjadi tabrakan (collision).

Selain menambah data, program juga menyediakan fungsi search untuk mencari apakah sebuah key ada di dalam tabel, remove_key untuk menghapus data dengan cara menandai slot sebagai DELETED, dan display untuk menampilkan isi tabel hash. Bagian main() adalah simulasi penggunaan dengan analogi lemari sepatu: beberapa sepatu dimasukkan dengan ukuran tertentu, lalu ditampilkan isi tabel, dicari sepatu dengan ukuran tertentu, dihapus, dan dicek kembali apakah sepatu lain masih ada. Jadi kodingan ini memperlihatkan bagaimana struktur hash map bekerja dalam menyimpan, mencari, memperbarui, dan menghapus data dengan cara yang efisien, sambil tetap menjaga agar slot yang pernah dipakai bisa digunakan kembali.

PENJELASAN KODINGAN INI


<img width="159" height="89" alt="image" src="https://github.com/user-attachments/assets/d29802a7-77cf-4545-992e-efa95bad98b1" />

Bagian ini bikin class SlotState yang isinya hanya penanda kondisi slot. Jadi setiap kotak di tabel hash bisa punya status: kosong (EMPTY), sedang dipakai (OCCUPIED), atau sudah dihapus (DELETED). Dengan adanya status ini, program bisa tahu apakah slot masih bisa dipakai atau tidak.


<img width="314" height="104" alt="image" src="https://github.com/user-attachments/assets/f512c43e-906f-4629-b40b-cdf8220bbb44" />

Class Entry ini ibarat satu kotak di tabel hash. Di dalamnya ada key untuk menyimpan kunci, value untuk isi data, dan state untuk status slot. Awalnya semua slot dianggap kosong, jadi belum ada data yang masuk.


<img width="457" height="94" alt="image" src="https://github.com/user-attachments/assets/7eae2d77-4922-4c89-a14b-45afb9bcb75b" />

Class HashMapOpenAddressing adalah struktur utama hash map. Saat dibuat, ukurannya default 10 slot. Lalu dibuat list berisi objek Entry sebanyak ukuran tersebut, sehingga tabel hash siap dipakai untuk menyimpan data.


<img width="423" height="43" alt="image" src="https://github.com/user-attachments/assets/971e29a6-becc-4e65-bff8-692d9cc4e5f5" />

Fungsi ini menentukan posisi slot berdasarkan key. Caranya dengan operasi modulo, sehingga key apapun akan jatuh ke indeks antara 0 sampai ukuran tabel. Ini penting supaya data bisa ditempatkan secara merata.


<img width="613" height="484" alt="image" src="https://github.com/user-attachments/assets/ead75e8c-6f56-493b-94ea-1d53918cce2d" />

Fungsi insert dipakai untuk menambahkan data. Pertama dihitung posisi awal dengan hash_function. Kalau slot sudah terisi, program akan maju ke slot berikutnya (linear probing) sampai ketemu slot kosong atau slot yang pernah dihapus. Kalau key yang sama sudah ada, value-nya diperbarui. Jadi data bisa tetap masuk meskipun terjadi tabrakan.


<img width="666" height="177" alt="image" src="https://github.com/user-attachments/assets/55a7e5ce-3109-48b3-9cd7-00b68063f1f3" />


Fungsi search dipakai untuk mencari data berdasarkan key. Program mulai dari posisi hasil hash, lalu maju satu per satu. Kalau ketemu slot kosong berarti data tidak ada. Kalau ketemu slot terisi dengan key yang sama, data dikembalikan.


<img width="316" height="122" alt="image" src="https://github.com/user-attachments/assets/12b9c7f3-90e9-4cd7-9ac3-5583916201bf" />

Fungsi ini menghapus data. Caranya dengan mencari dulu key yang dimaksud. Kalau ketemu, status slot diubah jadi DELETED. Jadi slot itu tidak langsung kosong, tapi ditandai sudah dihapus supaya pencarian tetap bisa berjalan dengan benar.


<img width="532" height="200" alt="image" src="https://github.com/user-attachments/assets/2b54b54f-0ab3-450d-8cc5-b4487fbc5452" />

Fungsi display menampilkan isi tabel hash. Setiap slot ditampilkan sesuai statusnya: kosong, dihapus, atau berisi pasangan key dan value. Ini berguna untuk melihat kondisi tabel secara keseluruhan.


<img width="330" height="144" alt="image" src="https://github.com/user-attachments/assets/c5ebd71f-a21d-4ec3-9d91-fcf560b64fd0" />

Bagian main() adalah simulasi penggunaan. Pertama dibuat objek lemari sebagai hash map. Lalu dimasukkan beberapa data sepatu dengan ukuran tertentu. Key 42 awalnya berisi “Nike Air”, lalu diperbarui jadi “Nike Jordan”. Setelah itu isi tabel ditampilkan.


<img width="468" height="104" alt="image" src="https://github.com/user-attachments/assets/2c4f54bf-30c8-4e87-acba-66a007846470" />

Di sini program mencari sepatu dengan key 43. Kalau ketemu, ditampilkan value-nya. Kalau tidak, muncul pesan bahwa sepatu tidak ada.


<img width="381" height="73" alt="image" src="https://github.com/user-attachments/assets/50c8fb1f-8224-440d-8977-5398aef1b026" />

Bagian ini menghapus sepatu dengan key 43. Setelah dihapus, isi tabel ditampilkan lagi untuk menunjukkan perubahan. Slot yang dihapus ditandai sebagai DELETED.


<img width="481" height="103" alt="image" src="https://github.com/user-attachments/assets/39ce0caf-7355-4e2e-8fc4-c65ed3252456" />

Bagian ini program mengecek apakah sepatu dengan key 44 masih ada. Kalau ada, ditampilkan value-nya. Kalau tidak, muncul pesan bahwa sepatu tidak ada.


PENJELASAN OUTPUT


<img width="512" height="527" alt="image" src="https://github.com/user-attachments/assets/56366521-561e-4f91-b684-3ac018e0cd69" />

Pertama, program menambahkan beberapa data sepatu ke dalam tabel hash. Sepatu dengan key 42 awalnya dimasukkan sebagai “Nike Air”, lalu key 43 berisi “Adidas Samba”, key 44 berisi “Converse High”. Setelah itu, key 42 dimasukkan lagi dengan value baru “Nike Jordan”, sehingga data lama di key 42 otomatis diperbarui. Ketika fungsi display() dipanggil, tabel hash menampilkan isi slot: ada yang kosong (EMPTY), ada yang berisi pasangan (key, value), dan nanti ada juga yang bisa berubah jadi DELETED.

Selanjutnya, program mencari sepatu dengan key 43. Karena sebelumnya sudah dimasukkan, hasil pencarian menampilkan “Sepatu ukuran 43 ditemukan: Adidas Samba”. Setelah itu, sepatu dengan key 43 dihapus. Slot yang tadinya berisi data tidak langsung kosong, tetapi ditandai sebagai DELETED. Fungsi display() dipanggil lagi, dan kita bisa melihat perubahan di tabel hash.

Terakhir, program mencari sepatu dengan key 44. Karena sepatu “Converse High” masih ada dan belum dihapus, hasil pencarian menampilkan “Sepatu ukuran 44 masih ada: Converse High”. Setelah semua langkah selesai, program berhenti.


LINK YOUTUBE = https://youtu.be/fFDStRTThko
