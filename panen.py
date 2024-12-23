import json
from datetime import datetime

DATA_PANEN = "data/data_panen.json"

def load_data():
    try:
        with open(DATA_PANEN, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_data(data):
    with open(DATA_PANEN, "w") as file:
        json.dump(data, file, indent=4)

def generate_id(data):
    panen_id = f"PNN0{len(data) + 1}"
    while panen_id in data:
        panen_id = f"PNN0{len(data) + 1}"
    return panen_id

def add_panen():
    data = load_data()
    
    print("\n=== Tambah Panen Baru ===")
    id_panen = generate_id(data)
    nama_tanaman = input("Nama Tanaman: ")
    jumlah_panen = input("Jumlah Panen (kg): ")
    tanggal_panen = input("Tanggal Panen (YYYY-MM-DD): ")
    kualitas_panen = input("Kualitas Panen: ")
    harga_per_unit = input("Harga Per Unit (Rp): ")

    try:
        jumlah_panen = float(jumlah_panen)
        harga_per_unit = float(harga_per_unit)
        datetime.strptime(tanggal_panen, "%Y-%m-%d")
    except ValueError:
        print("Error: Input tidak valid. Pastikan jumlah panen dan harga per unit adalah angka, dan tanggal dalam format yang benar.")
        return

    data[id_panen] = {
        "id": id_panen,
        "nama_tanaman": nama_tanaman,
        "jumlah_panen": jumlah_panen,
        "tanggal_panen": tanggal_panen,
        "kualitas_panen": kualitas_panen,
        "harga_per_unit": harga_per_unit
    }
    
    save_data(data)
    print("Data panen berhasil ditambahkan!")

def read_panen():
    data = load_data()
    if data:
        print("\n=== Data Panen ===")
        print(f"{'ID':<10} | {'Nama Tanaman':<20} | {'Jumlah (kg)':<15} | {'Tanggal':<15} | {'Kualitas':<15} | {'Harga (Rp)':<15}")
        print("=" * 100)
        for panen_id, panen in data.items():
            print(f"{panen['id']:<10} | {panen['nama_tanaman']:<20} | {panen['jumlah_panen']:<15} | {panen['tanggal_panen']:<15} | {panen['kualitas_panen']:<15} | Rp {panen['harga_per_unit']:,.2f}")
            print("-" * 100)
    else:
        print("Tidak ada data panen.")

def update_panen():
    data = load_data()
    id_panen = input("Masukkan ID panen yang akan diperbarui: ")
    
    if id_panen not in data:
        print("Panen dengan ID tersebut tidak ditemukan.")
        return
    
    print("\n=== Data Panen Lama ===")
    print(f"{'ID':<10} | {'Nama Tanaman':<20} | {'Jumlah (kg)':<15} | {'Tanggal':<15} | {'Kualitas':<15} | {'Harga (Rp)':<15}")
    print("=" * 100)
    print(f"{data[id_panen]['id']:<10} | {data[id_panen]['nama_tanaman']:<20} | {data[id_panen]['jumlah_panen']:<15} | {data[id_panen]['tanggal_panen']:<15} | {data[id_panen]['kualitas_panen']:<15} | Rp {data[id_panen]['harga_per_unit']:,.2f}")
    print("-" * 100)

    print("\n=== Update Data Panen ===")
    nama_tanaman = input("Nama Tanaman: ")
    jumlah_panen = input("Jumlah Panen (kg): ")
    tanggal_panen = input("Tanggal Panen (YYYY-MM-DD): ")
    kualitas_panen = input("Kualitas Panen: ")
    harga_per_unit = input("Harga Per Unit (Rp): ")

    try:
        jumlah_panen = float(jumlah_panen)
        harga_per_unit = float(harga_per_unit)
        datetime.strptime(tanggal_panen, "%Y-%m-%d")
    except ValueError:
        print("Error: Input tidak valid. Pastikan jumlah panen dan harga per unit adalah angka, dan tanggal dalam format yang benar.")
        return

    data[id_panen] = {
        "id": id_panen,
        "nama_tanaman": nama_tanaman,
        "jumlah_panen": jumlah_panen,
        "tanggal_panen": tanggal_panen,
        "kualitas_panen": kualitas_panen,
        "harga_per_unit": harga_per_unit
    }
    
    save_data(data)
    print("Data panen berhasil diperbarui!")

def delete_panen():
    data = load_data()
    id_panen = input("Masukkan ID panen yang akan dihapus: ")
    
    if id_panen in data:
        del data[id_panen]
        save_data(data)
        print("Data panen berhasil dihapus!")
    else:
        print("Panen dengan ID tersebut tidak ditemukan.")

def menu_panen():
    from main import main_menu
    while True:
        print("\n=== Menu Panen ===")
        print("1. Tambah Data Panen")
        print("2. Lihat Data Panen")
        print("3. Update Data Panen")
        print("4. Hapus Data Panen")
        print("5. Kembali ke Awal")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            add_panen()
        elif pilihan == "2":
            read_panen()
        elif pilihan == "3":
            update_panen()
        elif pilihan == "4":
            delete_panen()
        elif pilihan == "5":
            main_menu()
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")
