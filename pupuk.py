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
    
    while True:
        nama_pupuk = input("Nama Pupuk: ").strip().lower()
        if not nama_pupuk:
            print("Error: Nama Pupuk tidak boleh kosong!\n")
            continue
        break
    
    while True:    
        stok = input("Jumlah Stok: ").strip()
        if not stok:
            print("Error: Jumlah Stok tidak boleh kosong!\n")
            continue
        try:
            stok = int(stok)
            if stok < 0:
                print("Error: Jumlah Stok tidak boleh negatif!\n")
                continue
            break
        except ValueError:
            print("Error: Jumlah Stok harus berupa angka!\n")

    while True:
        tanggal_penerimaan = input("Tanggal Penerimaan (YYYY-MM-DD): ").strip()
        if not tanggal_penerimaan:
            print("Error: Tanggal Penerimaan tidak boleh kosong!\n")
            continue
        else:
            try:
                datetime.strptime(tanggal_penerimaan, "%Y-%m-%d")
            except ValueError:
                print("Error: Pastikan tanggal dalam format yang benar!\n")
                continue
            break
        
    while True:    
        catatan = input("Catatan Penggunaan: ").strip().lower()
        if not catatan:
            print("Error: Catatan Penggunaan tidak boleh kosong!\n")
            continue
        break

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
        print("\n=== Data Pupuk ===\n")
        print("=" * 100)
        print(f"{'ID':<10} | {'Nama Pupuk':<20} | {'Stok':<10} | {'Tanggal Penerimaan':<20} | {'Catatan':<20}")
        print("=" * 100)
        for pupuk_id, pupuk in data.items():
            print(f"{pupuk['id']:<10} | {pupuk['nama_pupuk']:<20} | {pupuk['stok']:<10} | {pupuk['tanggal_penerimaan']:<20} | {pupuk['catatan']:<20}")
            print("-" * 100)
    else:
        print("Tidak ada data pupuk.")

def update_pupuk():
    data = load_data()
    id_pupuk = input("\nMasukkan ID pupuk yang akan diperbarui: ").strip() 
        
    if not id_pupuk:
      print("Error: ID pupuk tidak boleh kosong!\n")
      return
    if id_pupuk not in data:
        print("Pupuk dengan ID tersebut tidak ditemukan.")
        return
    
    print(f"\n=== Data pupuk saat ini dengan ID {id_pupuk} ===\n")
    print("=" * 100)
    print(f"{'ID':<10} | {'Nama Pupuk':<20} | {'Stok':<10} | {'Tanggal Penerimaan':<20} | {'Catatan':<20}")
    print("=" * 100)
    print(f"{data[id_pupuk]['id']:<10} | {data[id_pupuk]['nama_pupuk']:<20} | {data[id_pupuk]['stok']:<10} | {data[id_pupuk]['tanggal_penerimaan']:<20} | {data[id_pupuk]['catatan']:<20}")
    print("-" * 100)

    print("\n=== Update Data Pupuk ===\n(Tidak perlu diisi jika tidak ingin diubah)")
    
    nama_pupuk = input(f"Nama Pupuk [{data[id_pupuk]['nama_pupuk']}]: ").strip().lower() or data[id_pupuk]['nama_pupuk']    
    
    while True:
        stok = input(f"Jumlah Stok [{data[id_pupuk]['stok']}]: ").strip() or data[id_pupuk]['stok']
        try:
            stok = int(stok)
            if stok < 0:
                print("Error: Jumlah Stok tidak boleh negatif!\n")
                continue
            break
        except ValueError:
            print("Error: Jumlah Stok harus berupa angka!\n")
    
    while True:    
        tanggal_penerimaan = input(f"Tanggal Penerimaan (YYYY-MM-DD) [{data[id_pupuk]['tanggal_penerimaan']}]: ").strip() or data[id_pupuk]['tanggal_penerimaan']
        try:
            datetime.strptime(tanggal_penerimaan, "%Y-%m-%d")
        except ValueError:
            print("Error: Pastikan tanggal dalam format yang benar.\n")
            continue
        break
    
    catatan = input(f"Catatan Penggunaan [{data[id_pupuk]['catatan']}]: ").strip().lower() or data[id_pupuk]['catatan']


    data[id_pupuk] = {
        "id": id_pupuk,
        "nama_pupuk": nama_pupuk,
        "stok": stok,
        "tanggal_penerimaan": tanggal_penerimaan,
        "catatan": catatan
    }
    
    save_data(data)
    print("\nData pupuk berhasil diperbarui!")

def delete_pupuk():
    data = load_data()
    id_pupuk = input("\nMasukkan ID pupuk yang akan dihapus: ").strip()
    
    if not id_pupuk:
        print("Error: ID pupuk tidak boleh kosong!\n")
        return
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
        
        pilihan = input("Pilih menu: ").strip()
        
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
