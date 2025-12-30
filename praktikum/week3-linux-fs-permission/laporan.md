
# Laporan Praktikum Minggu [3]
Topik: [Manajemen File dan Permission di Linux]

---

## Identitas
- **Nama**  : [Lutfi Khoerunnisa]  
- **NIM**   : [250202947]  
- **Kelas** : [1IKRB]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.    
> Menggunakan perintah ls, pwd, cd, cat untuk navigasi file dan direktori.
> Menggunakan chmod dan chown untuk manajemen hak akses file.
> Menjelaskan hasil output dari perintah Linux dasar.
> Menyusun laporan praktikum dengan struktur yang benar.
> Mengunggah dokumentasi hasil ke Git Repository tepat waktu.

---

## Dasar Teori
1. File tersebut adalah File Biasa (-) yang memiliki konfigurasi hak akses yang ketat bagi pengguna selain pemilik. Secara spesifik:
Pemilik (Owner) memiliki hak penuh (rwx): Mereka dapat Membaca, Menulis/Mengubah, dan Mengeksekusi file.
2. Grup (Group) memiliki hak terbatas (r-x): Mereka hanya dapat Membaca dan Mengeksekusi file, tetapi tidak dapat memodifikasinya.
3. Secara keseluruhan, permission ini sering digunakan untuk file yang dapat dieksekusi (seperti skrip atau program) yang boleh dibaca dan dijalankan oleh anggota grup, tetapi hanya boleh dimodifikasi oleh pemiliknya.

---

## Langkah Praktikum
1. Open folder praktikum/week3-linux-fs-permission/
2. Eksperimen satu navigasi file pwd,ls -l.cd /tmp,ls -a
3. Eksperimen 2 membaca file cat /etc/passwd | head -n 5
4. Masukan name dan chmod 600 percobaan.txt
5. Dokumentasi 
6. Push 

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
[Screenshot hasil](./screenshots/Week3.png)
[Screenshot hasil](./screenshots/week%203%20'.png)

 | Nomer | Perintah| Makna Hasil |
| :--- | :---: | ---: |
| Kondisi Deadlock | Terjadi di Versi Deadlock | Solusi di Versi Fixed |
| :--- | :---: | ---: |
     |kondisi | jalam |khvh |
     | Kondisi Deadlock | Terjadi di Versi Deadlock | Solusi di Versi Fixed |
     |jsksj| kdjd |jdjbf |
     
|2.| ls -lcd /tmp | Perintah ls -lcd /tmp di Linux memiliki fungsi untuk menampilkan detail file atau direktori /tmp saja, termasuk informasi hak akses (permissions), dan menggunakan timestamp waktu perubahan terakhir pada metadata (c-time).|
|3.| ls -a | Fungsi dari perintah ls -a di Linux adalah untuk menampilkan daftar semua file dan direktori dalam lokasi saat ini, termasuk file tersembunyi.ls: Perintah dasar untuk mendaftar isi suatu direktori.-a (all): Opsi ini (flag) memerintahkan ls untuk menyertakan file yang tersembunyi|

| Nomer | Perintah| Makna Hasil |
| :--- | :---: | ---: |
|1.|cat /etc/passwd | head -n 5|Percobaan cat /etc/passwd | head -n 5 memiliki makna fungsional untuk menampilkan lima baris pertama dari file konfigurasi pengguna sistem (/etc/passwd).Ini adalah contoh klasik penggunaan pipa (|) untuk merangkai dua perintah Linux:Analisis Percobaan
1. Perintah Pertama: cat /etc/passwd
cat (concatenate): Perintah ini membaca seluruh isi file /etc/passwd./etc/passwd: Ini adalah file teks penting dalam sistem Linux yang menyimpan informasi dasar tentang semua akun pengguna terdaftar, termasuk nama pengguna, ID pengguna (UID), ID grup (GID), home directory, dan shell default mereka.2. Pipa (|)
Pipa (|): Simbol ini berfungsi sebagai penghubung (redirector). Ini mengambil seluruh output dari perintah di sebelah kirinya (cat /etc/passwd) dan menjadikannya sebagai input untuk perintah di sebelah kanannya3. Perintah Kedua: head -n 5
head: Perintah ini dirancang untuk menampilkan baris-baris awal dari suatu file atau input yang diterima.-n 5: Opsi ini menentukan bahwa head harus membatasi outputnya hanya pada 5 baris pertama. |

| Nomer | Perintah| Makna Hasil |
| :--- | :---: | ---: |
|1.|echo "Hello Lutfi Khoerunnisa - 250202947" > percobaan.txt | mengganti nama 
|2.| ls -l percobaan.txt | untuk menampilkan detail lengkap dari file teks tersebut, termasuk hak akses, ukuran, dan kepemilikan.
|3.| chmod 600 percobaan.txt |Percobaan ini menghasilkan konfigurasi keamanan yang sangat tinggi, biasanya digunakan untuk:File Konfigurasi Rahasia: Seperti kunci SSH (id_rsa) atau file kata sandi pribadi yang tidak boleh dilihat, diubah, atau diakses oleh siapa pun selain pemilik akun.Privasi Maksimal: Memastikan bahwa file tersebut sepenuhnya privat dan terisolasi dari pengguna lain di sistem.|
---

## Quiz
1. [Apa fungsi dari perintah chmod?]  
   **Jawaban:Fungsi utama dari perintah chmod (singkatan dari Change Mode) di Linux adalah untuk mengubah hak akses (permissions) dari file dan direktori.Perintah ini memungkinkan pengguna untuk mengatur secara spesifik siapa (Pemilik, Grup, atau Lainnya) yang diizinkan untuk Membaca (r), Menulis/Mengubah (w), dan Mengeksekusi/Menjalankan (x) suatu objek.**
   2.[Apa arti dari kode permission rwxr-xr--?]
   **Jawaban:Kode permission rwxr-xr-- artinya:Pemilik (owner): Punya izin baca (r), tulis (w), dan eksekusi (x).Grup (group): Punya izin baca (r) dan eksekusi (x).Lainnya (others): Hanya punya izin baca (r).**
   3.[Jelaskan perbedaan antara chown dan chmod.]
   **Jawaban: Perbedaan utama adalah chmod mengubah hak akses (izin untuk membaca, menulis, mengeksekusi) pada sebuah berkas atau direktori, sedangkan chown mengubah kepemilikan (siapa pemilik dan grupnya). chmod menentukan apa yang dapat dilakukan, sementara chown menentukan siapa yang memiliki izin tersebut.**
   4.[Upload hasil dan laporan ke repositori Git sebelum deadline.]
   **Jawaban:**
   ---

   ## Tugas
   1.[Dokumentasikan hasil seluruh perintah pada tabel observasi di laporan.md]
   **Jawaban:**
   2. [Jelaskan fungsi tiap perintah dan arti kolom permission (rwxr-xr--).]
   **Jawaban:Perintah chmod (Change Mode) berfungsi sebagai alat utama untuk mengubah hak akses (permissions) sebuah file atau direktori dengan menentukan siapa yang boleh Membaca (r), Menulis/Mengubah (w), dan Mengeksekusi (x) objek tersebut, sementara chown dan chgrp berfungsi untuk menentukan kepemilikan file oleh User dan Group. Kode permission seperti rwxr-xr-- yang terlihat melalui perintah ls -l mengartikan bahwa objek tersebut adalah File Biasa (-), yang memberikan izin Penuh (Baca, Tulis, Eksekusi) kepada Pemilik (rwx), izin Baca dan Eksekusi kepada Grup (r-x), dan izin Hanya Baca kepada Lainnya (r--).**
   3. [Analisis peran chmod dan chown dalam keamanan sistem Linux]
   **Jawaban:Peran chmod dan chown dalam keamanan sistem Linux adalah fundamental karena kedua perintah tersebut bekerja sama untuk menerapkan Prinsip Hak Istimewa Paling Rendah (Principle of Least Privilege). Perintah chown (Change Owner) bertanggung jawab untuk menetapkan Kepemilikan sebuah file atau direktori kepada User dan Group tertentu, yang merupakan langkah awal dalam menentukan akuntabilitas dan membatasi siapa yang masuk kategori Pemilik, Grup, atau Lainnya. Sementara itu, perintah chmod (Change Mode) bertanggung jawab untuk mengatur Hak Akses (Baca, Tulis, Eksekusi) untuk masing-masing kategori tersebut, memastikan bahwa User dan service hanya diberikan izin minimal yang diperlukan untuk menjalankan fungsinya, sehingga secara efektif mencegah user atau program yang disusupi untuk memodifikasi atau menghapus file sensitif dan menjaga integritas sistem.**
   4.[Upload hasil dan laporan ke repositori Git sebelum deadline.]
   **Jawaban:**

## Kesimpulan
Peran Sentral chmod dan chown dalam Keamanan Linux 
**Chmod (Change Mode) dan chown (Change Owner) merupakan fondasi utama dari model keamanan file di Linux, yang secara sinergis menerapkan Prinsip Hak Istimewa Paling Rendah (Principle of Least Privilege).Peran chown (Kepemilikan dan Akuntabilitas)Perintah chown menetapkan Kepemilikan (Ownership) file (yaitu User dan Group), yang merupakan penentuan siapa yang memiliki kendali administratif dan akuntabilitas atas file tersebut. Dengan menentukan owner, sistem secara efektif membagi pengguna menjadi tiga kategori akses: Pemilik, Anggota Grup, dan Lainnya. Pemisahan ini krusial untuk mengisolasi hak istimewa; misalnya, file sistem sensitif seringkali dimiliki oleh root untuk mencegah modifikasi oleh user atau service dengan hak akses terbatas.Peran chmod (Hak Akses dan Integritas) Perintah chmod kemudian mengatur Hak Akses (Permissions)—yaitu izin Baca (r), Tulis (w), dan Eksekusi (x)—untuk ketiga kategori yang telah ditetapkan oleh chown. Fungsi utama chmod adalah untuk membatasi risiko dengan memastikan bahwa setiap user dan service hanya memiliki izin minimal yang mutlak diperlukan.-Analisis Permission (rwxr-xr--)Struktur permission, seperti rwxr-xr--, menjadi bukti konkret dari pengaturan keamanan ini. Kode tersebut mengartikan:Pemilik (rwx atau 7) memiliki izin Penuh (Baca, Tulis, Eksekusi).Grup (r-x atau 5) hanya memiliki izin Baca dan Eksekusi, dilarang memodifikasi (Tulis).Lainnya (r-- atau 4) hanya memiliki izin Baca.Kombinasi ownership dan permission ini memastikan bahwa file sensitif tidak dapat diubah (integritas terjaga) atau dijalankan (eksekusi dicegah) oleh pihak yang tidak berwenang, menjamin stabilitas dan keamanan sistem secara menyeluruh.**

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
**Jawaban:Laporan Hilang**
- Bagaimana cara Anda mengatasinya?  
**Jawaban:Mengulang**
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
