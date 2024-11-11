import json
import hashlib
import os
from datetime import datetime

# Nama file untuk menyimpan data pekerja
DATA_FILE = "data/data_pekerja.json"

# Fungsi untuk memuat data dari file JSON
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}

# Fungsi untuk menyimpan data ke file JSON
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)
        
def generate_id(data):
    pekerja_id = f"00{len(data) + 1}"
    while pekerja_id in data:
        pekerja_id = f"00{len(data) + 1}"
    return pekerja_id

# Fungsi untuk menambahkan data pekerja baru (CREATE)
def tambah_pekerja():
    data = load_data()
    
    print("=== Tambah Pekerja Baru ===")
    id_pekerja = generate_id(data)
    id_pengelola = input("ID Pengelola: ")
    nama = input("Nama Lengkap: ")

    # Cek dan minta email baru hingga tidak terdaftar
    while True:
        email = input("Email: ")
        if not is_email_used(data, email):
            break
        else:
            print("Email sudah terdaftar! Gunakan email lain.")
  
    kontak = input("Kontak: ")
    status = input("Status (aktif/non-aktif): ")
    tanggal_bergabung = input("Tanggal Bergabung (YYYY-MM-DD): ")
    posisi_jabatan = input("Posisi/Jabatan: ")
    hari_kerja = input("Hari Kerja (pisahkan dengan koma, misalnya: Senin, Selasa): ").split(",")
    jam_kerja = input("Jam Kerja (format HH:MM - HH:MM): ")

    # Tambahkan pekerja baru ke data
    data[id_pekerja] = {
        "informasi_login": {"email": email},
        "profil_pekerja": {
            "id": int(id_pekerja),
            "id_pengelola": int(id_pengelola),
            "nama": nama,
            "kontak": kontak,
            "status": status,
            "tanggal_bergabung": tanggal_bergabung,
            "posisi_jabatan": posisi_jabatan
        },
        "jadwal_kerja": {
            "hari_kerja": hari_kerja,
            "jam_kerja": jam_kerja
        }
    }
    save_data(data)
    print("Pekerja baru berhasil ditambahkan!")

# Fungsi untuk menampilkan data pekerja (READ)
def read_pekerja():
    data = load_data()
    print("=== Data Semua Pekerja ===")
    for pekerja in data.values():
        print(json.dumps(pekerja, indent=4))

# Fungsi untuk memperbarui data pekerja (UPDATE)
def update_pekerja():
    data = load_data()
    id_pekerja = input("Masukkan ID pekerja yang akan diupdate: ")
    
    if id_pekerja not in data:
        print("Pekerja dengan ID tersebut tidak ditemukan.")
        return
    
    print("=== Update Data Pekerja ===")
    nama = input("Nama Lengkap: ")
    kontak = input("Kontak: ")
    status = input("Status (aktif/non-aktif): ")
    posisi_jabatan = input("Posisi/Jabatan: ")

    # Cek email baru atau gunakan email lama
    while True:
        email = input("Email (biarkan kosong untuk tidak mengubah): ")
        if email == "":  # Tidak ingin mengubah email
            email = data[id_pekerja]["informasi_login"]["email"]
            break
        elif not is_email_used(data, email) or email == data[id_pekerja]["informasi_login"]["email"]:
            # Email baru boleh dipakai atau sama dengan email lama
            break
        else:
            print("Email sudah terdaftar! Gunakan email lain.")

    hari_kerja = input("Hari Kerja (pisahkan dengan koma, misalnya: Senin,Selasa): ").split(",")
    jam_kerja = input("Jam Kerja (format HH:MM - HH:MM): ")

    # Update data pekerja
    pekerja = data[id_pekerja]
    pekerja["profil_pekerja"]["nama"] = nama
    pekerja["profil_pekerja"]["kontak"] = kontak
    pekerja["profil_pekerja"]["status"] = status
    pekerja["profil_pekerja"]["posisi_jabatan"] = posisi_jabatan
    pekerja["informasi_login"]["email"] = email
    pekerja["jadwal_kerja"]["hari_kerja"] = hari_kerja
    pekerja["jadwal_kerja"]["jam_kerja"] = jam_kerja

    save_data(data)
    print("Data pekerja berhasil diperbarui!")

# Fungsi untuk menghapus data pekerja (DELETE)
def delete_pekerja():
    data = load_data()
    id_pekerja = input("Masukkan ID pekerja yang akan dihapus: ")
    
    if id_pekerja in data:
        del data[id_pekerja]
        save_data(data)
        print("Pekerja berhasil dihapus!")
    else:
        print("Pekerja dengan ID tersebut tidak ditemukan.")

# Fungsi untuk memeriksa apakah email sudah digunakan oleh pekerja lain
def is_email_used(data, email):
    for pekerja in data.values():
        if pekerja["informasi_login"]["email"] == email:
            return True
    return False

# Menu utama
def main():
    while True:
        print("\n=== Sistem Manajemen Data Pekerja ===")
        print("1. Tambah Pekerja")
        print("2. Lihat Semua Pekerja")
        print("3. Update Data Pekerja")
        print("4. Hapus Pekerja")
        print("5. Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            tambah_pekerja()
        elif pilihan == "2":
            read_pekerja()
        elif pilihan == "3":
            update_pekerja()
        elif pilihan == "4":
            delete_pekerja()
        elif pilihan == "5":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()
