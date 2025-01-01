import json
from datetime import datetime
from tanaman import load_data as load_data_tanaman

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

    # Memuat data tanaman untuk pilihan
    data_tanaman = load_data_tanaman()
    if not data_tanaman:
        print("Tidak ada data tanaman tersedia.")
        return

    print("\nPilih tanaman yang ingin dipanen.")
    print("=" * 100)
    print(f"{'ID':<10} | {'Nama Tanaman':<20} | {'Jenis Tanaman':<20} | {'Tanggal Tanam':<15} | {'Kondisi':<15} | {'Lokasi':<20}")
    print("=" * 100)
    for id_tanaman, tanaman in data_tanaman.items():
        print(f"{tanaman['id']:<10} | {tanaman['nama_tanaman']:<20} | {tanaman['jenis_tanaman']:<20} | {tanaman['tanggal_tanam']:<15} | {tanaman['kondisi_tanaman']:<15} | {tanaman['lokasi_tanaman']:<20}")
        print("-" * 100)

    while True:
        nama_tanaman_id = input("\nMasukkan ID tanaman yang ingin dipanen: ").strip()
        if not nama_tanaman_id:
            print("Error: ID tanaman tidak boleh kosong!\n")
            continue
        if nama_tanaman_id not in data_tanaman:
            print("ID tanaman tidak valid! Pastikan ID yang Anda masukkan sudah ada di database tanaman.\n")
            continue
        break

    while True: 
        jumlah_panen = input("Jumlah Panen: ").strip()
        if not jumlah_panen:
            print("Error: Jumlah panen tidak boleh kosong!\n")
            continue
        try:
            jumlah_panen = float(jumlah_panen)
        except ValueError:
            print("Error: Jumlah panen harus berupa angka!\n")
            continue
        if jumlah_panen <= 0:
            print("Error: Jumlah panen tidak boleh kurang dari atau sama dengan 0\n")
            continue
        break
    
    while True:
        satuan_panen = input("Satuan Panen (kg/buah/ikat): ").strip().lower()
        if not satuan_panen:
            print("Error: Satuan panen tidak boleh kosong!\n")
            continue
        if satuan_panen not in ['kg', 'buah', 'ikat']:
            print("Error: Satuan panen tidak valid! Pastikan Anda memasukkan salah satu dari 'kg', 'buah', atau 'ikat'\n")
            continue
        break
        
    while True: 
        tanggal_panen = input("Tanggal Panen (YYYY-MM-DD): ").strip()
        if not tanggal_panen:
            print("Error: Tanggal panen tidak boleh kosong!\n")
            continue
        else:
            try:
                datetime.strptime(tanggal_panen, "%Y-%m-%d")
            except ValueError:
                print("Error: Input tidak valid. Pastikan tanggal dalam format yang benar.\n")
                continue
            break
    
    while True:
        kualitas_panen = input("Kualitas Panen: ").strip().lower()
        if not kualitas_panen:
            print("Error: Kualitas panen tidak boleh kosong!\n")
            continue
        break
        
    while True:
        harga_per_satuan = input("Harga Per Satuan (Rp): ").strip()
        if not harga_per_satuan:
            print("Error: Harga per satuan tidak boleh kosong!\n")
            continue
        try:
            harga_per_satuan = float(harga_per_satuan)  
            if harga_per_satuan <= 0:
                print("Error: Harga per satuan tidak boleh kurang dari atau sama dengan 0\n") 
                continue
        except ValueError:
            print("Error: Harga per satuan harus berupa angka!\n")  
            continue
        break    
        
    total_harga = jumlah_panen * harga_per_satuan
        
    data[id_panen] = {
        "id": id_panen,
        "id_tanaman": nama_tanaman_id,
        "jumlah_panen": jumlah_panen,
        "satuan_panen": satuan_panen,
        "tanggal_panen": tanggal_panen,
        "kualitas_panen": kualitas_panen,
        "harga_per_satuan": harga_per_satuan,
        "total_harga": total_harga
    }
    
    save_data(data)
    print("Data panen berhasil ditambahkan!")

def read_panen():
    data = load_data()
    if data:
        print("\n=== Data Panen ===\n")
        print("=" * 120)
        print(f"{'ID':<10} | {'Nama Tanaman':<20} | {'Jumlah':<10} | {'Satuan':<8} | {'Tanggal':<12} | {'Kualitas':<10} | {'Harga/Satuan':<12} | {'Total Harga':<15}")
        print("=" * 120)
        data_tanaman = load_data_tanaman()
        for panen_id, panen in data.items():
            nama_tanaman = data_tanaman[panen['id_tanaman']]['nama_tanaman']
            print(f"{panen['id']:<10} | {nama_tanaman:<20} | {panen['jumlah_panen']:<10} | {panen['satuan_panen']:<8} | {panen['tanggal_panen']:<12} | {panen['kualitas_panen']:<10} | Rp {panen['harga_per_satuan']:,.2f} | Rp {panen['total_harga']:,.2f}")
            print("-" * 120)
    else:
        print("Tidak ada data panen.")

def update_panen():
    data = load_data()
    id_panen = input("\nMasukkan ID panen yang akan diperbarui: ").strip()
    if id_panen not in data:
        print("Panen dengan ID tersebut tidak ditemukan.")
        return
    if not id_panen:
        print("Error: ID panen tidak boleh kosong!\n")
        return
    
    print(f"\n=== Data panen saat ini dengan ID {id_panen} ===\n")
    print("=" * 120)
    print(f"{'ID':<10} | {'Nama Tanaman':<20} | {'Jumlah':<10} | {'Satuan':<8} | {'Tanggal':<12} | {'Kualitas':<10} | {'Harga/Satuan':<12} | {'Total Harga':<15}")
    print("=" * 120)
    data_tanaman = load_data_tanaman()
    nama_tanaman = data_tanaman[data[id_panen]['id_tanaman']]['nama_tanaman']
    print(f"{data[id_panen]['id']:<10} | {nama_tanaman:<20} | {data[id_panen]['jumlah_panen']:<10} | {data[id_panen]['satuan_panen']:<8} | {data[id_panen]['tanggal_panen']:<12} | {data[id_panen]['kualitas_panen']:<10} | Rp {data[id_panen]['harga_per_satuan']:,.2f} | Rp {data[id_panen]['total_harga']:,.2f}")
    print("-" * 120)

    print("\n=== Update Data Panen ===\n(Tidak perlu diisi jika tidak ingin diubah)")
    
    # Memuat data tanaman untuk pilihan
    data_tanaman = load_data_tanaman()
    if not data_tanaman:
        print("Tidak ada data tanaman tersedia.")
        return

    print("\nPilih tanaman yang ingin dipanen.")
    print("=" * 100)
    print(f"{'ID':<10} | {'Nama Tanaman':<20} | {'Jenis Tanaman':<20} | {'Tanggal Tanam':<15} | {'Kondisi':<15} | {'Lokasi':<20}")
    print("=" * 100)
    for id_tanaman, tanaman in data_tanaman.items():
        print(f"{tanaman['id']:<10} | {tanaman['nama_tanaman']:<20} | {tanaman['jenis_tanaman']:<20} | {tanaman['tanggal_tanam']:<15} | {tanaman['kondisi_tanaman']:<15} | {tanaman['lokasi_tanaman']:<20}")
        print("-" * 100)

    nama_tanaman_id = input(f"Masukkan ID tanaman yang ingin dipanen [{data[id_panen]['id_tanaman']}]: ") or data[id_panen]['id_tanaman']
    if nama_tanaman_id not in data_tanaman:
        print(f"\nID tanaman tidak valid! Pastikan ID tanaman sesuai dengan data yang ada.")
        return
    
    while True:
        jumlah_panen = input(f"Jumlah Panen [{data[id_panen]['jumlah_panen']}]: ").strip() or data[id_panen]['jumlah_panen']
        try:
            jumlah_panen = float(jumlah_panen)
        except ValueError:
            print("Error: Jumlah panen harus berupa angka!\n")
            continue
        if jumlah_panen <= 0:
            print("Error: Jumlah panen tidak boleh kurang dari atau sama dengan 0\n")
            continue
        break
    
    while True:
        satuan_panen = input(f"Satuan Panen (kg/buah/ikat) [{data[id_panen]['satuan_panen']}]: ").strip().lower() or data[id_panen]['satuan_panen']
        if satuan_panen not in ['kg', 'buah', 'ikat']:
            print("Error: Satuan panen tidak valid! Pastikan Anda memasukkan salah satu dari 'kg', 'buah', atau 'ikat'\n")
            continue
        break
    
    while True:
      tanggal_panen = input(f"Tanggal Panen (YYYY-MM-DD) [{data[id_panen]['tanggal_panen']}]: ").strip() or data[id_panen]['tanggal_panen']
      try:
         datetime.strptime(tanggal_panen, "%Y-%m-%d")
      except ValueError:
         print("Error:  Pastikan tanggal panen dalam format yang benar.\n")
         continue
      break
    
    kualitas_panen = input(f"Kualitas Panen [{data[id_panen]['kualitas_panen']}]: ").strip().lower() or data[id_panen]['kualitas_panen']
        
    while True:
        harga_per_satuan = input(f"Harga Per Satuan (Rp) [{data[id_panen]['harga_per_satuan']}]: ").strip() or data[id_panen]['harga_per_satuan']
        try:
            harga_per_satuan = float(harga_per_satuan)  
            if harga_per_satuan <= 0:
                print("Error: Harga per satuan tidak boleh kurang dari atau sama dengan 0\n") 
                continue
        except ValueError:
            print("Error: Harga per satuan harus berupa angka!\n")  
            continue
        break
    
    total_harga = jumlah_panen * harga_per_satuan

    data[id_panen] = {
        "id": id_panen,
        "id_tanaman": nama_tanaman_id,
        "jumlah_panen": jumlah_panen,
        "satuan_panen": satuan_panen,
        "tanggal_panen": tanggal_panen,
        "kualitas_panen": kualitas_panen,
        "harga_per_satuan": harga_per_satuan,
        "total_harga": total_harga
    }
    
    save_data(data)
    print(f"\nData panen berhasil diperbarui!")

def delete_panen():
    data = load_data()
    id_panen = input("Masukkan ID panen yang akan dihapus: ").strip()
    
    if id_panen in data:
        konfirmasi = input(f"Anda yakin ingin menghapus panen {id_panen}? (y/n): ").lower()
        if konfirmasi == 'y':
            del data[id_panen]
            save_data(data)
            print("Panen berhasil dihapus!")
        else:
            print("Penghapusan dibatalkan.")
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
        
        pilihan = input("Pilih menu: ").strip()
        
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
