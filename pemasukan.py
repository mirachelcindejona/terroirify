import json
from datetime import datetime
from panen import load_data as load_data_panen
from tanaman import load_data as load_data_tanaman

DATA_PEMASUKAN = "data/data_pemasukan.json"

def load_data():
    try:
        with open(DATA_PEMASUKAN, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_data(data):
    with open(DATA_PEMASUKAN, "w") as file:
        json.dump(data, file, indent=4)

def generate_id(data):
    pemasukan_id = f"PMSK0{len(data) + 1}"
    while pemasukan_id in data:
        pemasukan_id = f"PMSK0{len(data) + 1}"
    return pemasukan_id

def add_pemasukan():
    data = load_data()

    print("\n=== Tambah Data Pemasukan ===")
    id_pemasukan = generate_id(data)

    # Memuat data panen untuk pilihan
    data_panen = load_data_panen()
    if not data_panen:
        print("Tidak ada data panen tersedia.")
        return
    
    data_tanaman = load_data_tanaman()
    if not data_tanaman:
        print("Tidak ada data tanaman tersedia.")
        return
    
    print("Pilih data panen yang ingin ditambah ke pemasukkan:")
    for panen_id, panen in data_panen.items():
        print(f"{panen_id}: {data_tanaman[panen['id_tanaman']]['nama_tanaman']}")
    
    nama_panen_id = input("Masukkan ID panen yang ingin ditambah ke pemasukkan: ")
    if nama_panen_id not in data_panen:
        print("ID panen tidak valid.")
    
    jumlah_penjualan = input("Masukkan jumlah penjualan: ")
    tanggal_penerimaan = input("Tanggal Penerimaan (YYYY-MM-DD): ")
    id_panen = input("Masukkan ID Panen: ")

    try:
        jumlah_penjualan = float(jumlah_penjualan)
        datetime.strptime(tanggal_penerimaan, "%Y-%m-%d")
    except ValueError:
        print("Error: Input tidak valid. Pastikan jumlah stok adalah angka dan tanggal dalam format yang benar.")
        return
    
    data[id_pemasukan] = {
        "id": id_pemasukan,
        "id_panen": nama_panen_id,
        "jumlah_penjualan": jumlah_penjualan,
        "tanggal_penerimaan": tanggal_penerimaan,
        "id_panen": id_panen
    }

    save_data(data)
    print("Data pemasukan berhasil ditambahkan!")

def read_pemasukan():
    data = load_data()
    if data:
        print("\n=== Data Pemasukan ===")
        print("=" * 60)
        print(f"{'ID':<10} | {'Jumlah Penjualan':<20} | {'Tanggal Penerimaan':<20} | {'ID Panen':<10}")
        print("=" * 60)
        for pemasukan_id, pemasukan in data.items():
            print(f"{pemasukan['id']:<10} | {pemasukan['jumlah_penjualan']:<20} | {pemasukan['tanggal_penerimaan']:<20} | {pemasukan['id_panen']:<10}")
        print("-" * 60)
    else:
        print("Tidak ada data pemasukan.")

def update_pupuk():
    data = load_data()
    id_pemasukan = input("Masukkan Id Pemasukan yang akan diperbarui: ")

    if id_pemasukan not in data:
        print("Pemasukan dengan ID tersebut tidak ditemukan.")
        return
    
    print("\n=== Data Pemasukan ===")
    print("=" * 100)
    print(f"{'ID':<10} | {'Jumlah Penjualan':<20} | {'Tanggal Penerimaan':<20} | {'ID Panen':<10}")
    print("=" * 100)
    print(f"{data[id_pemasukan]['id']:<10} | {data[id_pemasukan]['jumlah_penjualan']:<20} | {data[id_pemasukan]['tanggal_penerimaan']:<20} | {data[id_pemasukan]['id_panen']:<10}")
    print("-" * 100)
    
    print("\n=== Update Data Pemasukan ===")

    # Memuat data panen untuk pilihan
    data_panen = load_data_panen()
    if not data_panen:
        print("Tidak ada data panen tersedia.")
        return
    
    data_tanaman = load_data_tanaman()
    if not data_tanaman:
        print("Tidak ada data tanaman tersedia.")
        return
    
    print("Pilih data panen yang ingin diperbarui ke pemasukkan:")
    for panen_id, panen in data_panen.items():
        print(f"{panen_id}: {data_tanaman[panen['id_tanaman']]['nama_tanaman']}")
    
    nama_panen_id = input("Masukkan ID panen yang ingin diperbarui ke pemasukkan: ")
    if nama_panen_id not in data_panen:
        print("ID panen tidak valid.")
    
    jumlah_penjualan = input("Masukkan jumlah penjualan: ")
    tanggal_penerimaan = input("Tanggal Penerimaan (YYYY-MM-DD): ")
    id_panen = input("Masukkan ID Panen: ")

    try:
        jumlah_penjualan = float(jumlah_penjualan)
        datetime.strptime(tanggal_penerimaan, "%Y-%m-%d")
    except ValueError:
        print("Error: Input tidak valid. Pastikan jumlah stok adalah angka dan tanggal dalam format yang benar.")
        return
    
    data[id_pemasukan] = {
        "id": id_pemasukan,
        "jumlah_penjualan": jumlah_penjualan,
        "tanggal_penerimaan": tanggal_penerimaan,
        "id_panen": id_panen
    }

    save_data(data)
    print("Data Pemasukan berhasil diperbarui!")

def delete_pemasukan():
    data = load_data()
    id_pemasukan = input("Masukkan ID Pemasukan yang akan dihapus: ")

    if id_pemasukan in data:
        del data[id_pemasukan]
        save_data(data)
        print("Pemasukan berhasil dihapus!")
    else:
        print("Pemasukan dengan ID tersebut tidak ditemukan.")

def menu_pemasukan():
    from main import main_menu
    while True:
        print("\n=== Menu Pemasukan ===")
        print("1. Tambah Data Pemasukan")
        print("2. Lihat Data Pemasukan")
        print("3. Update Data Pemasukan")
        print("4. Hapus Data Pemasukan")
        print("5. Kembali ke Awal")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            add_pemasukan()
        elif pilihan == "2":
            read_pemasukan()
        elif pilihan == "3":
            update_pupuk()
        elif pilihan == "4":
            delete_pemasukan()
        elif pilihan == "5":
            main_menu()
        else:
            print("Pilihan tidak valid. Silahkan pilih lagi.")