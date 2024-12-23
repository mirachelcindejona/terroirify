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
    kategori_pengeluaran = input("Masukkan kategori pengeluaran: ")
    jumlah_pengeluaran = input("Masukkan jumlah pengeluaran: ")
    tanggal_pengeluaran = input("Tanggal Pengeluaran (YYYY-MM-DD): ")
    keterangan = input("Masukkan keterangan pengeluaran: ")
    
    try:
        jumlah_pengeluaran = float(jumlah_pengeluaran)
        datetime.strptime(tanggal_pengeluaran, "%Y-%m-%d")
    except ValueError:
        print("Error: Input tidak valid. Pastikan pengeluaran operasional adlah angka dan tanggal pengeluaran dalam format yang benar! ")
        return

    data[id_pengeluaran] = {
        "id": id_pengeluaran, 
        "jumlah_pengeluaran": jumlah_pengeluaran,
        "tanggal_pengeluaran": tanggal_pengeluaran,
        "kategori_pengeluaran": kategori_pengeluaran,
        "keterangan": keterangan
    }

    save_data(data)
    print("Data pengeluaran berhasil ditambahkan!")

def read_pengeluara():
    data = load_data()
    if data:
        print("\n=== Data Pengeluaran ===")
        print(f"{'ID':<10} {'Jumlah Pengeluaran':<20} {'Keterangan':<30} {'Tanggal Pengeluaran':<20} {'Kategori':<20}")
        print("=" * 100)
        for pengeluaran_id, pengeluaran in data.items():
            print(f"{pengeluaran['id']:<10} {pengeluaran['jumlah_pengeluaran']:<20} {pengeluaran['keterangan']:<30} {pengeluaran['tanggal_pengeluaran']:<20} {pengeluaran['kategori_pengeluaran']:<20}")
            print("-" * 100)
    else:
        print("Tidak ada data pengeluaran.")

def update_pengeluaran():
    data = load_data()
    id_pengeluaran = input("Masukkan ID pengeluaran yang akan diperbarui: ")

    if id_pengeluaran not in data:
        print("pupuk dengan ID tersebut tidak ditemukan.")
        return
    
    print("\n=== Update Data Pengeluaran ===")
    jumlah_pengeluaran = input("Masukkan jumlah pengeluaran: ")
    keterangan = input("Keterangan Pengeluaran: ")
    tanggal_pengeluaran= input("Tanggal Pengeluaran (YYYY-MM-DD):")
    kategori_pengeluaran = input("Masukkan kategori pengeluaran (Biaya pupuk atau Biaya tenaga kerja): ")  

    try:
        jumlah_pengeluaran = int(jumlah_pengeluaran)
        datetime.strptime(tanggal_pengeluaran, "%Y-%m-%d")
    except ValueError:
        print("Error: Input tidak valid. Pastikan jumlah stok adalah angka dan tanggal dalam format yang benar.")
        return
    
    data[id_pengeluaran] = {
        "id": id_pengeluaran, 
        "jumlah_pengeluaran": jumlah_pengeluaran,
        "tanggal_pengeluaran": tanggal_pengeluaran,
        "kategori_pengeluaran": kategori_pengeluaran,
        "keterangan": keterangan
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
        print("\n=== Menu Pengeluaran ===")
        print("1. Tambah Data Pengeluaran")
        print("2. Lihat Data Pengeluaran")
        print("3. Update Data Pengeluaran")
        print("4. Hapus Data Pengeluaran")
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