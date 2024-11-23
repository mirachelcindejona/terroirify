import json
from datetime import datetime

DATA_PUPUK = "data/data_pupuk.json"

def load_data():
    try:
        with open(DATA_PUPUK, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_data(data):
    with open(DATA_PUPUK, "w") as file:
        json.dump(data, file, indent=4)

def generate_id(data):
    pupuk_id = f"PPK0{len(data) + 1}"
    while pupuk_id in data:
        pupuk_id = f"PPK0{len(data) + 1}"
    return pupuk_id

def add_pupuk():
    data = load_data()
    
    print("\n=== Tambah Pupuk Baru ===")
    id_pupuk = generate_id(data)
    nama_pupuk = input("Nama Pupuk: ")
    stok = input("Jumlah Stok: ")
    tanggal_penerimaan = input("Tanggal Penerimaan (YYYY-MM-DD): ")
    catatan = input("Catatan Penggunaan: ")

    try:
        stok = int(stok)
        datetime.strptime(tanggal_penerimaan, "%Y-%m-%d")
    except ValueError:
        print("Error: Input tidak valid. Pastikan jumlah stok adalah angka dan tanggal dalam format yang benar.")
        return

    data[id_pupuk] = {
        "id": id_pupuk,
        "nama_pupuk": nama_pupuk,
        "stok": stok,
        "tanggal_penerimaan": tanggal_penerimaan,
        "catatan": catatan
    }
    
    save_data(data)
    print("Data pupuk berhasil ditambahkan!")

def read_pupuk():
    data = load_data()
    if data:
        print("\n=== Data Pupuk ===")
        for pupuk_id, pupuk in data.items():
            print(f"ID: {pupuk['id']}")
            print(f"Nama Pupuk: {pupuk['nama_pupuk']}")
            print(f"Stok: {pupuk['stok']}")
            print(f"Tanggal Penerimaan: {pupuk['tanggal_penerimaan']}")
            print(f"Catatan: {pupuk['catatan']}")
            print("-" * 30)
    else:
        print("Tidak ada data pupuk.")

def update_pupuk():
    data = load_data()
    id_pupuk = input("Masukkan ID pupuk yang akan diperbarui: ")
    
    if id_pupuk not in data:
        print("Pupuk dengan ID tersebut tidak ditemukan.")
        return
        
    print("\n=== Update Data Pupuk ===")
    nama_pupuk = input("Nama Pupuk: ")
    stok = input("Jumlah Stok: ")
    tanggal_penerimaan = input("Tanggal Penerimaan (YYYY-MM-DD): ")
    catatan = input("Catatan Penggunaan: ")

    try:
        stok = int(stok)
        datetime.strptime(tanggal_penerimaan, "%Y-%m-%d")
    except ValueError:
        print("Error: Input tidak valid. Pastikan jumlah stok adalah angka dan tanggal dalam format yang benar.")
        return

    data[id_pupuk] = {
        "id": id_pupuk,
        "nama_pupuk": nama_pupuk,
        "stok": stok,
        "tanggal_penerimaan": tanggal_penerimaan,
        "catatan": catatan
    }
    
    save_data(data)
    print("Data pupuk berhasil diperbarui!")

def delete_pupuk():
    data = load_data()
    id_pupuk = input("Masukkan ID pupuk yang akan dihapus: ")
    
    if id_pupuk in data:
        del data[id_pupuk]
        save_data(data)
        print("Pupuk berhasil dihapus!")
    else:
        print("Pupuk dengan ID tersebut tidak ditemukan.")

def menu_pupuk():
    from main import main_menu
    while True:
        print("\n=== Menu Pupuk ===")
        print("1. Tambah Data Pupuk")
        print("2. Lihat Data Pupuk")
        print("3. Update Data Pupuk")
        print("4. Hapus Data Pupuk")
        print("5. Kembali ke Awal")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            add_pupuk()
        elif pilihan == "2":
            read_pupuk()
        elif pilihan == "3":
            update_pupuk()
        elif pilihan == "4":
            delete_pupuk()
        elif pilihan == "5":
            main_menu()
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")
