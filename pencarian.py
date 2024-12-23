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
        print(f"{'ID':<10} {'Nama Tanaman':<20} {'Jenis Tanaman':<20} {'Tanggal Tanam':<20} {'Kondisi Tanaman':<20} {'Lokasi Tanaman':<20}")
        for tanaman in data.values():
            print(f"{tanaman['id']:<10} {tanaman['nama_tanaman']:<20} {tanaman['jenis_tanaman']:<20} {tanaman['tanggal_tanam']:<20} {tanaman['kondisi_tanaman']:<20} {tanaman['lokasi_tanaman']:<20}")
    else:
        print("\nTanaman tidak ditemukan.")

def cari_pemasukan():
    data = load_data("data/data_pemasukan.json")
    id_pemasukan = input("Masukkan ID pemasukan yang dicari: ")
    if id_pemasukan in data:
        print(f"\nMencari pemasukan dengan ID: {id_pemasukan}")
        print(f"{'Jumlah Penjualan':<20} {'Tanggal Penerimaan':<20} {'ID Panen':<10}")
        for pemasukan in data.values():
            print(f"{pemasukan['jumlah_penjualan']:<20} {pemasukan['tanggal_penerimaan']:<20} {pemasukan['id_panen']:<10}")
    else:
        print("\nPemasukan tidak ditemukan.")

def cari_pengeluaran():
    data = load_data("data/data_pengeluaran.json")
    id_pengeluaran = input("Masukkan ID pengeluaran yang dicari: ")
    if id_pengeluaran in data:
        print(f"\nMencari pengeluaran dengan ID: {id_pengeluaran}")
        print(f"{'Jumlah Pengeluaran':<20} {'Keterangan':<20} {'Tanggal Pengeluaran':<20} {'Kategori Pengeluaran':<20}")
        for pengeluaran in data.values():
            print(f"{pengeluaran['jumlah_pengeluaran']:<20} {pengeluaran['keterangan']:<20} {pengeluaran['tanggal_pengeluaran']:<20} {pengeluaran['kategori_pengeluaran']:<20}")
    else:
        print("\nPengeluaran tidak ditemukan.")

def cari_pekerja():
    data = load_data("data/data_pekerja.json")
    user_login = get_data_login()
    nama_pekerja = input("Masukkan nama pekerja yang dicari: ")
    if any(pekerja['nama'] == nama_pekerja for pekerja in data.values()):
        print(f"\nMencari pekerja dengan nama: {nama_pekerja}")
        print(f"{'ID':<10} {'Lokasi Kebun':<20} {'Nama':<20} {'Email':<20} {'Kontak':<20} {'Status':<20} {'Tanggal Bergabung':<20} {'Posisi/Jabatan':<20} {'Hari Kerja':<20} {'Jam Kerja':<20}")
        for pekerja in data.values():
            if pekerja['id_kebun'] == user_login['id_kebun']:
                print(f"{pekerja['id_pekerja']:<10} {user_login['alamat_kebun']:<20} {pekerja['nama']:<20} {pekerja['email']:<20} {pekerja['kontak']:<20} {pekerja['status']:<20} {pekerja['tanggal_bergabung']:<20} {pekerja['posisi_jabatan']:<20} {', '.join(pekerja['hari_kerja']):<20} {pekerja['jam_kerja']:<20}")
    else:
        print("\nPekerja tidak ditemukan.")

def cari_pupuk():
    data = load_data("data/data_pupuk.json")
    nama_pupuk = input("Masukkan nama pupuk yang dicari: ")
    if any(pupuk['nama_pupuk'] == nama_pupuk for pupuk in data.values()):
        print(f"\nMencari pupuk dengan nama: {nama_pupuk}")
        print(f"{'ID':<10} {'Nama Pupuk':<20} {'Stok':<10} {'Tanggal Penerimaan':<20} {'Catatan':<20}")
        for pupuk in data.values():
            print(f"{pupuk['id']:<10} {pupuk['nama_pupuk']:<20} {pupuk['stok']:<10} {pupuk['tanggal_penerimaan']:<20} {pupuk['catatan']:<20}")
    else:
        print("\nPupuk tidak ditemukan.")

def cari_jadwal_pengingat():
    data = load_data("data/data_jadwal_pengingat.json")
    id_jadwal = input("Masukkan ID jadwal pengingat yang dicari: ")
    if id_jadwal in data:
        print(f"\nMencari jadwal pengingat dengan ID: {id_jadwal}")
        print(f"{'Waktu Pengingat':<20} {'Frekuensi':<20}")
        for pengingat in data.values():
            print(f"{pengingat['waktu_pengingat']:<20} {'Setiap ' + str(pengingat['frekuensi_hari']) + ' hari':<20}")
    else:
        print("\nJadwal pengingat tidak ditemukan.")
