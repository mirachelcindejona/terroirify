import json

def load_data(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def get_data_login():
    try:
        with open("data/data_login.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def pencarian():
    from main import main_menu
    print("\n=== Pencarian Data ===")
    print("1. Pencarian Tanaman")
    print("2. Pencarian Pemasukan")
    print("3. Pencarian Pengeluaran")
    print("4. Pencarian Pekerja")
    print("5. Pencarian Pupuk")
    print("6. Pencarian Jadwal Pengingat")
    print("7. Kembali ke awal")
    pilihan = input("Pilih jenis pencarian (1-7): ")

    if pilihan == "1":
        cari_tanaman()
    elif pilihan == "2":
        cari_pemasukan()
    elif pilihan == "3":
        cari_pengeluaran()
    elif pilihan == "4":
        cari_pekerja()
    elif pilihan == "5":
        cari_pupuk()
    elif pilihan == "6":
        cari_jadwal_pengingat()
    elif pilihan == "7":
        main_menu()
    else:
        print("Pilihan tidak valid!")

def cari_tanaman():
    data = load_data("data/data_tanaman.json")
    nama_tanaman = input("Masukkan nama tanaman yang dicari: ")
    if any(tanaman['nama_tanaman'] == nama_tanaman for tanaman in data.values()):
        print(f"\nMencari tanaman dengan nama: {nama_tanaman}")
        for tanaman in data.values():
            print(f"ID: {tanaman['id']}")
            print(f"Nama Tanaman: {tanaman['nama_tanaman']}")
            print(f"Jenis Tanaman: {tanaman['jenis_tanaman']}")
            print(f"Tanggal Tanam: {tanaman['tanggal_tanam']}")
            print(f"Kondisi Tanaman: {tanaman['kondisi_tanaman']}")
            print(f"Lokasi Tanaman: {tanaman['lokasi_tanaman']}")
            print("-" * 30)
    else:
        print("\nTanaman tidak ditemukan.")

def cari_pemasukan():
    data = load_data("data/data_pemasukan.json")
    id_pemasukan = input("Masukkan ID pemasukan yang dicari: ")
    if id_pemasukan in data:
        print(f"\nMencari pemasukan dengan ID: {id_pemasukan}")
        for pemasukan_id, pemasukan in data.items():
            print(f"Jumlah Penjualan: {pemasukan['jumlah_penjualan']}")
            print(f"Tanggal Penerimaan: {pemasukan['tanggal_penerimaan']}")
            print(f"ID Panen: {pemasukan['id_panen']}")
            print("-" * 30)
    else:
        print("\nPemasukan tidak ditemukan.")

def cari_pengeluaran():
    data = load_data("data/data_pengeluaran.json")
    id_pengeluaran = input("Masukkan ID pengeluaran yang dicari: ")
    if id_pengeluaran in data:
        print(f"\nMencari pengeluaran dengan ID: {id_pengeluaran}")
        for pengeluaran_id, pengeluaran in data.items():
            print(f"Pengeluaran operasional: {pengeluaran['jumlah_pengeluaran']}")
            print(f"Nama pengeluaran:{pengeluaran['keterangan']}")
            print(f"Tanggal pengeluaran: {pengeluaran['tanggal_pengeluaran']}")  
            print(f"Kategori pengeluaran: {pengeluaran['kategori_pengeluaran']}")
            print("-" * 30)
        
    else:
        print("\nPengeluaran tidak ditemukan.")

def cari_pekerja():
    data = load_data("data/data_pekerja.json")
    user_login = get_data_login()
    nama_pekerja = input("Masukkan nama pekerja yang dicari: ")
    if any(pekerja['nama'] == nama_pekerja for pekerja in data.values()):
        print(f"\nMencari pekerja dengan nama: {nama_pekerja}")
        for pekerja in data.values():
            if pekerja['id_kebun'] == user_login['id_kebun']:
                print(f"ID: {pekerja['id_pekerja']}")
                print(f"Lokasi Kebun: {user_login['alamat_kebun']}")
                print(f"Nama: {pekerja['nama']}")
                print(f"Email: {pekerja['email']}")
                print(f"Kontak: {pekerja['kontak']}")
                print(f"Status: {pekerja['status']}")
                print(f"Tanggal Bergabung: {pekerja['tanggal_bergabung']}")
                print(f"Posisi/Jabatan: {pekerja['posisi_jabatan']}")
                print(f"Hari Kerja: {', '.join(pekerja['hari_kerja'])}")
                print(f"Jam Kerja: {pekerja['jam_kerja']}")
                print("-" * 30)
    else:
        print("\nPekerja tidak ditemukan.")

def cari_pupuk():
    data = load_data("data/data_pupuk.json")
    nama_pupuk = input("Masukkan nama pupuk yang dicari: ")
    if any(pupuk['nama_pupuk'] == nama_pupuk for pupuk in data.values()):
        print(f"\nMencari pupuk dengan nama: {nama_pupuk}")
        for pupuk in data.values():
            print(f"ID: {pupuk['id']}")
            print(f"Nama Pupuk: {pupuk['nama_pupuk']}")
            print(f"Stok: {pupuk['stok']}")
            print(f"Tanggal Penerimaan: {pupuk['tanggal_penerimaan']}")
            print(f"Catatan: {pupuk['catatan']}")
            print("-" * 30)
    else:
        print("\nPupuk tidak ditemukan.")

def cari_jadwal_pengingat():
    data = load_data("data/data_jadwal_pengingat.json")
    id_jadwal = input("Masukkan ID jadwal pengingat yang dicari: ")
    if id_jadwal in data:
        print(f"\nMencari jadwal pengingat dengan ID: {id_jadwal}")
        for jadwal_pengingat_id, pengingat in data.items():
            print(f"Waktu Pengingat: {pengingat['waktu_pengingat']}")
            print(f"Frekuensi: Setiap {pengingat['frekuensi_hari']} hari")
            print("-" * 30)
    else:
        print("\nJadwal pengingat tidak ditemukan.")
