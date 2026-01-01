# Laporan Praktikum Minggu [10]
Topik: ["Manajemen Memori – Page Replacement (FIFO & LRU)"]

---

## Identitas
- **Nama**  : [Lutfi Khoerunnisa]  
- **NIM**   : [250202947]  
- **Kelas** : [1IKRB]

---

## Tujuan  
1. Mengimplementasikan algoritma page replacement FIFO dalam program.
2. Mengimplementasikan algoritma page replacement LRU dalam program.
3. Menjalankan simulasi page replacement dengan dataset tertentu.
4. Membandingkan performa FIFO dan LRU berdasarkan jumlah page fault.
5. Menyajikan hasil simulasi dalam laporan yang sistematis.

---

## Dasar Teori
1. Konsep Virtual Memory & Page Fault: Memori virtual memungkinkan sistem menjalankan aplikasi besar dengan membagi data ke dalam satuan kecil (page). Jika page yang dibutuhkan tidak ada di RAM, terjadi Page Fault, yang memicu sistem untuk mencari dan memuat data tersebut dari disk.

2. Algoritma FIFO (First-In, First-Out): Algoritma paling sederhana yang mengganti halaman berdasarkan urutan waktu masuk; halaman yang paling lama berada di memori akan dihapus terlebih dahulu tanpa mempertimbangkan seberapa sering halaman tersebut diakses.

3. Algoritma LRU (Least Recently Used): Algoritma yang mengganti halaman berdasarkan riwayat penggunaan; halaman yang paling lama tidak digunakan oleh CPU akan diganti, karena dianggap memiliki probabilitas kecil untuk dibutuhkan kembali dalam waktu dekat.

---

## Langkah Praktikum
1. Menyiapkan Dataset
Gunakan reference string berikut sebagai contoh:
7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2
Jumlah frame memori: 3 frame.

2. Implementasi FIFO
Simulasikan penggantian halaman menggunakan algoritma FIFO.Catat setiap page hit dan page fault.Hitung total page fault.

3. Implementasi LRU
Simulasikan penggantian halaman menggunakan algoritma LRU.
Catat setiap page hit dan page fault.
Hitung total page fault.
4. Eksekusi & Validasi Jalankan program untuk FIFO dan LRU.Pastikan hasil simulasi logis dan konsisten.Simpan screenshot hasil eksekusi.
5. Analisis Perbandingan
Buat tabel perbandingan seperti berikut:
Algoritma	Jumlah Page Fault	Keterangan
FIFO	...	...
LRU	...	...
Jelaskan mengapa jumlah page fault bisa berbeda.
Analisis algoritma mana yang lebih efisien dan alasannya.
6. Commit & Push
git add .
git commit -m "Minggu 10 - Page Replacement FIFO & LRU"
git push origin main

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
praktikum/week10-page-replacement/
├─ code/
│  ├─ page_replacement.*
│  └─ reference_string.txt
├─ screenshots/
│  └─ hasil_simulasi.png
└─ laporan.md
```

---

## Hasil Eksekusi
1. FIFO Page Replacement Simulation
![Screenshots hasil](./screenshots/FIFO%20Page.png)
2. LRU Page Replacement Simulation
![Screenshots hasil](./screenshots/LRU%20Page.png)
3. Summary Page Replacement (FIFO vs LRU)
![Screenshots hasil](./screenshots/Sunmary%20Page.png)


---

## Analisis
1. Analisis Tabel Perbandingan :

| Algoritma| Jumlah Page Fault | Keterangan |
| :--- | :---: | ---: |
|1.| 10| Mengganti halaman berdasarkan urutan waktu masuk pertama kali. |
|2.| 9| Mengganti halaman yang paling lama tidak digunakan berdasarkan riwayat akses.|


2. Perbedaan jumlah page fault terjadi karena algoritma FIFO secara kaku mengganti halaman berdasarkan urutan waktu masuk tanpa mempedulikan aktivitas akses, sementara LRU lebih dinamis dengan mengganti halaman yang sudah paling lama tidak digunakan berdasarkan riwayat pemakaian. Hal ini terlihat pada simulasi Anda di mana LRU lebih efektif mempertahankan halaman yang sering diakses, sehingga menghasilkan 9 page fault, lebih rendah dibandingkan FIFO yang mencapai 10 page fault. Dengan demikian, LRU terbukti lebih efisien karena mampu meminimalkan kegagalan pemuatan halaman dengan cara mengutamakan data yang masih aktif digunakan oleh sistem.

3. Algoritma LRU lebih efisien karena menggunakan prinsip lokalitas waktu, yaitu mengganti halaman yang sudah paling lama tidak digunakan berdasarkan riwayat akses nyata. Dalam simulasi Anda, strategi ini berhasil menekan angka page fault menjadi 9 kali (lebih rendah dari FIFO yang 10 kali) karena mampu mempertahankan data yang masih aktif dibutuhkan oleh sistem.
---

## Kesimpulan
1. Efisiensi dan Akurasi: Algoritma LRU secara umum lebih efisien dibandingkan FIFO dalam meminimalkan page fault karena memanfaatkan prinsip lokalitas waktu (riwayat penggunaan), sedangkan FIFO sering kali kurang akurat karena hanya mengandalkan urutan waktu masuk tanpa mempedulikan kebutuhan CPU.

2. Kompleksitas Implementasi: FIFO adalah algoritma yang paling mudah diimplementasikan karena hanya memerlukan struktur data antrean (queue) sederhana, sementara LRU lebih kompleks dan membutuhkan overhead sistem yang lebih tinggi untuk melacak setiap akses halaman.

3. Anomali Belady: Percobaan membuktikan bahwa FIFO dapat mengalami Anomali Belady, di mana penambahan jumlah frame justru meningkatkan jumlah page fault, sedangkan LRU bersifat lebih stabil dan konsisten terhadap penambahan memori fisik.

---

## Quiz
1. [Apa perbedaan utama FIFO dan LRU?]  
   **Jawaban:FIFO (First-In, First-Out): Mengganti halaman berdasarkan urutan waktu masuk ke memori; halaman yang paling pertama masuk akan menjadi yang pertama keluar, tanpa mempedulikan seberapa sering halaman tersebut diakses oleh CPU.LRU (Least Recently Used): Mengganti halaman berdasarkan riwayat penggunaan; halaman yang sudah paling lama tidak digunakan akan diganti karena dianggap memiliki probabilitas kecil untuk dibutuhkan kembali dalam waktu dekat.**  
2. [Mengapa FIFO dapat menghasilkan Belady’s Anomaly?]  
   **Jawaban:Anomali Belady dapat terjadi pada algoritma FIFO karena mekanismenya hanya mengandalkan urutan waktu masuk tanpa mempertimbangkan pola akses halaman oleh CPU, sehingga ia tidak termasuk dalam kategori stack algorithm. Hal ini menyebabkan penambahan jumlah frame fisik tidak menjamin penurunan angka page fault; sebaliknya, perubahan urutan dalam antrean justru bisa mendorong keluar halaman yang akan segera dibutuhkan kembali oleh sistem. Akibatnya, memori yang lebih besar terkadang justru memperburuk performa karena halaman-halaman aktif lebih sering terusir dibandingkan saat kapasitas memori lebih kecil.**  
3. [Mengapa LRU umumnya menghasilkan performa lebih baik dibanding FIFO?]  
   **Jawaban:Algoritma LRU menghasilkan performa lebih baik karena menggunakan prinsip lokalitas waktu, yaitu memprioritaskan penyimpanan halaman yang baru saja diakses karena kemungkinan besar akan segera digunakan kembali. Berbeda dengan FIFO yang hanya melihat urutan waktu masuk, LRU secara dinamis membuang halaman yang sudah paling lama tidak aktif. Hal ini efektif meminimalkan page fault dan mempercepat kinerja sistem dengan mengurangi frekuensi pengambilan data dari penyimpanan sekunder.**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
