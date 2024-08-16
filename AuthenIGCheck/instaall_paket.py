import os
import platform
import subprocess

def install_packages():
    # Daftar paket yang ingin diinstal
    packages = ["requests", "threading", "itertools"]
    
    # Periksa sistem operasi
    os_type = platform.system()
    
    if os_type == "Linux":
        print("Terdeteksi OS: Linux (Kali Linux)")
        try:
            # Instal pip jika belum terinstal
            subprocess.check_call(["sudo", "apt-get", "update"])
            subprocess.check_call(["sudo", "apt-get", "install", "-y", "python3-pip"])
        except subprocess.CalledProcessError:
            print("Gagal memasang pip. Harap periksa sistem Anda dan coba lagi.")
            return
    elif os_type == "Windows":
        print("Terdeteksi OS: Windows")
        try:
            # Instal pip jika belum terinstal
            subprocess.check_call(["python", "-m", "ensurepip", "--upgrade"])
        except subprocess.CalledProcessError:
            print("Gagal memasang pip. Harap periksa sistem Anda dan coba lagi.")
            return
    else:
        print("OS yang tidak didukung terdeteksi.")
        return

    # Instal paket-paket yang dibutuhkan
    for package in packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except subprocess.CalledProcessError:
            print(f"Gagal memasang {package}. Silakan periksa sistem Anda dan coba lagi.")

if __name__ == "__main__":
    install_packages()
