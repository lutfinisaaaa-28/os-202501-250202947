
# Laporan Praktikum Minggu [11]
Topik: ["Simulasi dan Deteksi Deadlock"]

---

## Identitas
- **Nama**  : [Lutfi Khoerunnisa]  
- **NIM**   : [250202947]  
- **Kelas** : [1IKRB]

---

## Tujuan
1. Membuat program sederhana untuk mendeteksi deadlock.
2. Menjalankan simulasi deteksi deadlock dengan dataset uji.
3. Menyajikan hasil analisis deadlock dalam bentuk tabel.
4. Memberikan interpretasi hasil uji secara logis dan sistematis.
5. Menyusun laporan praktikum sesuai format yang ditentukan.

---

## Dasar Teori
1. Definisi Deadlock: Kondisi di mana sekumpulan proses saling menunggu sumber daya secara permanen sehingga eksekusi terhenti total.

2. Kondisi Coffman: Deadlock hanya terjadi jika empat syarat terpenuhi serentak: Mutual Exclusion, Hold and Wait, No Preemption, dan Circular Wait.

3. Deteksi & RAG: Identifikasi dilakukan menggunakan Resource Allocation Graph (RAG); jika terdapat siklus (cycle) dalam graf alokasi tersebut, maka sistem terdeteksi mengalami deadlock.

---

## Langkah Praktikum
1. Menyiapkan Dataset Gunakan dataset sederhana yang berisi:
Daftar proses
Resource Allocation
Resource Request / Need
2. Implementasi Algoritma Deteksi Deadlock
Program minimal harus:
Membaca data proses dan resource.
Menentukan apakah sistem berada dalam kondisi deadlock.
Menampilkan proses mana saja yang terlibat deadlock.
3. Eksekusi & Validasi
Jalankan program dengan dataset uji.
Validasi hasil deteksi dengan analisis manual/logis.
Simpan hasil eksekusi dalam bentuk screenshot.
4. Analisis Hasil
Sajikan hasil deteksi dalam tabel (proses deadlock / tidak).
Jelaskan mengapa deadlock terjadi atau tidak terjadi.
Kaitkan hasil dengan teori deadlock (empat kondisi).
5. Commit & Push
git add .
git commit -m "Minggu 11 - Deadlock Detection"
git push origin main



---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
praktikum/week11-deadlock-detection/
├─ code/
│  ├─ deadlock_detection.*
│  └─ dataset_deadlock.csv
├─ screenshots/
│  └─ hasil_deteksi.png
└─ laporan.md
```

---

## Hasil Eksekusi Def Detect_Deadlock
![Screenshot hasil](./screenshots/def%20detect.png)

---

## Analisis
1. Analisis Hasil Deteksi

| Proses | Status| Keterangan|
| :--- | :---: | ---: |
|P1| Deadlock|Terlibat dalam siklus karena memegang R2 dan meminta R1. |
|P2| Deadlock| Terlibat dalam siklus karena memegang R3 dan meminta R2. |
|P3 | Deadlock| Terlibat dalam siklus karena memegang R1 dan meminta R3.|

2. Analisis Penyebab Deadlock
Deadlock terjadi karena sistem berada dalam kondisi di mana setiap proses menunggu sumber daya yang sedang dipegang oleh proses lain dalam sebuah rantai yang tidak terputus. Berdasarkan output terminal, program mendeteksi adanya jalur siklus: R1 -> P1 -> R2 -> P2 -> R3 -> P3 -> R1. Karena setiap sumber daya dalam simulasi ini bersifat tunggal dan tidak dapat digunakan bersama, maka tidak ada satu pun proses yang dapat menyelesaikan tugasnya, menyebabkan sistem berhenti total (stagnan).

3. Hasil simulasi pada file def detect.png membuktikan teori deadlock melalui terbentuknya siklus R1 -> P1 -> R2 -> P2 -> R3 -> P3 -> R1, yang memenuhi syarat Circular Wait. Kondisi ini terjadi karena setiap proses memegang satu sumber daya sambil menunggu sumber daya lain (Hold and Wait) yang bersifat eksklusif (Mutual Exclusion) dan tidak dapat diambil paksa (No Preemption). Akibat terpenuhinya keempat syarat Coffman tersebut secara simultan, sistem mengalami kebuntuan permanen karena tidak ada proses yang dapat menyelesaikan eksekusinya.

---

## Kesimpulan
1. Validasi Teori Circular Wait: Praktikum membuktikan bahwa deadlock terjadi ketika terbentuk siklus alokasi sumber daya yang tertutup (P1 → R2 → P2 → R3 → P3 → R1), yang memenuhi kondisi Circular Wait dari syarat Coffman.

2. Efektivitas Deteksi Graf: Penggunaan Resource Allocation Graph (RAG) terbukti efektif untuk mendeteksi kebuntuan sistem secara otomatis dengan cara mengidentifikasi adanya siklus antar proses dan sumber daya yang saling menunggu.

3. Kondisi Stagnasi Sistem: Hasil deteksi menunjukkan bahwa ketika deadlock terjadi, semua proses yang terlibat (P1, P2, P3) akan berhenti secara permanen karena tidak ada sumber daya yang dapat dilepaskan untuk memutus rantai ketergantungan tersebut.

---

## Quiz
1. [Apa perbedaan antara deadlock prevention, avoidance, dan detection?]  
   **Jawaban:a. Deadlock Prevention (Pencegahan): Strategi ini bekerja sangat dini dengan cara memastikan bahwa setidaknya satu dari empat kondisi Coffman (seperti Hold and Wait atau Circular Wait) tidak akan pernah terpenuhi. Metodenya sangat restriktif, misalnya mewajibkan proses meminta semua sumber daya sekaligus di awal.
   b. Deadlock Avoidance (Penghindaran): Strategi ini lebih dinamis dibandingkan pencegahan karena sistem memeriksa setiap permintaan sumber daya secara real-time. Sistem akan menghitung apakah pemberian sumber daya akan membawa sistem ke dalam "State Tidak Aman" (Unsafe State) yang berisiko deadlock; jika ya, permintaan tersebut ditunda (contohnya menggunakan Algoritma Banker).
   c.Deadlock Detection (Deteksi): Strategi ini bersifat reaktif, di mana sistem membiarkan deadlock terjadi, lalu secara periodik menjalankan algoritma untuk memeriksa apakah ada siklus pada graf alokasi sumber daya (Resource Allocation Graph). Seperti yang terlihat pada simulasi Anda (def detect.png), deteksi berfungsi mengidentifikasi proses mana yang sudah terjebak agar bisa dilakukan tindakan pemulihan (recovery).**  
2. [Mengapa deteksi deadlock tetap diperlukan dalam sistem operasi?]  
   **Jawaban:Deteksi deadlock diperlukan karena memberikan keseimbangan antara efisiensi penggunaan sumber daya dan fleksibilitas sistem dibandingkan metode pencegahan yang terlalu kaku. Strategi ini membiarkan sistem bekerja maksimal dan hanya melakukan intervensi saat kebuntuan benar-benar terjadi, sehingga utilisasi sumber daya tetap tinggi. Selain itu,deteksi sangat penting untuk mengidentifikasi proses dan sumber daya spesifik yang terlibat dalam siklus agar tindakan pemulihan dapat dilakukan tanpa menghentikan seluruh sistem.**  
3. [Apa kelebihan dan kekurangan pendekatan deteksi deadlock?]  
   **Jawaban:a.Kelebihan Meningkatkan utilisasi sumber daya karena sistem tidak dibatasi aturan pencegahan yang kaku, sehingga proses berjalan lebih fleksibel. Intervensi hanya dilakukan saat masalah benar-benar terjadi, memungkinkan identifikasi proses spesifik yang terjebak untuk pemulihan yang tepat sasaran.
   b.Kekurangan Menimbulkan beban komputasi (overhead) karena algoritma deteksi harus berjalan rutin. Selain itu, pemulihan sering kali menyebabkan hilangnya data akibat penghentian proses paksa, serta berisiko menimbulkan starvation pada proses tertentu yang terus-menerus dikorbankan.**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
