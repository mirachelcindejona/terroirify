import json
from datetime import datetime

DATA_PENGELUARAN = "data/data_pengeluaran.json"

def load_data():
    try:
        with open(DATA_PENGELUARAN, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    
def save_data(data):
    with open(DATA_PENGELUARAN, "w") as file:
        json.dump(data, file, indent=4)
        
def generate_id(data):
    pengeluaran_id = f"PLRN{len(data) + 1}"
    while pengeluaran_id in data:
       pengeluaran_id = f"PLRN{len(data) + 1}"
    return pengeluaran_id

def add_pengeluaran():
    data = load_data()
    
    print ("\n=== Tambah Data Pengeluaran ===")
    id_pengeluaran = generate_id(data) 
    pengeluaran_operasional = input("Masukkan jumlah pengeluaran: ")
    nama_pengeluaran = input("Masukkan nama pengeluaran: ")
    tanggal_pengeluaran = input("Tanggal Pengeluaran (YYYY-MM-DD): ")
    kategori_pengeluaran = input("Masukkan kategori pengeluaran (Biaya pupuk atau Biaya tenaga kerja): ")
    
    try:
        pengeluaran_operasional = float(pengeluaran_operasional)
        datetime.strptime(tanggal_pengeluaran, "%Y-%m-%d")
    except ValueError:
        print("Error: Input tidak valid. Pastikan pengeluaran operasional adlah angka dan tanggal pengeluaran dalam format yang benar! ")
        return

    data[id_pengeluaran] = {
        "id": id_pengeluaran, 
        "pengeluaran_operasional": pengeluaran_operasional,
        "tanggal_pengeluaran": tanggal_pengeluaran,
        "kategori_pengeluaran": kategori_pengeluaran,
        "nama_pengeluaran": nama_pengeluaran
    }

    save_data(data)
    print("Data pengeluaran berhasil ditambahkan!")

def read_pengeluara():
    data = load_data()
    if data:
        print (("\n=== Data Pengeluaran"))
        for pengeluaran_id, pengeluaran in data.items():
            print(f"ID: {pengeluaran["id"]}")
            print(f"Pengeluaran operasional: {pengeluaran["pengeluaran_operasional"]}")
            print(f"Nama pengeluaran:{pengeluaran["nama_pengeluaran"]}")
            print(f"Tanggal pengeluaran: {pengeluaran["tanggal_pengeluaran"]}")  
            print(f"Kategori pengeluaran: {pengeluaran["kategori_pengeluaran"]}")
            print("-" * 30)
    else:
        print("Tidak ada data pengeluaran.")

def update_pengeluaran():
    data = load_data()
    id_pengeluaran = input("Masukkan ID pengeluaran yang akan diperbarui: ")

    if id_pengeluaran not in data:
        print("pupuk dengan ID tersebut tidak ditemukan.")
        return
    
    print("\n=== Update Data Pengeluaran ===")
    pengeluaran_operasional = input("Masukkan jumlah pengeluaran: ")
    nama_pengeluaran = input("Nama Pengeluaran: ")
    tanggal_pengeluaran= input("Tanggal Pengeluaran (YYYY-MM-DD):")
    kategori_pengeluaran = input("Masukkan kategori pengeluaran (Biaya pupuk atau Biaya tenaga kerja): ")  

    try:
        pengeluaran_operasional = int(pengeluaran_operasional)
        datetime.strptime(tanggal_pengeluaran, "%Y-%m-%d")
    except ValueError:
        print("Error: Input tidak valid. Pastikan jumlah stok adalah angka dan tanggal dalam format yang benar.")
        return
    
    data[id_pengeluaran] = {
        "id": id_pengeluaran, 
        "pengeluaran_operasional": pengeluaran_operasional,
        "tanggal_pengeluaran": tanggal_pengeluaran,
        "kategori_pengeluaran": kategori_pengeluaran,
        "nama_pengeluaran": nama_pengeluaran
    }

    save_data(data)
    print("Data pengeluaran berhasil diperbarui!")

def delete_pengeluaran():
    data = load_data()
    id_pengeluaran = input("Masukkan ID pengeluaran yang akan dihapus: ")

    if id_pengeluaran in data:
        del data[id_pengeluaran]
        save_data(data)
        print("Pengeluaran berhasil dihapus!")
    else:
        print("Pengeluaran dengan ID tersebut tidak ditemukan.")

def menu_pengeluaran():
    from main import main_menu
    while True:
        print("\n=== Menu Pupuk ===")
        print("1. Tambah pengeluaran")
        print("2. Lihat Semua data pengeluaran")
        print("3. Update Data pengeluaran")
        print("4. Hapus pengeluaran")
        print("5. Kembali ke Awal")

        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            add_pengeluaran()
        elif pilihan == "2":
            read_pengeluara()
        elif pilihan == "3":
            update_pengeluaran()
        elif pilihan == "4":
            delete_pengeluaran()
        elif pilihan == "5":
            main_menu()
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")