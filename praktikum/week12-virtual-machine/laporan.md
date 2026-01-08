
# Laporan Praktikum Minggu [12]
Topik: ["Virtualisasi Menggunakan Virtual Machine"]

---

## Identitas
- **Nama**  : [Lutfi Khoerunnisa],  [Aster Rifani] , [Ani Ngismatul Hawa]
- **NIM**   : [250202947]  , [250202915] , [250202914]
- **Kelas** : [1IKRB]

---

## Tujuan
1. Menginstal perangkat lunak virtualisasi (VirtualBox/VMware).
2. Membuat dan menjalankan sistem operasi guest di dalam VM.
3. Mengatur konfigurasi resource VM (CPU, RAM, storage).
4. Menjelaskan mekanisme proteksi OS melalui virtualisasi.
5. Menyusun laporan praktikum instalasi dan konfigurasi VM secara sistematis.

---

## Dasar Teori
Virtualisasi adalah teknologi yang mengabstraksi perangkat keras fisik menjadi beberapa sumber daya virtual. Hal ini memungkinkan satu komputer fisik menjalankan berbagai sistem operasi secara bersamaan tanpa saling mengganggu, yang berfungsi sebagai metode pengujian yang aman dan efisien.

Arsitekturnya terdiri dari Host OS (sistem utama), Guest OS (sistem virtual), dan Hypervisor. Hypervisor seperti VirtualBox bertindak sebagai pengelola alokasi sumber daya (CPU, RAM, storage) agar Guest OS dapat beroperasi secara mandiri di atas Host OS.

Konfigurasi sumber daya yang tepat sangat krusial untuk menjaga keseimbangan kinerja sistem. Melalui mekanisme isolasi, virtualisasi bertindak sebagai "benteng pertahanan" yang memastikan bahwa gangguan atau ancaman di dalam sistem virtual tidak akan menyebar ke sistem fisik utama.

---

## Langkah Praktikum
1. Instalasi Virtual Machine
Instal VirtualBox atau VMware pada komputer host.
Pastikan fitur virtualisasi (VT-x / AMD-V) aktif di BIOS.
2. Pembuatan OS Guest
   - Buat VM baru dan pilih OS guest (misal: Ubuntu Linux).
      - Atur resource awal:
      - CPU: 1–2 core
      - RAM: 2–4 GB
      - Storage: ≥ 20 GB
3. Instalasi Sistem Operasi
   - Jalankan proses instalasi OS guest sampai selesai.
   - Pastikan OS guest dapat login dan berjalan normal.
4. Konfigurasi Resource
   - Ubah konfigurasi CPU dan RAM.
   - Amati perbedaan performa sebelum dan sesudah perubahan resource.
5. Analisis Proteksi OS
   - Jelaskan bagaimana VM menyediakan isolasi antara host dan guest.
   - Kaitkan dengan konsep sandboxing dan hardening OS.
6. Dokumentasi
   - Ambil screenshot setiap tahap penting.
   - Simpan di folder screenshots/.
7. Commit & Push
   ```
   git add .
   git commit -m "Minggu 12 - Virtual Machine"
   git push origin main
   ```

---

## Kode / Perintah
```bash
praktikum/week12-virtual-machine/
├─ code/
│  └─ catatan_konfigurasi.txt (opsional)
├─ screenshots/
│  ├─ instalasi_vm.png
│  ├─ konfigurasi_resource.png
│  └─ os_guest_running.png
└─ laporan.md
```

---

## Hasil Eksekusi

1. Persiapan instalasi proses menginstal oracle virtual box untuk persiapan dalam pembuatan virtual/machine
![Screenshot hasil](./screenshots/instalasi_VM.png.png)
2. Konfigurasi dan instalasi VM proses pembuatan mesin virtual menggunakan fitur unattended install di virtual box untuk otomatisasi instalasi Ubuntu.
![Screenshot hasil](./screenshots/konfigurasi_resource.png.jpeg)
3. Eksperimen VM linux ubuntu 24.pengecekan menggunakan perintah uname-a (cek kernel) & free -h (cek ram).Terlihat total RAm 2.8Gi (3GB).Pengujian beban kerja dengan membuka tab Firefox (Youtube dan E-learning).
 -  Hasil : Ram terpakai mencapai 90.5% (3.1 GB).
 - Kondisi : Sistem berjalan responsif dan lancar meskipun pengguna memori hampir habis.
 ![Screenshot hasil](./screenshots/os_guest_running.png.png)
 
4. Setelah proses mengurangi Resource,kemudian membuka lagi VM dan membuka system manager,terlihat belum menjalankan aplikasi lain sudah memakai RAM 2,1 GB (97,7%).
![Screenshot hasil](./screenshots/RAM_2.jpeg)

5. Saat menggunakan RAM 3GB,membuka 5 tab berjalan lancar meski RAM terpakai 90%.Namun saat RAM diturunkan menjadi 2 GB diturunkan menjadi 2GB,sistem menjadi sangat lambat (lag)dan Firefox sering not responding karena kehabisan memori.
![Screenshot hasil](./screenshots/FIREFOX.PNG.jpeg)

---

## Analisis
- Isolasi VM Isolasi VM bekerja dengan menciptakan batasan digital yang tegas melalui hypervisor sehingga Guest OS (Ubuntu) tidak memiliki akses langsung ke perangkat keras fisik maupun memori milik Host OS. Hal ini terlihat pada konfigurasi Virtual Hardware yang Anda buat, di mana sistem tamu hanya diizinkan menggunakan jatah spesifik (seperti 2 CPU dan 4000 MB RAM), sehingga segala aktivitas atau kegagalan fungsi di dalam VM tidak akan mengganggu stabilitas sistem utama.
- Konsep isolasi dalam VM bekerja dengan menciptakan batasan digital melalui hypervisor agar Guest OS (Ubuntu) hanya menggunakan sumber daya virtual yang ditentukan, sehingga aktivitasnya tidak dapat mengakses atau merusak Host OS. Hal ini secara otomatis menerapkan prinsip sandboxing, di mana segala bentuk kegagalan aplikasi (seperti Firefox yang not responding) atau serangan malware terperangkap dalam "kotak pasir" virtual tanpa mengganggu stabilitas sistem utama. Melalui pembatasan alokasi sumber daya dan penggunaan VM sebagai lingkungan terisolasi, praktikum ini juga menjalankan strategi hardening OS dengan memperkecil permukaan serangan dan melindungi integritas sistem fisik dari risiko yang muncul selama pengujian.

---

## Kesimpulan
1. Efisiensi Sumber Daya dan Isolasi: Virtualisasi memungkinkan satu perangkat keras fisik menjalankan beberapa sistem operasi (Guest OS) secara bersamaan melalui pembagian sumber daya (CPU, RAM, storage) yang dikelola oleh Hypervisor. Mekanisme ini menciptakan isolasi yang kuat, di mana aktivitas atau kegagalan pada sistem tamu tidak akan mengganggu stabilitas sistem utama (Host OS).

2. Keamanan sebagai Benteng Pertahanan: Praktikum ini membuktikan bahwa Virtual Machine berfungsi sebagai lingkungan aman (sandboxing) untuk pengujian. Dengan isolasi sistem, ancaman digital seperti malware dapat dikurung di dalam lingkungan virtual, sehingga melindungi infrastruktur fisik dan integritas data pada sistem inang.

---

## Quiz
1. [Apa perbedaan antara host OS dan guest OS?]  
   **Jawaban** : Instalasi dan Kontrol Host OS adalah sistem utama yang terpasang langsung pada perangkat keras fisik dan memegang kendali penuh atas mesin. Sementara Guest OS adalah sistem virtual yang berjalan di dalam Host OS melalui perantara hypervisor.Pengelolaan Sumber Daya: Host OS bertindak sebagai penyedia dan pengelola sumber daya (CPU, RAM, storage). Guest OS hanya menggunakan jatah sumber daya virtual yang dialokasikan kepadanya dan tidak bisa mengakses perangkat keras secara langsung.Isolasi dan Keamanan: Host OS mengelola stabilitas seluruh sistem. Guest OS bersifat terisolasi; jika sistem tamu ini mengalami gangguan atau terkena virus, dampaknya tidak akan menyebar atau merusak sistem fisik utama (Host OS).
2. [Apa peran hypervisor dalam virtualisasi?]  
   **Jawaban**  :  Hypervisor berperan sebagai pengelola utama yang menjembatani perangkat keras fisik dengan berbagai sistem operasi virtual. Tugas intinya adalah membagi dan mendistribusikan sumber daya seperti CPU, RAM, dan penyimpanan dari Host OS kepada beberapa Guest OS agar dapat berjalan secara bersamaan secara efisien.
   Selain mengelola sumber daya, hypervisor berfungsi sebagai penjamin keamanan melalui mekanisme isolasi. Ia memastikan setiap mesin virtual berjalan di lingkungannya masing-masing, sehingga jika terjadi crash atau infeksi malware pada satu sistem tamu, hal tersebut tidak akan memengaruhi stabilitas sistem utama maupun mesin virtual lainnya.
3. [Mengapa virtualisasi meningkatkan keamanan sistem?]  
   **Jawaban**  : Virtualisasi meningkatkan keamanan melalui isolasi sistem, di mana setiap mesin virtual (VM) bekerja dalam lingkungan tertutup. Jika satu sistem terkena virus atau malware, ancaman tersebut akan terkurung di dalam VM dan tidak dapat menyebar ke sistem utama (Host OS) maupun perangkat keras fisik.
   Selain itu, fitur snapshot memungkinkan pemulihan instan ke kondisi aman jika terjadi kegagalan. Dengan metode ini, pengujian aplikasi berbahaya dapat dilakukan tanpa risiko, karena sistem fisik tetap terlindungi di balik lapisan virtualisasi yang bertindak sebagai benteng pertahanan.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
Pusing 7 keliling
- Bagaimana cara Anda mengatasinya?  
Paramex Obatnya
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
