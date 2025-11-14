
# Laporan Praktikum Minggu [6]
Topik: [Penjadwalan CPU – Round Robin (RR) dan Priority Scheduling]

---

## Identitas
- **Nama**  : [Lutfi Khoerunnisa]  
- **NIM**   : [250202947]  
- **Kelas** : [1IKRB]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
> Menghitung waiting time dan turnaround time pada algoritma RR dan Priority.
> Menyusun tabel hasil perhitungan dengan benar dan sistematis.
> Membandingkan performa algoritma RR dan Priority.
> Menjelaskan pengaruh time quantum dan prioritas terhadap keadilan eksekusi proses.
> Menarik kesimpulan mengenai efisiensi dan keadilan kedua algoritma.

---

## Dasar Teori
1. Tujuan dan Prinsip Dasar Preemption (Preemptive Scheduling): Tujuan utama penjadwalan CPU adalah memaksimalkan efisiensi sambil memastikan keadilan (fairness) dan responsif yang cepat. Baik Round Robin (RR) maupun Priority Scheduling sering menggunakan prinsip preemption, yaitu kemampuan untuk menginterupsi proses yang sedang berjalan (meskipun belum selesai) agar CPU dapat dialihkan ke proses lain. Hal ini krusial untuk lingkungan time-sharing modern di mana banyak proses harus berbagi sumber daya CPU secara responsif dan adil.

2. Mekanisme Round Robin (Fairness melalui Time Quantum): Round Robin (RR) mencapai keadilan dengan memberikan setiap proses time quantum (unit waktu CPU yang kecil dan tetap) secara bergantian dalam antrian melingkar. Jika proses tidak selesai dalam quantum waktunya, proses tersebut akan diinterupsi (preempted) dan diletakkan di akhir antrian. Keuntungan utama RR adalah respons time yang baik dan mencegah starvation, namun kelemahannya adalah tingginya overhead context switch jika quantum terlalu kecil.

3. Mekanisme Priority Scheduling (Starvation dan Aging): Priority Scheduling mengalokasikan CPU ke proses dengan prioritas tertinggi. Prioritas ini dapat bersifat statis atau dinamis. Masalah signifikan dari algoritma ini adalah starvation, yaitu proses dengan prioritas rendah mungkin tidak pernah mendapatkan CPU jika terus-menerus ada proses prioritas tinggi yang masuk. Solusi umum untuk mengatasi starvation adalah Aging, di mana prioritas proses yang telah menunggu lama dalam sistem secara bertahap ditingkatkan.
---

## Langkah Praktikum
1. Siapkan Data Proses Gunakan contoh data berikut (boleh dimodifikasi sesuai kebutuhan)
2. Gunakan time quantum (q) = 3.
Hitung waiting time dan turnaround time untuk tiap proses.
Simulasikan eksekusi menggunakan Gantt Chart (manual atau spreadsheet).
| P1 | P2 | P3 | P4 | P1 | P3 | ...
0    3    6    9   12   15   18  ...
3. Urutkan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi).
Lakukan perhitungan manual untuk:
WT[i] = waktu mulai eksekusi - Arrival[i]
TAT[i] = WT[i] + Burst[i]
Buat tabel perbandingan hasil RR dan Priority.
4. Buat tabel perbandingan
5. Mengerjakan tugas dan quiz
6. Update tugas tepat waktu 
---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
| P1 | P2 | P3 | P4 | P1 | P3 | ...
0    3    6    9   12   15   18  ...
WT[i] = waktu mulai eksekusi - Arrival[i]
TAT[i] = WT[i] + Burst[i]
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](./screenshots/gabungan.png)
Eksperimen 1 Round Robin
![Screenshot hasil](./screenshots/RB.png)
| P1 | P2 | P3 | P4 | P1 | P3 | P4 | P3 |
0    3    6    9   12   14  17  20  22

Eksperimen 2 Priority Scheduling
![Screenshot hasil](./screenshots/PS.png)
| P1 | P2 | P4 | P3 | 
0    5    8    14   22   
Tabel Perbandingan Round Robin dan Priority Scheduling
![Screenshot hasil](./screenshots/Tabel%20perbandingan%20RB%20dan%20PS.png)

---

## Analisis
- Round Robin = Proses berjalan bergantian (seperti estafet), di mana setiap proses mendapat jatah waktu kecil yang sama (Time Quantum).
- Priority Scheduling = menentukan urutan eksekusi berdasarkan tingkat Prioritas dan kemudian mengukur seberapa lama proses menunggu dan menyelesaikan tugas.

---

## Kesimpulan
1. Keunggulan RR dan Isu Overhead: Percobaan Round Robin (RR) membuktikan bahwa algoritma ini optimal untuk mencapai keadilan (fairness) dan respons time yang cepat. Dengan menggunakan jatah waktu tetap (Time Quantum), RR mencegah starvation dan cocok untuk sistem time-sharing. Namun, kelemahannya adalah tingginya overhead context switch yang terjadi akibat seringnya perpindahan antar proses, yang dapat mengurangi efisiensi CPU secara keseluruhan.

2. Efektivitas Priority Scheduling dan Risiko Starvation: Priority Scheduling unggul dalam memastikan tugas-tugas kritis (berprioritas tinggi) diselesaikan dengan cepat. Algoritma ini memberikan turnaround time yang minimal bagi proses penting, sering kali menggunakan preemption untuk segera mengambil alih CPU. Namun, risiko terbesarnya adalah starvation, di mana proses berprioritas rendah mungkin tidak pernah dieksekusi, sehingga memerlukan implementasi teknik Aging untuk menjaga keadilan minimum.

3. Kompromi Pilihan Algoritma: Kesimpulannya, tidak ada algoritma yang sempurna; pemilihan didasarkan pada tujuan sistem. RR dikhususkan untuk keadilan merata dan responsifitas (mengorbankan sedikit efisiensi), sedangkan Priority Scheduling dikhususkan untuk mengutamakan tugas penting (mengorbankan keadilan bagi proses prioritas rendah).
---

## Quiz
1. [Apa perbedaan utama antara Round Robin dan Priority Scheduling?]  
   **Jawaban: Perbedaan utama antara Round Robin (RR) dan Priority Scheduling terletak pada dasar penentuan proses mana yang didahulukan dan tujuan utama yang ingin dicapai. RR beroperasi berdasarkan Time Quantum (jatah waktu tetap), di mana proses berjalan secara bergantian dan adil, sehingga RR dirancang untuk mencapai respons time yang cepat dan fairness di antara semua pengguna, namun memiliki kelemahan berupa potensi overhead context switch yang tinggi. Sebaliknya, Priority Scheduling beroperasi berdasarkan nilai Prioritas yang ditetapkan pada setiap proses, di mana proses prioritas tertinggi selalu dieksekusi terlebih dahulu. Algoritma ini bertujuan untuk memastikan tugas kritis diselesaikan secepat mungkin, namun memiliki risiko utama berupa starvation pada proses berprioritas rendah.**  
2. [Apa pengaruh besar/kecilnya time quantum terhadap performa sistem?]  
   **Jawaban: Pengaruh utama ukuran Jatah Waktu (Time Quantum) adalah menciptakan pertukaran (trade-off) penting antara responsifitas dan efisiensi sistem. Jika Jatah Waktu terlalu kecil, sistem menjadi sangat responsif dan adil karena proses sering berganti, namun hal ini meningkatkan biaya pergantian konteks (Context Switch) secara drastis, sehingga Unit Pemroses Sentral (CPU) menghabiskan lebih banyak waktu untuk mengelola pergantian daripada menjalankan pekerjaan nyata, yang pada akhirnya menurunkan efisiensi sistem. Sebaliknya, jika Jatah Waktu terlalu besar, biaya pergantian konteks menjadi minimal, yang meningkatkan efisiensi, tetapi responsifitas dan keadilan menurun tajam, menyebabkan algoritma Round Robin berperilaku mirip First-Come, First-Served karena proses di depan dapat memonopoli CPU untuk jangka waktu yang lama.**  
3. [Mengapa algoritma Priority dapat menyebabkan starvation?]  
   **Jawaban:Starvation pada algoritma Priority Scheduling terjadi karena kedatangan proses berprioritas tinggi yang terus-menerus. Karena CPU harus selalu memilih proses dengan prioritas tertinggi, proses prioritas rendah yang sudah siap akan terus ditunda tanpa batas waktu (preempted), sebab selalu ada proses yang lebih penting yang baru tiba atau sedang berjalan. Hal ini membuat proses berprioritas rendah "kelaparan" dari alokasi CPU. .**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? Menghitung Round Robin dan Priority Scheduling 
- Bagaimana cara Anda mengatasinya?  
Mencoba dan mencari referensi

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
