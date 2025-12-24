
# Laporan Praktikum Minggu [9]
Topik: ["Simulasi Algoritma Penjadwalan CPU"]

---

## Identitas
- **Nama**  : [Lutfi Khoerunnisa]  
- **NIM**   : [250202947]  
- **Kelas** : [1IKRB]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
1. Membuat program simulasi algoritma penjadwalan FCFS dan/atau SJF.
2. Menjalankan program dengan dataset uji yang diberikan atau dibuat sendiri.
3. Menyajikan output simulasi dalam bentuk tabel atau grafik.
4. Menjelaskan hasil simulasi secara tertulis.
5. Mengunggah kode dan laporan ke Git repository dengan rapi dan tepat waktu.


## Dasar Teori
1. Konsep Dasar Penjadwalan CPU: Merupakan mekanisme utama dalam sistem operasi multiprogramming untuk memaksimalkan utilitas CPU. Tujuannya adalah memastikan CPU selalu sibuk dengan cara beralih di antara berbagai proses yang berada dalam antrean (ready queue).
2. Kriteria Penjadwalan: Digunakan sebagai parameter untuk mengukur efisiensi algoritma. Kriteria utama meliputi Waiting Time (total waktu tunggu proses di ready queue), Turnaround Time (waktu total dari saat proses masuk hingga selesai), dan Response Time (waktu sejak permintaan masuk hingga respons pertama diberikan).
3. Gantt Chart sebagai Alat Simulasi: Dalam percobaan, Gantt Chart digunakan untuk memvisualisasikan urutan eksekusi proses secara kronologis. Diagram ini memudahkan penghitungan statistik performa algoritma seperti rata-rata waktu tunggu (Average Waiting Time).
---

## Langkah Praktikum
1. Menyiapkan Dataset Buat dataset proses minimal berisi data yang telah disajikan.
2. Implementasi Algoritma
Program harus: Menghitung waiting time dan turnaround time.
               Mendukung minimal 1 algoritma (FCFS atau SJF non-preemptive).
               Menampilkan hasil dalam tabel.
3. Eksekusi & Validasi : Jalankan program menggunakan dataset uji. Pastikan hasil sesuai dengan perhitungan manual minggu sebelumnya.Simpan Hasil Screenshot.
4. Analisis :  Jelaskan alur program.
               Bandingkan hasil simulasi dengan perhitungan manual.
               Jelaskan kelebihan dan keterbatasan simulasi.
5. Commit & Push
git add .
git commit -m "Minggu 9 - Simulasi Scheduling CPU"
git push origin main


---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
praktikum/week9-sim-scheduling/
├─ code/
│  ├─ scheduling_simulation.*
│  └─ dataset.csv
├─ screenshots/
│  └─ hasil_simulasi.png
└─ laporan.md
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshots hasil](./screenshots/Hasil%20eksekusi.png)

---

## Analisis
1. Hasil di terminal menunjukkan simulasi bagaimana CPU mengelola empat proses (P1 hingga P4). Algoritma FCFS bekerja dengan prinsip antrean: siapa yang datang lebih dulu, dia yang dilayani.
Urutan Kedatangan (Arrival Time): P1 datang pertama pada detik ke-0, disusul P2 (detik 1), P3 (detik 2), dan P4 (detik 3).
Waktu Tunggu (Waiting Time):P1 langsung dikerjakan (tunggu = 0).P4 memiliki waktu tunggu tertinggi (18) karena harus menunggu P1, P2, dan P3 selesai diproses.
Waktu Penyelesaian (Turnaround Time): Ini adalah total waktu sejak proses datang hingga selesai. Misalnya, P4 datang pada detik ke-3 dan selesai pada detik ke-21 (total 18 detik menunggu + 3 detik pengerjaan = 21).

2. Fungsi Kernel (Penjadwal/Scheduler): Kernel bertindak sebagai "polisi lalu lintas". Bagian kernel yang disebut Short-Term Scheduler adalah yang memutuskan proses mana dari antrean ready yang akan diberikan akses ke CPU berdasarkan algoritma (dalam hal ini FCFS).
System Call: Saat program simulasi ini berjalan dan menampilkan teks ke layar (print), ia melakukan System Call (seperti write pada Linux atau WriteFile pada Windows). Ini adalah jembatan bagi program pengguna untuk meminta bantuan kernel mencetak data ke perangkat output (terminal).
Arsitektur OS (Context Switching): Meskipun simulasi ini terlihat sederhana, dalam arsitektur OS asli, perpindahan dari P1 ke P2 melibatkan Context Switching. Kernel harus menyimpan status (register, PC) proses yang lama ke dalam Process Control Block (PCB) dan memuat status proses baru agar eksekusi bisa dilanjutkan tanpa kehilanga
3. Path File: Windows menggunakan backslash (contoh: C:\Users\ASUS), sedangkan Linux menggunakan forward slash (contoh: /home/user).Manajemen Memori: Linux umumnya lebih efisien dalam membuat proses baru (process forking) dibandingkan Windows yang memiliki overhead lebih besar.


---

## Kesimpulan
1. Efektivitas Algoritma FCFS: Hasil percobaan menunjukkan bahwa algoritma First-Come, First-Served sangat bergantung pada urutan kedatangan; proses yang datang terakhir (P4) mengalami waktu tunggu yang sangat tinggi (18 satuan waktu) karena harus menunggu selesainya proses-proses sebelumnya, yang dalam teori dikenal sebagai Convoy Effect.

2. Peran Kernel dan Sistem: Secara teoretis, eksekusi ini mencerminkan fungsi Short-Term Scheduler pada kernel dalam mengelola antrean proses, di mana setiap output yang muncul di terminal merupakan hasil dari System Call untuk berinteraksi dengan perangkat keras melalui arsitektur sistem operasi.

3. Pengaruh Lingkungan OS: Terdapat perbedaan teknis yang terlihat dari penggunaan Windows (seperti pada gambar) yang menggunakan backslash (\) dalam jalur file dan manajemen process creation yang lebih berat, dibandingkan dengan Linux yang menggunakan forward slash (/) dan mekanisme forking yang lebih ringan untuk menangani proses serupa.

---

## Quiz
1. [Mengapa simulasi diperlukan untuk menguji algoritma scheduling?]  
   **Jawaban:Simulasi sangat penting untuk menguji algoritma penjadwalan karena memungkinkan pengembang untuk menganalisis perilaku algoritma secara aman tanpa risiko merusak sistem operasi yang sedang berjalan (live system). Melalui simulasi, variabel kompleks seperti waktu kedatangan dan durasi proses dapat dimanipulasi dengan mudah untuk mengamati fenomena seperti convoy effect atau starvation secara berulang dalam lingkungan yang terkontrol. Selain itu, simulasi jauh lebih efisien dari segi biaya dan waktu dibandingkan melakukan pengujian pada perangkat keras nyata, sehingga memudahkan perbandingan performa antar algoritma secara objektif sebelum diimplementasikan ke dalam kernel yang sesungguhnya.**  
2. [Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar?]  
   **Jawaban:Perhitungan manual sangat berisiko terhadap kesalahan manusia (human error) dan menjadi tidak praktis karena membutuhkan waktu yang sangat lama untuk memproses ribuan data secara beruntun. Sebaliknya, simulasi komputer mampu mengolah dataset besar dalam hitungan milidetik dengan akurasi yang presisi, serta memudahkan pembaruan data secara otomatis tanpa harus mengulang perhitungan dari awal. Selain itu, simulasi memungkinkan pembuatan visualisasi statistik dan Gantt Chart yang rumit secara instan, sehingga memudahkan analisis performa algoritma yang sulit dicapai melalui cara manual.**  
3. [Algoritma mana yang lebih mudah diimplementasikan? Jelaskan.]  
   **Jawaban:Algoritma yang paling mudah diimplementasikan adalah First-Come, First-Served (FCFS) karena logikanya hanya menggunakan prinsip antrean sederhana atau FIFO (First-In, First-Out). Dalam implementasi kodenya, pengembang tidak perlu membuat fungsi pengurutan ulang yang rumit seperti pada Shortest Job First (SJF) atau mengatur interupsi kuantum waktu seperti pada Round Robin, melainkan cukup mengeksekusi proses berdasarkan urutan kedatangannya saja. Algoritma ini juga memiliki beban sistem (overhead) yang sangat rendah karena tidak memerlukan prediksi waktu pengerjaan di masa depan, sehingga struktur datanya sangat ringkas dan mudah dipahami bagi pemula dalam pemrograman sistem operasi.**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
**Menjalankan pyhton**
- Bagaimana cara Anda mengatasinya?  
**Mencoba**

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
