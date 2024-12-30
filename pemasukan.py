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
    
    print("\nPilih data panen yang ingin ditambah ke pemasukkan.")
    print("=" * 120)
    print(f"{'ID':<10} | {'Nama Tanaman':<20} | {'Jumlah':<10} | {'Satuan':<8} | {'Tanggal':<12} | {'Kualitas':<10} | {'Harga/Satuan':<12} | {'Total Harga':<15}")
    print("=" * 120)
    for nama_panen_id, panen in data_panen.items():
        nama_tanaman = data_tanaman[panen['id_tanaman']]['nama_tanaman']
        print(f"{panen['id']:<10} | {nama_tanaman:<20} | {panen['jumlah_panen']:<10} | {panen['satuan_panen']:<8} | {panen['tanggal_panen']:<12} | {panen['kualitas_panen']:<10} | Rp {panen['harga_per_satuan']:,.2f} | Rp {panen['total_harga']:,.2f}")
        print("-" * 120)
    
    while True:
        nama_panen_id = input("\nMasukkan ID panen yang ingin ditambah ke pemasukkan: ").strip()
        if nama_panen_id not in data_panen:
            print("ID panen tidak valid. Silakan memilih ID panen yang ada.\n")
            continue
        break
            
    while True:    
        jumlah_penjualan = input("Masukkan jumlah penjualan: ").strip()
        if not jumlah_penjualan:
            print("Error: Jumlah penjualan tidak boleh kosong!\n")
            continue
        try:
            jumlah_penjualan = float(jumlah_penjualan)
            if jumlah_penjualan <= 0:
                print("Error: Jumlah penjualan harus lebih besar dari 0!\n")
                continue
            break
        except ValueError:
            print("Error: Jumlah penjualan harus berupa angka!\n")
            
    while True: 
      tanggal_penerimaan = input("Tanggal Penerimaan (YYYY-MM-DD): ").strip()
      if not tanggal_penerimaan:
         print("Error: Tanggal penerimaan tidak boleh kosong!\n")
         continue
      else:
         try:
            datetime.strptime(tanggal_penerimaan, "%Y-%m-%d")
         except ValueError:
            print("Error: Pastikan tanggal dalam format yang benar.\n")
            continue
         break
    
    data[id_pemasukan] = {
        "id": id_pemasukan,
        "id_panen": nama_panen_id,
        "jumlah_penjualan": jumlah_penjualan,
        "tanggal_penerimaan": tanggal_penerimaan,
    }

    save_data(data)
    print("Data pemasukan berhasil ditambahkan!")

def read_pemasukan():
    data = load_data()
    if data:
        print("\n=== Data Pemasukan ===\n")
        print("=" * 60)
        print(f"{'ID':<10} | {'Jumlah Penjualan':<20} | {'Tanggal Penerimaan':<20} | {'ID Panen':<10}")
        print("=" * 60)
        for pemasukan_id, pemasukan in data.items():
            print(f"{pemasukan['id']:<10} | {pemasukan['jumlah_penjualan']:<20} | {pemasukan['tanggal_penerimaan']:<20} | {pemasukan['id_panen']:<10}")
        print("-" * 60)
    else:
        print("Tidak ada data pemasukan.")

def update_pemasukan():
    data = load_data()
    id_pemasukan = input("Masukkan ID pemasukan yang akan diperbarui: ").strip()

    if not id_pemasukan:
      print("Error: ID pemasukan tidak boleh kosong!\n")
      return
    if id_pemasukan not in data:
        print("Pemasukan dengan ID tersebut tidak ditemukan.")
        return
    
    print(f"\n=== Data pemasukan saat ini dengan ID {id_pemasukan} ===\n")
    print("=" * 100)
    print(f"{'ID':<10} | {'Jumlah Penjualan':<20} | {'Tanggal Penerimaan':<20} | {'ID Panen':<10}")
    print("=" * 100)
    print(f"{data[id_pemasukan]['id']:<10} | {data[id_pemasukan]['jumlah_penjualan']:<20} | {data[id_pemasukan]['tanggal_penerimaan']:<20} | {data[id_pemasukan]['id_panen']:<10}")
    print("-" * 100)
    
    print("\n=== Update Data Pemasukan ===\n(Tidak perlu diisi jika tidak ingin diubah)")

    data_panen = load_data_panen()
    if not data_panen:
        print("Tidak ada data panen tersedia.")
        return
    
    data_tanaman = load_data_tanaman()
    if not data_tanaman:
        print("Tidak ada data tanaman tersedia.")
        return
    
    print("\nPilih data panen yang ingin diperbarui ke pemasukkan.")
    print("=" * 120)
    print(f"{'ID':<10} | {'Nama Tanaman':<20} | {'Jumlah':<10} | {'Satuan':<8} | {'Tanggal':<12} | {'Kualitas':<10} | {'Harga/Satuan':<12} | {'Total Harga':<15}")
    print("=" * 120)
    for panen_id, panen in data_panen.items():
        nama_tanaman = data_tanaman[panen['id_tanaman']]['nama_tanaman']
        print(f"{panen['id']:<10} | {nama_tanaman:<20} | {panen['jumlah_panen']:<10} | {panen['satuan_panen']:<8} | {panen['tanggal_panen']:<12} | {panen['kualitas_panen']:<10} | Rp {panen['harga_per_satuan']:,.2f} | Rp {panen['total_harga']:,.2f}")
        print("-" * 120)
    
    nama_panen_id = input(f"\nMasukkan ID panen yang ingin diperbarui ke pemasukkan [{data[id_pemasukan]['id_panen']}]: ").strip() or data[id_pemasukan]['id_panen']
    if nama_panen_id not in data_panen:
        print("Error: ID panen tidak ada! Pastikan ID panen sesuai dengan data panen yang ada.")
        return
    if not nama_panen_id:
        print("Error: ID panen tidak boleh kosong!")
        return

    while True:
        jumlah_penjualan = input(f"Masukkan jumlah penjualan [{data[id_pemasukan]['jumlah_penjualan']}]: ").strip() or data[id_pemasukan]['jumlah_penjualan']
        try:
            jumlah_penjualan = float(jumlah_penjualan)
        except ValueError:
            print("Error: Jumlah penjualan harus berupa angka!\n")
            continue
        break
    
    while True:
        tanggal_penerimaan = input(f"Tanggal Penerimaan (YYYY-MM-DD) [{data[id_pemasukan]['tanggal_penerimaan']}]: ").strip() or data[id_pemasukan]['tanggal_penerimaan']
        try:
            datetime.strptime(tanggal_penerimaan, "%Y-%m-%d")
        except ValueError:
            print("Error: Pastikan tanggal dalam format yang benar.\n")
            continue
        break
    
    data[id_pemasukan] = {
        "id": id_pemasukan,
        "id_panen": nama_panen_id,
        "jumlah_penjualan": jumlah_penjualan,
        "tanggal_penerimaan": tanggal_penerimaan,
    }

    save_data(data)
    print("\nData pemasukan berhasil diperbarui!")

def delete_pemasukan():
    data = load_data()
    id_pemasukan = input("\nMasukkan ID Pemasukan yang akan dihapus: ").strip()

    if id_pemasukan in data:
        konfirmasi = input(f"Anda yakin ingin menghapus pemasukan {id_pemasukan}? (y/n): ").lower()
        if konfirmasi == 'y':
            del data[id_pemasukan]
            save_data(data)
            print("Pemasukan berhasil dihapus!")
        else:
            print("Penghapusan dibatalkan.")
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

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            add_pemasukan()
        elif pilihan == "2":
            read_pemasukan()
        elif pilihan == "3":
            update_pemasukan()
        elif pilihan == "4":
            delete_pemasukan()
        elif pilihan == "5":
            main_menu()
        else:
            print("Pilihan tidak valid. Silahkan pilih lagi.")