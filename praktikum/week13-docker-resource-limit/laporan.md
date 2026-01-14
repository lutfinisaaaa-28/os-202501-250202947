
# Laporan Praktikum Minggu [13]
Topik: ["Docker – Resource Limit (CPU & Memori)"]

---

## Identitas
- **Nama**  : [Lutfi Khoerunnisa]  
- **NIM**   : [250202947]  
- **Kelas** : [250202947]

---

## Tujuan
1. Menulis Dockerfile sederhana untuk sebuah aplikasi/skrip.
2. Membangun image dan menjalankan container.
3. Menjalankan container dengan pembatasan CPU dan memori.
4. Mengamati dan menjelaskan perbedaan eksekusi container dengan dan tanpa limit resource.
5. Menyusun laporan praktikum secara runtut dan sistematis.

---

## Dasar Teori
- Mekanisme Control Groups (cgroups): Docker memanfaatkan fitur kernel Linux bernama cgroups untuk mengisolasi dan membatasi penggunaan sumber daya fisik (CPU, Memori, I/O) bagi setiap kontainer agar tidak mengganggu performa server utama (host).
- Batas Memori (Hard & Soft): Pengendalian RAM dilakukan melalui Hard Limit untuk menetapkan batas maksimal penggunaan memori yang tidak boleh dilampaui, serta Soft Limit sebagai reservasi memori minimum guna menjaga stabilitas sistem saat beban kerja tinggi.
- Manajemen Kuota CPU: Docker mengatur waktu akses prosesor dengan menentukan berapa banyak siklus CPU yang boleh digunakan oleh sebuah kontainer, sehingga distribusi daya komputasi tetap adil dan mencegah terjadinya kelebihan beban (overload) pada perangkat keras.


---

## Langkah Praktikum
1. Persiapan Lingkungan
   - Pastikan Docker terpasang dan berjalan.
   - Verifikasi

   ```bash
   docker version
   docker ps
   ```
2. Membuat Aplikasi/Skrip Uji
   - Buat program sederhana di folder ```code/ ```bash(bahasa bebas) yang:
   - Melakukan komputasi berulang (untuk mengamati limit CPU), dan/atau
   - Mengalokasikan memori bertahap (untuk mengamati limit memori).
3. Membuat Dockerfile
   - Tulis ```Dockerfile``` untuk menjalankan program uji.
   - Build image:
   ```bash
   docker build -t week13-resource-limit .
   ```
4. Menjalankan Container Tanpa Limit
   - Jalankan container normal:
   ```bash
   docker run --rm week13-resource-limit
   ```
   - Catat output/hasil pengamatan.
5. Menjalankan Container Dengan Limit Resource
Jalankan container dengan batasan resource (contoh):
   ```bash
   docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
   ```
Catat perubahan perilaku program (mis. lebih lambat, error saat memori tidak cukup, dll.).
6. Monitoring Sederhana
   - Jalankan container (tanpa ```--rm``` jika perlu) dan amati penggunaan resource:
   ```bash
   docker stats
   ```
   - Ambil screenshot output eksekusi dan/atau docker stats.
7. Commit & Push
   ```bash
   git add .
   git commit -m "Minggu 13 - Docker Resource Limit"
   git push origin main
   ```
---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
docker version
docker ps
```
```bash
docker build -t week13-resource-limit .
```
```bash
docker run --rm week13-resource-limit
```
```bash
docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
```
```bash
docker stats
```
---

## Hasil Eksekusi
1. Membuat Dockerfile : 
![Screenshot hasil](screenshots/build.png)
2. Menjalankan Container Tanpa Limit
![Screenshot hasil](screenshots/tanpa%20limit%201.png)
![Screenshot hasil](screenshots/tanpa%20limit%202.png)
3. Menjalankan Container Dengan Limit
![Screenshot hasil](screenshots/dgn%20limit.png)
4. Monitoring Sederhana
![Screenshot hasil](screenshots/docker%20stats.png)

---

## Analisis
Analisis hasil praktikum menunjukkan bahwa penggunaan image Docker berbasis Python 3.11-slim berhasil menciptakan isolasi aplikasi yang efisien. Tanpa pembatasan, kontainer terdeteksi mengonsumsi memori secara terus-menerus hingga 50 MB, yang berisiko menguras sumber daya host. Namun, penerapan Resource Limit (CPU 0.5 dan RAM 256MB) terbukti efektif mengunci penggunaan sumber daya pada batas aman. Hal ini divalidasi oleh data monitoring yang menunjukkan konsumsi CPU hanya 8.00% dan RAM 32.57 MiB, sehingga stabilitas infrastruktur tetap terjaga.

---

## Kesimpulan
1. Keberhasilan Isolasi Sistem: Proses build image menggunakan Python 3.11-slim berhasil menciptakan lingkungan aplikasi yang terisolasi dan siap untuk diuji.

2. Risiko Tanpa Pembatasan: Pengujian tanpa limitasi membuktikan bahwa kontainer akan mengonsumsi memori secara terus-menerus (mencapai 50 MB), yang berisiko menguras sumber daya host jika tidak dikendalikan.

3. Efektivitas Pengendalian: Penerapan batas CPU 0.5 dan memori 256 MB terbukti efektif menjaga stabilitas sistem, dengan realisasi penggunaan CPU hanya sebesar 8.00% dan memori 32.57 MiB berdasarkan data monitoring.

---

## Quiz
1. [Mengapa container perlu dibatasi CPU dan memori?]  
   **Jawaban:** Pembatasan CPU dan memori diperlukan untuk mencegah satu kontainer menghabiskan seluruh sumber daya host (noisy neighbor effect), yang dapat menyebabkan sistem tidak stabil atau freeze. Dengan menetapkan batas (limit), administrator dapat memastikan ketersediaan sumber daya bagi layanan lain sekaligus menjalankan strategi keamanan (hardening) untuk memitigasi risiko serangan yang menguras daya komputasi infrastruktur. 
2. [Apa perbedaan VM dan container dalam konteks isolasi resource?]  
   **Jawaban:**  VM mengisolasi sumber daya pada level perangkat keras, di mana setiap VM menjalankan sistem operasi (OS) tamu lengkap di atas hypervisor, sehingga penggunaan CPU dan memori benar-benar terpisah secara fisik namun memakan overhead yang besar. Sebaliknya, kontainer melakukan isolasi pada level sistem operasi (OS) dengan berbagi kernel yang sama menggunakan fitur cgroups. Hal ini membuat kontainer jauh lebih ringan dan cepat dalam alokasi sumber daya, namun memerlukan konfigurasi manual seperti --cpus atau --memory agar satu kontainer tidak mengganggu host atau kontainer lainnya.
3. [Apa dampak limit memori terhadap aplikasi yang boros memori?]  
   **Jawaban:**  Dampak utama limit memori terhadap aplikasi yang boros memori adalah terjadinya kondisi Out Of Memory (OOM) Kill. Jika aplikasi terus melakukan alokasi memori hingga melampaui batas yang ditentukan (seperti limit 256MB pada pengujian Anda), sistem Docker akan secara otomatis menghentikan (kill) proses tersebut untuk melindungi stabilitas host. Hal ini berbeda dengan pengujian tanpa limit, di mana aplikasi dapat terus membengkak (mencapai 50 MB dan seterusnya) tanpa hambatan, yang jika dibiarkan pada aplikasi asli yang lebih berat, dapat menyebabkan seluruh server menjadi tidak responsif atau freeze.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
