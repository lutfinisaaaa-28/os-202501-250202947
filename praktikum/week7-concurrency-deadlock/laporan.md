
# Laporan Praktikum Minggu [7]
Topik: Sinkronisasi Proses dan Masalah Deadlock

---

## Identitas
- **Nama Kelompok**  :

 [Lutfi Khoerunnisa Bertugas Dokumentasi] [250202947] ,

 [Alya Deviana Putri Reynaldi Bertugas Ketua Kelompok] [250202928] , 

 [Muslimah Nuraini Bertugas Implementasi] [250202980] ,

 [Aster Rifani Bertugas Analisis] [250202915]

- **Kelas** : [1IKRB]

---

## Tujuan
 
1.  Mengidentifikasi empat kondisi penyebab deadlock (mutual exclusion, hold and wait, no preemption, circular wait).

2. Menjelaskan mekanisme sinkronisasi menggunakan semaphore atau monitor.

3.  Menganalisis dan memberikan solusi untuk kasus deadlock.

4.  Berkolaborasi dalam tim untuk menyusun laporan analisis.

5.  Menyajikan hasil studi kasus secara sistematis.

---

## Pendahuluan
Masalah Dining Philosophers merupakan model klasik dalam ilmu sistem operasi yang mengilustrasikan risiko deadlock pada proses konkurensi. Dalam skenario ini, lima filosof berbagi lima garpu, di mana setiap filosof memerlukan dua garpu untuk melakukan aktivitas makan. Tanpa adanya mekanisme pencegahan, kondisi deadlock dapat muncul ketika semua filosof menahan satu garpu dan menunggu garpu lainnya yang dipegang oleh filosof tetangga, sehingga terbentuk siklus tunggu.

---

## Dasar Teori
- Deadlock
   Terjadinya dua atau lebih proses saling menunggu sumber daya yang tidak akan pernah terjadi karena saling mengunci. Ada empat kondisi yang menyebabkan deadlock,yaitu:  
    1. Mutual Exclusion
    2. Hold and Wait
    3. No Preemption
    4. Circular Wait
- Critical section
   Bagian dari kode yang dimana proses mengakses data bersama.
- Mutual exclusion (Mutex)
   Memastikan hanya satu proses yang dapat berada di critical section dalam satu waktu.
- Teknik Sinkronisasi
   1. Mutex
      - Hanya satu proses yang boleh memegang lock pada satu waktu.
      - Cocok untuk melindungi resource tunggal.
      - Jika lock diambil proses lain harus menunggu.
   2. Semaphore
      - Variabel sinkronisasi yang dapat bernilai lebih dari 1.
      - Operasi dasar : wait (P) dan signal (V)
      - Digunakan untuk mengelola akses ke sejumlah sumber daya tertentu atau mengatur antrian proses.
- Dining Philosophers problem
   Permasalahan yang diperkenalkan untuk menggambarkan masalah sinkronisasi dalam berbagi sumber daya terbatas.
   Konsep Dasar:
   - Terdapat N filsuf yang duduk mengelilingi meja.
   - Di antara setiap dua filsuf terdapat satu garpu.
   - Untuk makan, setiap filsuf membutuhkan dua garpu.
   - Jika semua filsuf mengambil satu garpu dan menunggu garpu kedua, deadlock dapat terjadi.

---

## Metode
1. - Eksperimen 1 – Simulasi Dining Philosophers (Deadlock Version)*
   Pada eksperimen ini simulasi dasar Dining Philosophers di mana setiap proses mengambil garpu kiri lalu garpu kanan tanpa mekanisme pencegah deadlock. Tujuannya adalah mengamati kapan deadlock terjadi, yaitu saat semua Philosopher memegang satu garpu dan menunggu garpu lainnya secara bersamaan.
2. - *Eksperimen 2 – Versi Fixed (Menggunakan Semaphore)*
   Pada eksperimen ini ditambahkan mekanisme sinkronisasi berupa *semaphore dengan nilai N−1* untuk membatasi hanya maksimal empat Philosopher yang dapat memasuki area makan. Pembatasan ini mencegah semua garpu diambil bersamaan sehingga memutus terjadinya circular wait dan menghilangkan deadlock.
3. - Eksperimen 3 – Analisis Deadlock*
   Menganalisis empat kondisi penyebab deadlock pada versi pertama serta menjelaskan bagaimana versi fixed memecah tiap kondisi. Hasil analisis disajikan dalam tabel yang membandingkan kondisi deadlock pada kedua versi.


---
## Langkah Praktikum
1. Bentuk kelompok beranggotakan 3–4 orang.
2. Implementasikan versi sederhana dari masalah Dining Philosophers tanpa mekanisme pencegahan deadlock.
3. Jalankan simulasi atau analisis alur (boleh menggunakan pseudocode atau diagram alur).
Identifikasi kapan dan mengapa deadlock terjadi.
4. Modifikasi pseudocode agar deadlock tidak terjadi, misalnya:
Menggunakan semaphore (mutex) untuk mengontrol akses.
Membatasi jumlah filosof yang dapat makan bersamaan (max 4).
Mengatur urutan pengambilan garpu (misal, filosof terakhir mengambil secara terbalik).
Analisis hasil modifikasi dan buktikan bahwa deadlock telah dihindari.
5. Jelaskan empat kondisi deadlock dari versi pertama dan bagaimana kondisi tersebut dipecahkan pada versi fixed
6. Commit dan upload tugas tepat waktu.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
while true:
  think()
  pick_left_fork()
  pick_right_fork()
  eat()
  put_left_fork()
  put_right_fork()
  ```

---

## Hasil Eksekusi
1. **Eksperimen 1 – Simulasi Dining Philosophers (Deadlock Version)**

![Screenshot hasil](./screenshots/Simulasi%20Dining.png)

2. **Eksperimen 2 – Versi Fixed (Menggunakan Semaphore / Monitor)**

![Screenshot hasil](./screenshots/Versi%20Fixed.png)

---

## Analisis
1. **Eksperimen 1 – Simulasi Dining Philosophers (Deadlock Version)**
![Screenshot hasil](./screenshots/Simulasi%20Dining.png)
Deadlock pada kode Dining Philosophers terjadi ketika semua philosopher secara bersamaan berhasil mengambil garpu kiri, lalu masing-masing mencoba mengambil garpu kanan yang ternyata sedang dipegang oleh philosopher di sebelahnya, sehingga setiap thread memegang satu garpu dan menunggu garpu lainnya tanpa ada satu pun yang bisa melanjutkan; kondisi ini memenuhi pola circular wait, sehingga tidak ada garpu yang dilepas dan seluruh proses berhenti di pemanggilan 'right.acquire().'

2. **Eksperimen 2 – Versi Fixed (Menggunakan Semaphore / Monitor)**
![Screenshot hasil](./screenshots/Versi%20Fixed.png)
Strategi penanganan Deadlock yang paling efektif adalah dengan membatasi jumlah proses yang dapat bersaing untuk sumber daya (N-1), seperti membatasi 4 filosof untuk 5 garpu. Modifikasi ini secara langsung melanggar kondisi Tunggu Melingkar (Circular Wait) dan Tahan dan Tunggu (Hold and Wait), sehingga sistem dijamin tidak akan pernah masuk ke dalam kondisi kebuntuan permanen (Deadlock). 

3. **Eksperimen 3**

 | Kondisi Deadlock |Terjadi di Versi Deadlock | Strategi Solusi (Tujuan Teori Pencegahan) |
| :--- | :---: | ---: |
|  Mutual Exclusion (Saling Pengecualian)| Ya | Dipertahankan (Ini dibutuhkan untuk integritas data; Dicegah menggunakan Lock/Semaphore).|
|Hold and Wait (Tahan dan Tunggu)| Ya |Dihindari dengan memastikan proses harus mengambil semua sumber daya yang diperlukan secara simultan atau melepaskannya jika gagal mendapatkan yang kedua.|
| No Preemption (Tidak Ada Pemberhentian Paksa) | Ya |Dihindari dengan mengizinkan pelepasan paksa sumber daya yang ditahan, atau dengan melepaskan secara sukarela sumber daya yang ditahan jika permintaan sumber daya tambahan gagal.  |
| Circular Wait (Tunggu Melingkar)| Ya | Dihindari dengan mengubah urutan pengambilan sumber daya (misalnya, membuat satu filosof mengambil garpu dengan urutan terbalik, atau menggunakan urutan pengindeksan global). |
| |  |  |

     


## Diskusi 

Dari hasil percobaan, dapat diketahui bahwa versi pertama program mengalami deadlock karena setiap filosof saling menunggu garpu yang tidak pernah dilepas. Setelah diterapkan mekanisme pencegahan (semaphore/aturan pengambilan garpu), program dapat berjalan tanpa kebuntuan. Hal ini menunjukkan bahwa sinkronisasi sangat penting untuk memastikan proses dapat berjalan bersamaan tanpa saling menghambat, serta membuktikan bahwa pengaturan akses sumber daya mampu mencegah deadlock secara efektif.

---



## Kesimpulan
1. Analisis Kode Awal (Deadlock Terjadi): Kode Filosof Makan awal membuktikan bahwa jika semua empat kondisi Deadlock (Mutual Exclusion, Hold and Wait, No Preemption, dan Circular Wait) terpenuhi secara simultan, Deadlock pasti terjadi, mengakibatkan sistem macet permanen (Starvation).
2. Sinkronisasi Proses menekankan bahwa Mutual Exclusion (Saling Pengecualian) adalah syarat fundamental untuk menjaga integritas data dan mencegah Race Condition di Critical Section. Namun, meskipun Mutual Exclusion diterapkan, kegagalan dalam manajemen sumber daya tetap dapat terjadi.
3. Solusi untuk Deadlock terletak pada pelanggaran salah satu dari empat kondisi pembentuknya. Analisis modifikasi kode, seperti membatasi jumlah proses menjadi N-1 (misalnya, 4 filosof untuk 5 garpu), secara efektif menghindari kebuntuan permanen. Strategi ini berhasil karena memutus rantai tunggu melingkar dan menjamin bahwa selalu ada jalan keluar (safe state), sehingga semua proses pada akhirnya dapat maju. 
---

## Quiz
1. [Sebutkan empat kondisi utama penyebab deadlock] 

   **Jawaban:Mutual Exclusion (Saling Pengecualian),Hold and Wait (Tahan dan Tunggu),No Preemption (Tidak Ada Pemberhentian Paksa),Circular Wait (Tunggu Melingkar).**  
2. [Mengapa sinkronisasi diperlukan dalam sistem operasi?]

   **Jawaban:Sinkronisasi diperlukan dalam sistem operasi terutama untuk mengelola akses bersama ke sumber daya atau data oleh banyak proses atau thread yang berjalan secara bersamaan (concurrently), sehingga menjaga konsistensi dan integritas sistem.**  
3. [Jelaskan perbedaan antara semaphore dan monitor]  

   **Jawaban:perbedaan utama antara Semaphore dan Monitor adalah pada tingkat abstraksi dan penanganan Mutual Exclusion: Semaphore adalah variabel integer primitif berlevel rendah yang memerlukan programmer untuk secara eksplisit memanggil operasi wait dan signal untuk menjamin sinkronisasi, menjadikannya rentan terhadap kesalahan (bug); sebaliknya, Monitor adalah konstruksi bahasa tingkat tinggi berbasis objek yang mengelompokkan data bersama dan prosedur aksesnya, di mana Mutual Exclusion dijamin secara implisit oleh kompiler, menjadikannya mekanisme yang lebih aman, terstruktur, dan kurang rentan terhadap kesalahan programmer.**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
**Menjalankan pseudocode**
- Bagaimana cara Anda mengatasinya?  
**Berlatih dan Mencoba**

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
