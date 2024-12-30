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

    while True:
        kategori_pengeluaran = input("Masukkan kategori pengeluaran (Biaya pupuk atau Biaya tenaga kerja): ").strip().lower()
        if not kategori_pengeluaran:
            print("Error: Kategori pengeluaran tidak boleh kosong!\n")
            continue
        break
    
    while True:    
        jumlah_pengeluaran = input("Masukkan jumlah pengeluaran: ").strip()
        if not jumlah_pengeluaran:
            print("Error: Jumlah pengeluaran tidak boleh kosong!\n")
            continue
        try:
            jumlah_pengeluaran = float(jumlah_pengeluaran)
            if jumlah_pengeluaran <= 0:
                print("Error: Jumlah pengeluaran harus lebih besar dari 0!\n")
                continue
            break
        except ValueError:
            print("Error: Jumlah pengeluaran harus berupa angka!\n")
    
    while True:
        tanggal_pengeluaran = input("Tanggal Pengeluaran (YYYY-MM-DD): ").strip()
        if not tanggal_pengeluaran:
            print("Error: Tanggal pengeluaran tidak boleh kosong!\n")
            continue
        try:
            datetime.strptime(tanggal_pengeluaran, "%Y-%m-%d")
        except ValueError:
                print("Error: Pastikan tanggal pengeluaran dalam format yang benar!\n")
                continue
        break
        
    while True:
        keterangan = input("Masukkan keterangan pengeluaran: ").strip().lower()
        if not keterangan:
            print("Error: Keterangan pengeluaran tidak boleh kosong!\n")
            continue
        break

    data[id_pengeluaran] = {
        "id": id_pengeluaran, 
        "jumlah_pengeluaran": jumlah_pengeluaran,
        "tanggal_pengeluaran": tanggal_pengeluaran,
        "kategori_pengeluaran": kategori_pengeluaran,
        "keterangan": keterangan
        }

    save_data(data)
    print("Data pengeluaran berhasil ditambahkan!")

def read_pengeluaran():
    data = load_data()
    if data:
        print("\n=== Data Pengeluaran ===\n")
        print("=" * 100)
        print(f"{'ID':<10} | {'Jumlah Pengeluaran':<20} | {'Keterangan':<30} | {'Tanggal Pengeluaran':<20} | {'Kategori':<20}")
        print("=" * 100)
        for pengeluaran_id, pengeluaran in data.items():
                print(f"{pengeluaran['id']:<10} | {pengeluaran['jumlah_pengeluaran']:<20} | {pengeluaran['keterangan']:<30} | {pengeluaran['tanggal_pengeluaran']:<20} | {pengeluaran['kategori_pengeluaran']:<20}")
                print("-" * 100)
    else:
        print("Tidak ada data pengeluaran.")

def update_pengeluaran():
    data = load_data()
    id_pengeluaran = input("\nMasukkan ID pengeluaran yang akan diperbarui: ").strip()

    if not id_pengeluaran:
      print("Error: ID pengeluaran tidak boleh kosong!\n")
      return
    if id_pengeluaran not in data:
        print("Pengeluaran dengan ID tersebut tidak ditemukan.")
        return
    
    print(f"\n=== Data pengeluaran saat ini dengan ID {id_pengeluaran} ===\n")
    print("=" * 100)
    print(f"{'ID':<10} | {'Jumlah Pengeluaran':<20} | {'Keterangan':<30} | {'Tanggal Pengeluaran':<20} | {'Kategori':<20}")
    print("=" * 100)
    print(f"{data[id_pengeluaran]['id']:<10} | {data[id_pengeluaran]['jumlah_pengeluaran']:<20} | {data[id_pengeluaran]['keterangan']:<30} | {data[id_pengeluaran]['tanggal_pengeluaran']:<20} | {data[id_pengeluaran]['kategori_pengeluaran']:<20}")
    print("-" * 100)

    print("\n=== Update Data Pengeluaran ===\n(Tidak perlu diisi jika tidak ingin diubah)")
    
    kategori_pengeluaran = input(f"Masukkan kategori pengeluaran (Biaya pupuk atau Biaya tenaga kerja) [{data[id_pengeluaran]['kategori_pengeluaran']}]: ").strip().lower() or data[id_pengeluaran]['kategori_pengeluaran']
    
    while True:
        jumlah_pengeluaran = input(f"Masukkan jumlah pengeluaran [{data[id_pengeluaran]['jumlah_pengeluaran']}]: ").strip() or data[id_pengeluaran]['jumlah_pengeluaran']
        try:
            jumlah_pengeluaran = int(jumlah_pengeluaran)
        except ValueError:
            print("Error: Pastikan jumlah dalam format yang benar!\n")
            continue
        break
    
    while True:
        tanggal_pengeluaran = input(f"Tanggal Pengeluaran (YYYY-MM-DD) [{data[id_pengeluaran]['tanggal_pengeluaran']}]: ").strip() or data[id_pengeluaran]['tanggal_pengeluaran']
        try:
            datetime.strptime(tanggal_pengeluaran, "%Y-%m-%d")
        except ValueError:
            print("Error: Pastikan jumlah pengeluaran adalah angka dan tanggal dalam format yang benar.\n")
            continue
        break
    
    keterangan = input(f"Masukkan keterangan pengeluaran [{data[id_pengeluaran]['keterangan']}]: ").strip().lower() or data[id_pengeluaran]['keterangan']

    
    data[id_pengeluaran] = {
        "id": id_pengeluaran, 
        "jumlah_pengeluaran": jumlah_pengeluaran,
        "tanggal_pengeluaran": tanggal_pengeluaran,
        "kategori_pengeluaran": kategori_pengeluaran,
        "keterangan": keterangan
    }

    save_data(data)
    print("\nData pengeluaran berhasil diperbarui!")

def delete_pengeluaran():
    data = load_data()
    id_pengeluaran = input("Masukkan ID pengeluaran yang akan dihapus: ").strip()

    if id_pengeluaran in data:
        konfirmasi = input(f"Anda yakin ingin menghapus pemasukan {id_pengeluaran}? (y/n): ").lower()
        if konfirmasi == 'y':
            del data[id_pengeluaran]
            save_data(data)
            print("Pengeluaran berhasil dihapus!")
        else:
            print("Penghapusan dibatalkan.")
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

        pilihan = input("Pilih menu: ").strip()
        
        if pilihan == "1":
            add_pengeluaran()
        elif pilihan == "2":
            read_pengeluaran()
        elif pilihan == "3":
            update_pengeluaran()
        elif pilihan == "4":
            delete_pengeluaran()
        elif pilihan == "5":
            main_menu()
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")