import json
from datetime import datetime

DATA_PEKERJA = "data/data_pekerja.json"

def load_data():
    try:
        with open(DATA_PEKERJA, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_data(data):
    with open(DATA_PEKERJA, "w") as file:
        json.dump(data, file, indent=4)

def generate_id(data):
    pekerja_id = f"PKJ0{len(data) + 1}"
    while pekerja_id in data:
        pekerja_id = f"PKJ0{len(data) + 1}"
    return pekerja_id

def get_data_login():
    try:
        with open("data/data_login.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def add_pekerja():
    data = load_data()
    user_login = get_data_login()
    
    print("\n=== Tambah Pekerja Baru ===")
    id_pekerja = generate_id(data)
    id_kebun = user_login['id_kebun']
    nama = input("Nama Lengkap: ")
    email = input("Email: ")
    kontak = input("Kontak: ")
    status = input("Status (aktif/non-aktif): ")
    tanggal_bergabung = input("Tanggal Bergabung (YYYY-MM-DD): ")
    posisi_jabatan = input("Posisi/Jabatan: ")
    hari_kerja = input("Hari Kerja (pisahkan dengan koma, misalnya: Senin, Selasa): ").split(",")
    jam_kerja = input("Jam Kerja (format HH:MM - HH:MM): ")

    try:
        datetime.strptime(tanggal_bergabung, "%Y-%m-%d")
    except ValueError:
        print("Error: Format tanggal tidak valid.")
        return

    for pekerja in data.values():
        if pekerja['email'] == email:
            print("Email sudah terdaftar! Gunakan email lain.")
            return

    data[id_pekerja] = {
        "id_pekerja": id_pekerja,
        "id_kebun": id_kebun,
        "nama": nama,
        "email": email,
        "kontak": kontak,
        "status": status,
        "tanggal_bergabung": tanggal_bergabung,
        "posisi_jabatan": posisi_jabatan,
        "hari_kerja": hari_kerja,
        "jam_kerja": jam_kerja
    }
    
    save_data(data)
    print("Data pekerja berhasil ditambahkan!")

def read_pekerja():
    data = load_data()
    user_login = get_data_login()
    if data:
        print("\n=== Data Pekerja ===")
        print("-" * 100)
        print(f"{'ID':<10} | {'Lokasi Kebun':<20} | {'Nama':<20} | {'Email':<20} | {'Kontak':<20} | {'Status':<20} | {'Tanggal Bergabung':<20} | {'Posisi/Jabatan':<20} | {'Hari Kerja':<20} | {'Jam Kerja':<20}")
        print("-" * 100)
        for pekerja_id, pekerja in data.items():
            if pekerja['id_kebun'] == user_login['id_kebun']:
                print(f"{pekerja['id_pekerja']:<10} | {user_login['alamat_kebun']:<20} | {pekerja['nama']:<20} | {pekerja['email']:<20} | {pekerja['kontak']:<20} | {pekerja['status']:<20} | {pekerja['tanggal_bergabung']:<20} | {pekerja['posisi_jabatan']:<20} | {', '.join(pekerja['hari_kerja']):<20} | {pekerja['jam_kerja']:<20}")
                print("-" * 100)
    else:
        print("Tidak ada data pekerja.")

def update_pekerja():
    data = load_data()
    user_login = get_data_login()
        
    id_pekerja = input("Masukkan ID pekerja yang akan diperbarui: ")
    
    if id_pekerja not in data:
        print("Pekerja dengan ID tersebut tidak ditemukan.")
        return
        
    if data[id_pekerja]['id_kebun'] != user_login['id_kebun']:
        print("Anda tidak memiliki akses untuk mengubah data pekerja ini!")
        return
    
    print("\n=== Data Pekerja Lama ===")
    print("=" * 100)
    print(f"{'ID':<10} | {'Lokasi Kebun':<20} | {'Nama':<20} | {'Email':<20} | {'Kontak':<20} | {'Status':<20} | {'Tanggal Bergabung':<20} | {'Posisi/Jabatan':<20} | {'Hari Kerja':<20} | {'Jam Kerja':<20}")
    print("=" * 100)
    print(f"{data[id_pekerja]['id_pekerja']:<10} | {user_login['alamat_kebun']:<20} | {data[id_pekerja]['nama']:<20} | {data[id_pekerja]['email']:<20} | {data[id_pekerja]['kontak']:<20} | {data[id_pekerja]['status']:<20} | {data[id_pekerja]['tanggal_bergabung']:<20} | {data[id_pekerja]['posisi_jabatan']:<20} | {', '.join(data[id_pekerja]['hari_kerja']):<20} | {data[id_pekerja]['jam_kerja']:<20}")
    print("-" * 100)

    print("\n=== Update Data Pekerja ===")
    nama = input("Nama Lengkap: ")
    email = input("Email: ")
    kontak = input("Kontak: ")
    status = input("Status (aktif/non-aktif): ")
    tanggal_bergabung = input("Tanggal Bergabung (YYYY-MM-DD): ")
    posisi_jabatan = input("Posisi/Jabatan: ")
    hari_kerja = input("Hari Kerja (pisahkan dengan koma): ").split(",")
    jam_kerja = input("Jam Kerja (format HH:MM - HH:MM): ")

    try:
        datetime.strptime(tanggal_bergabung, "%Y-%m-%d")
    except ValueError:
        print("Error: Format tanggal tidak valid.")
        return

    for pid, pekerja in data.items():
        if pekerja['email'] == email and pid != id_pekerja:
            print("Email sudah terdaftar! Gunakan email lain.")
            return

    data[id_pekerja].update({
        "nama": nama,
        "email": email,
        "kontak": kontak,
        "status": status,
        "tanggal_bergabung": tanggal_bergabung,
        "posisi_jabatan": posisi_jabatan,
        "hari_kerja": hari_kerja,
        "jam_kerja": jam_kerja
    })
    
    save_data(data)
    print("Data pekerja berhasil diperbarui!")

def delete_pekerja():
    data = load_data()
    user_login = get_data_login()
        
    id_pekerja = input("Masukkan ID pekerja yang akan dihapus: ")
    
    if id_pekerja not in data:
        print("Pekerja dengan ID tersebut tidak ditemukan.")
        return
        
    if data[id_pekerja]['id_kebun'] != user_login['id_kebun']:
        print("Anda tidak memiliki akses untuk menghapus data pekerja ini!")
        return
    
    konfirmasi = input(f"Anda yakin ingin menghapus pekerja {data[id_pekerja]['nama']}? (y/n): ")
    if konfirmasi.lower() == 'y':
        del data[id_pekerja]
        save_data(data)
        print("Pekerja berhasil dihapus!")
    else:
        print("Penghapusan dibatalkan.")

def menu_pekerja():
    from main import main_menu
    while True:
        print("\n=== Menu Pekerja ===")
        print("1. Tambah Data Pekerja")
        print("2. Lihat Data Pekerja")
        print("3. Update Data Pekerja")
        print("4. Hapus Data Pekerja")
        print("5. Kembali ke Awal")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            add_pekerja()
        elif pilihan == "2":
            read_pekerja()
        elif pilihan == "3":
            update_pekerja()
        elif pilihan == "4":
            delete_pekerja()
        elif pilihan == "5":
            main_menu()
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")
