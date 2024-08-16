# Insta-Checker

## Deskripsi

Pemeriksa Akun Instagram yang akan memeriksa nama pengguna/email:kata sandi untuk melihat apakah kredensial akun sudah benar. Kemudian, ia akan menuliskan nama pengguna:kata sandi yang berhasil ke dalam berkas bernama Accounts.txt.

# Catatan

Proxy wajib digunakan karena Instagram akan memblokir Anda jika tidak, jadi program ini tidak akan berguna tanpanya.

## Proxy
### Proxy harus diformat IP:Port dan harus HTTPS. HASIL yang lambat semata-mata didasarkan pada kecepatan proxy karena multithreading berarti program dapat memeriksa respons segera setelah respons diterima.

*Jika Eror*
```bash
"requests.exceptions.ProxyError: HTTPSConnectionPool(host='www.instagram.com', port=443): Max retries exceeded with url: /accounts/login/ajax/ (Disebabkan oleh ProxyError('Tidak dapat terhubung ke proxy.', OSError('Koneksi Tunnel gagal: 403 Dilarang')))
"
```
 muncul. Kesalahan ini berarti tidak ada cukup proxy dan Instagram telah memasukkan proxy tertentu ke dalam daftar hitam karena penggunaan yang berlebihan atau proxy tersebut bersifat publik dan oleh karena itu orang lain telah menggunakannya dan Instagram telah memblokirnya karena penggunaan mereka. Program akan memilih proxy secara acak. Daftar proxy yang besar (GB) akan menyebabkan program berjalan lambat.

**Proxy yang dirotasi direkomendasikan!**
### proxy yang direkomendasikan 500-1000
### proxy maks: 10k

### Penyedia proxy murah terbaik + proxy gratis: https://bit.ly/2DPFwHI

## Instalasi
Linux + Windows:

*cloning repository*
``` bash
git clone https://github.com/Yoga913/AuthenIGCheck.git
```
*masuk Kedirektory*
```bash
cd AuthenIGCheck
```

*meninstall paket*
```bash
python3 install_packages.py
```
*menjalankan*
```bash
python3 AuthenIGCheck.py
```

*Noted*:yang membedakan cara menjalankan di kali linux dan windows hanyalah cara penulisan `python3` dan `python`

# Penafian
PERANGKAT LUNAK INI HANYA UNTUK PENGGUNAAN PENDIDIKAN DAN PENELITIAN. SAYA TIDAK BERTANGGUNG JAWAB ATAS PENGGUNAAN PERANGKAT LUNAK INI YANG BERBAHAYA ATAU PENGGUNAAN KODE SUMBER YANG BERBAHAYA
