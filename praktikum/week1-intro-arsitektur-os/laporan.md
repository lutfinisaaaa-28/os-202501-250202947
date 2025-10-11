
# Laporan Praktikum Minggu [X]
Topik:  "Arsitektur Sistem Operasi dan Kernel"

---

## Identitas
- **Nama**  : [Lutfi Khoerunnisa]  
- **NIM**   : [250202947]  
- **Kelas** : [1IKRB]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
> Mahasiswa mampu membuat visual code,gitbash.

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.
Sistem operasi adalah perangkat lunak dasar yang mengelola semua sumber daya perangkat keras dan lunak komputer serta menjadi perantara antara pengguna dan perangkat keras.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.
 Setup Environment

Pastikan Linux (Ubuntu/WSL) sudah terinstal.
Pastikan Git sudah dikonfigurasi dengan benar:
git config --global user.name "Nama Anda"
git config --global user.email "email@contoh.com"
Diskusi Konsep

Baca materi pengantar tentang komponen OS.
Identifikasi komponen yang ada pada Linux/Windows/Android.
Eksperimen Dasar Jalankan perintah berikut di terminal:

uname -a
whoami
lsmod | head
dmesg | head
Catat dan analisis modul kernel yang tampil.

Membuat Diagram Arsitektur

Buat diagram hubungan antara User → System Call → Kernel → Hardware.
Gunakan draw.io atau Mermaid.
Simpan hasilnya di:
praktikum/week1-intro-arsitektur-os/screenshots/diagram-os.png
Penulisan Laporan

Tuliskan hasil pengamatan, analisis, dan kesimpulan ke dalam laporan.md.
Tambahkan screenshot hasil terminal ke folder screenshots/.
Commit & Push

git add .
git commit -m "Minggu 1 - Arsitektur Sistem Operasi dan Kernel"
git push origin main

2. Perintah yang dijalankan.  
Menjelaskan peran sistem operasi dalam arsitektur komputer.
Mengidentifikasi komponen utama OS (kernel, system call, device driver, file system).
Membandingkan model arsitektur OS (monolithic, layered, microkernel).
Menggambarkan diagram sederhana arsitektur OS menggunakan alat bantu digital (draw.io / mermaid).

3. File dan kode yang dibuat. 
code github,code visual code,code gitbash 
4. Commit message yang digunakan.
git add .

git commit -m "Minggu 1 - Arsitektur Sistem Operasi dan Kernel"

git push origin main

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
whoami
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](./screenshots/Screenshot%202025-10-11%20210447.png)

---

## Analisis
- Jelaskan makna hasil percobaan.

      * uname -a   adalah perintah di Linux yang digunakan untuk menampilkan semua informasi detail tentang sistem, termasuk nama kernel, nama mesin 
      *  uname -a adalah perintah di Linux yang digunakan untuk menampilkan semua informasi detail tentang sistem, termasuk nama kernel, nama mesin (
         *  Perintah lsmod digunakan untuk menampilkan daftar modul kernel yang saat ini sedang dimuat (loaded) di sistem. Modul kernel ini bisa berupa driver perangkat keras atau modul fungsional lainnya yang digunakan oleh kernel Linux
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).
Hasil dapat dihubungkan dengan fungsi kernel sebagai inti sistem operasi yang menjembatani hardware dan software; panggilan sistem (\(syscall\)) sebagai jembatan antara aplikasi pengguna dan kernel untuk meminta layanan; dan arsitektur OS yang mendefinisikan struktur ini, di mana kernel menjadi komponen sentral yang mengelola sumber daya melalui panggilan sistem. 

- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?
  Perbedaan hasil antara Linux dan Windows terlihat dari struktur sistem file (garis miring / di Linux vs `C:\` di Windows), cara penamaan berkas (bisa ada dua berkas dengan nama sama di direktori berbeda di Linux, tidak bisa di Windows), sistem partisi (Linux lebih fleksibel, Windows mendukung partisi Linux namun Linux belum tentu mendukung partisi Windows), dan penggunaan baris perintah (terminal di Linux lebih ampuh, cmd di Windows lebih terbatas).

---

## Kesimpulan
Monolithic kernel adalah arsitektur sistem operasi di mana semua layanan inti OS, seperti manajemen memori, penjadwalan proses, dan manajemen perangkat keras, berjalan dalam satu ruang alamat (satu program besar)bagian dapat menyebabkan crash seluruh.Mikrokernel adalah jenis kernel sistem operasi yang hanya berisi fungsionalitas inti minimal, seperti manajemen memori dan komunikasi antarproses (IPC), sementara layanan lainnya (seperti driver perangkat dan sistem berkas) berjalan di ruang pengguna Arsitektur berlapis (layered architecture) adalah pola desain perangkat lunak yang membagi aplikasi menjadi beberapa lapisan terpisah, di mana setiap lapisan memiliki tanggung jawab tertentu dan hanya berinteraksi dengan lapisan di bawahnya. sebagai server terpisah.

---

## Quiz
1. [ Sebutkan tiga fungsi utama sistem operasi]
   **Jawaban:** 
   Tiga fungsi utama sistem operasi adalah Manajemen Sumber Daya, Manajemen Proses dan File, serta Penyediaan Antarmuka Pengguna
2. [Jelaskan perbedaan antara kernel mode dan user mode]  
   **Jawaban:** 
   Perbedaan utama antara mode kernel dan mode pengguna adalah tingkat akses dan hak istimewa terhadap sumber daya sistem. 
3. [Sebutkan contoh OS dengan arsitektur monolithic dan microkernel]  
   **Jawaban:**  
   Contoh OS arsitektur monolitik antara lain adalah Linux dan varian Unix tradisional (seperti BSD), sementara contoh OS dengan arsitektur mikrokernel (monokernel) adalah GNU Hurd

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
semua menantang leptop rusak 
- Bagaimana cara Anda mengatasinya?  
bersabar

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
