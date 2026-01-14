
# Laporan Praktikum Minggu [14]
Topik: ["Penyusunan Laporan Praktikum Format IMRAD"]

---

## Identitas 
- **Nama**  : [Lutfi Khoerunnisa]  
- **NIM**   : [250202947]  
- **Kelas** : [1IKRB]

---

## 1. Pendahuluan (Introduction)
## 1.1 Latar Belakang
   Manajemen memori merupakan aspek krusial dalam sistem operasi yang berfungsi untuk mengelola memori utama agar dapat digunakan secara optimal oleh berbagai proses yang berjalan. Dalam sistem memori virtual, keterbatasan fisik RAM sering kali menjadi tantangan ketika banyak proses meminta ruang alokasi secara bersamaan, sebagaimana terlihat pada fenomena alokasi memori bertahap dalam pengujian kontainer. Untuk mengatasi hal ini, sistem operasi menggunakan teknik paging dan mekanisme page replacement.

   Algoritma page replacement diperlukan ketika terjadi page fault, yaitu kondisi di mana data yang dibutuhkan tidak ditemukan di RAM sehingga sistem harus memilih satu halaman (page) untuk dikeluarkan dan diganti dengan halaman baru. Tanpa pengelolaan dan batasan yang tepat, konsumsi memori yang tidak terkendali dapat menyebabkan degradasi performa sistem secara keseluruhan. Dua metode yang paling umum digunakan adalah First-In-First-Out (FIFO) yang bekerja berdasarkan urutan waktu kedatangan, dan Least Recently Used (LRU) yang bekerja berdasarkan riwayat penggunaan terakhir halaman tersebut.

## 1.2 Rumusan Masalah
1. Antara algoritma FIFO dan LRU, manakah yang lebih baik dalam mengelola memori agar tidak terjadi banyak kesalahan (fault)?
2. Apa yang akan terjadi pada sistem jika sebuah aplikasi dibiarkan memakai RAM tanpa batasan?
3. Apakah pemberian batas CPU dan RAM pada Docker benar-benar efektif melindungi komputer dari beban berlebih?

### 1.3 Tujuan
1. Mengimplementasikan algoritma page replacement FIFO dalam program.
2. Mengimplementasikan algoritma page replacement LRU dalam program.
3. Menjalankan simulasi page replacement dengan dataset tertentu.
4. Membandingkan performa FIFO dan LRU berdasarkan jumlah page fault.
5. Menyajikan hasil simulasi dalam laporan yang sistematis.

---

## 2. Metode (Methods)
## 2.1 Lingkungan Pengujian

Pengujian dilakukan dengan lingkungan sebagai berikut : 

   - Sistem Operasi : Windows
   - Metode Pengujian : Simulasi Manajemen Memori - Page Replacement (FIFO 7 LRU)
   - Jumlah Frame Memori : 3 Frame
   - Dataset : Isi String Tidak Selalu Tetap Tergantung Algoritma
   - Dokumentasi : Screenshot Hasil Eksekusi

Lingkungan pengujian dibuat seragam untuk memastikan hasil yang diperoleh bersifat objektif dan dapat dibandingkan.

## 2.2 Skenario Pengujian
Tujuannya adalah untuk membandingkan efisiensi dua metode penggantian halaman data dalam memori yang terbatas.

   1. Menyiapkan Dataset Yang Berisi Reference String Berikut :

      ``` 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2```

   2. Menentukan Jumlah Frame Yang Terdiri Dari 3 Frame.
   3. Menjalankan Simulasi Penggantian Halaman Menggunakan Algoritma FIFO Catat Setiap Page Hit Dan Page Fault.
Hitung Total Page Fault.
   4. Menjalankan Simulasi Penggantian Halaman Menggunakan Algoritma LRU Catat Setiap Page Hit Dan Page Fault.
Hitung total page fault.
   5. Menjalankan Program Untuk FIFO dan LRU Secara Konsisten.
   6. Menghitung Hasil FIFO Dan LRU Tersebut.

## 2.3 Variabel Pengukuran
Variabel yang digunakan dalam praktikum ini meliputi:
   - Variabel Bebas (Independent): Jenis algoritma yang digunakan (FIFO dan LRU)
   - Variabel Terikat (Dependent): Jumlah Page Fault (kegagalan memori) dan jumlah Page Hit (keberhasilan memori).
   - Variabel Kontrol: Reference String (Deret data) , Kapasitas Memori

## 2.4 Langkah Eksperimen
1. Menyiapkan reference string dan 3 frame memori.

   ```7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2```

2. Menjalankan simulasi algoritma FIFO kemudian catat dan hitung page fault.
3. Menghitung total page fault FIFO.
4. Menjalankan simulasi algoritma LRU dengan dataset yang sama.
5. Mencatat page hit dan page fault pada algoritma LRU.
6. Membandingkan hasil kedua algoritma.
7. Menyimpan bukti hasil eksekusi dalam bentuk screenshot.
8. Commit & Push
---

## 3. Hasil (Result)
## 3.1 Hasil Eksekusi Program
1. Algoritma Fifo
![Screenshot hasil](./screenshots/FIFO%20Page.png)

2. Algoritma LRU 
![Screenshot hasil](./screenshots/LRU%20Page.png)

## 3.2 Tabel Perbandingan Hasil 
| Algoritma | Jumlah Page Fault | Keterangan |
| :--- | :---: | ---: |
|1. | 10  | Mengganti halaman berdasarkan urutan waktu masuk pertama kali. |
|2.  | 9 |  Mengganti halaman yang paling lama tidak digunakan berdasarkan riwayat akses|

## 3.3 Temuan Hasil Tabel
Berdasarkan hasil simulasi, algoritma LRU terbukti lebih efisien dengan mencatat 9 Page Fault, sedangkan FIFO mencatat 10 Page Fault. Hal ini disebabkan karena FIFO mengganti halaman hanya berdasarkan urutan waktu masuk tanpa melihat riwayat pemakaian. Sebaliknya, LRU mampu menghasilkan 4 Page Hit karena mempertahankan data yang baru saja diakses, unggul satu poin dibandingkan FIFO yang hanya menghasilkan 3 Page Hit. Temuan ini menunjukkan bahwa LRU lebih optimal dalam meminimalkan kesalahan memori pada kapasitas 3 frame.



## 4. Pembahasan (Discussion)
## 4.1 Interpretasi Hasil
Berdasarkan hasil simulasi dengan 3 frame memori, algoritma LRU terbukti lebih efisien daripada FIFO. Algoritma FIFO mencatat 10 page fault karena mengganti halaman hanya berdasarkan urutan waktu masuk tanpa melihat riwayat pemakaian. Sebaliknya, LRU mampu menekan kegagalan menjadi 9 page fault dengan mempertahankan data yang baru saja diakses, sehingga menghasilkan 4 page hit atau satu poin lebih baik daripada FIFO. Selisih ini membuktikan bahwa LRU lebih optimal dalam memanfaatkan kapasitas memori yang terbatas untuk dataset tersebut.

## 4.2 Keterbatasan 
Eksperimen ini memiliki keterbatasan pada jumlah kapasitas memori (frame) yang hanya dipatok sebanyak 3 slot, sehingga efisiensi algoritma belum teruji pada skala memori yang lebih besar. Selain itu, panjang data input hanya terbatas pada 13 angka, yang menyebabkan perbedaan performa antara FIFO dan LRU hanya terpaut 1 angka fault (10 vs 9). Pada sisi pengujian Docker, pembatasan sumber daya masih berada di zona aman karena aplikasi hanya menggunakan 8.00% CPU dari batas 50% yang diberikan, sehingga perilaku sistem saat terjadi lonjakan beban ekstrem belum dapat teramati secara penuh melalui data ini.

## 4.3 Perbandingan Teori
- Prinsip Kerja dan Efisiensi: Secara teori, FIFO hanya mengganti halaman berdasarkan urutan waktu masuk sehingga menghasilkan 10 page fault, sedangkan LRU lebih cerdas dengan memantau riwayat akses yang terbukti lebih efisien dengan hanya 9 page fault.

- Akurasi Data (Hit Rate): FIFO memiliki kelemahan karena sering menghapus data yang sebenarnya masih diperlukan sehingga hanya mendapat 3 hit, sementara LRU mampu mempertahankan data aktif yang menghasilkan 4 hit dan membuktikan bahwa pendekatan berbasis riwayat penggunaan lebih optimal untuk memori terbatas.

---

## 5. Closing (Penutupan)
## 5.1 Kesimpulan 
- Efisiensi Algoritma: Algoritma LRU terbukti lebih unggul dengan mencatatkan 9 Page Fault dan 4 Page Hit, mengalahkan FIFO yang mencatatkan 10 Page Fault dan 3 Page Hit pada dataset yang sama.

- Akurasi Mekanisme: Keunggulan LRU terletak pada kemampuannya mempertahankan data yang sering diakses berdasarkan riwayat penggunaan, sementara FIFO memiliki kelemahan karena membuang data (seperti Page 0) hanya berdasarkan urutan waktu masuk.

- Stabilitas Sistem: Pengujian limitasi sumber daya pada Docker menunjukkan sistem berjalan sangat stabil dengan beban CPU hanya 8.00% dan RAM 32.57 MiB, yang membuktikan bahwa batasan sumber daya berhasil menjaga performa tetap di bawah limit yang ditentukan.

## 5.2 Saran
- Menambah Variasi Parameter
- Melakukan Stress Test
- Eksperimen Algoritma Lain

## 5.3 Quiz
1. [Mengapa format IMRAD membantu membuat laporan praktikum lebih ilmiah dan mudah dievaluasi?]
**Jawaban:** Format IMRAD (Introduction, Methods, Results, and Discussion) membantu membuat laporan praktikum lebih ilmiah dan mudah dievaluasi karena memberikan struktur logis yang konsisten untuk menyampaikan alur pikir penelitian.
2. [Apa perbedaan antara bagian Hasil dan Pembahasan?]
**Jawaban:** Bagian Hasil hanya menyajikan data objektif apa adanya, seperti temuan 9 page fault pada LRU dan 10 page fault pada FIFO. Sementara itu, Pembahasan menjelaskan alasan di balik angka tersebut, yakni mengapa LRU lebih efisien karena mempertimbangkan riwayat akses data dibandingkan FIFO yang hanya berdasarkan urutan waktu masuk. Singkatnya, Hasil menyajikan fakta angka, sedangkan Pembahasan memberikan analisis teoritisnya.
3. [Mengapa sitasi dan daftar pustaka penting, bahkan untuk laporan praktikum?]
**Jawaban:** Sitasi dan daftar pustaka sangat penting karena berfungsi sebagai bukti orisinalitas dan bentuk penghargaan terhadap teori yang digunakan, seperti algoritma FIFO dan LRU yang bukan merupakan temuan pribadi praktikan. Secara teknis, sitasi memperkuat kredibilitas laporan dengan menunjukkan bahwa analisis Anda didasarkan pada landasan ilmiah yang valid, bukan sekadar asumsi. Selain itu, daftar pustaka memudahkan pembaca atau dosen untuk melacak sumber asli jika ingin memverifikasi data atau memperdalam materi manajemen memori yang dibahas.

---

## Daftar Pustaka
1. Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). Operating System Concepts (10th ed.). Wiley.
2. Merkel, D. (2014). Docker: Lightweight Linux Containers for Consistent Development and Deployment. Linux Journal, 2014(239).

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? Membuat Laporan Imrad
- Bagaimana cara Anda mengatasinya?  Mencoba Dan Terus Mencoba

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
