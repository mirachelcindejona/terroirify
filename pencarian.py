import json

def load_data(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def pencarian():
    print("\n=== Pencarian Data ===")
    print("1. Pencarian Tanaman")
    print("2. Pencarian Pemasukan")
    print("3. Pencarian Pengeluaran")
    print("4. Pencarian Pekerja")
    print("5. Pencarian Pupuk")
    print("6. Pencarian Jadwal Pengingat")
    pilihan = input("Pilih jenis pencarian (1-6): ")

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
    else:
        print("Pilihan tidak valid!")

def cari_tanaman():
    data = load_data("data/data_tanaman.json")
    nama_tanaman = input("Masukkan nama tanaman yang dicari: ")
    if any(tanaman['nama'] == nama_tanaman for tanaman in data.values()):
        print(f"Mencari tanaman dengan nama: {nama_tanaman}")
    else:
        print("Tanaman tidak ditemukan.")

def cari_pemasukan():
    data = load_data("data/data_pemasukan.json")
    id_pemasukan = input("Masukkan ID pemasukan yang dicari: ")
    if id_pemasukan in data:
        print(f"Mencari pemasukan dengan ID: {id_pemasukan}")
    else:
        print("Pemasukan tidak ditemukan.")

def cari_pengeluaran():
    data = load_data("data/data_pengeluaran.json")
    id_pengeluaran = input("Masukkan ID pengeluaran yang dicari: ")
    if id_pengeluaran in data:
        print(f"Mencari pengeluaran dengan ID: {id_pengeluaran}")
    else:
        print("Pengeluaran tidak ditemukan.")

def cari_pekerja():
    data = load_data("data/data_pekerja.json")
    nama_pekerja = input("Masukkan nama pekerja yang dicari: ")
    if any(pekerja['nama'] == nama_pekerja for pekerja in data.values()):
        print(f"Mencari pekerja dengan nama: {nama_pekerja}")
    else:
        print("Pekerja tidak ditemukan.")

def cari_pupuk():
    data = load_data("data/data_pupuk.json")
    nama_pupuk = input("Masukkan nama pupuk yang dicari: ")
    if any(pupuk['nama'] == nama_pupuk for pupuk in data.values()):
        print(f"Mencari pupuk dengan nama: {nama_pupuk}")
    else:
        print("Pupuk tidak ditemukan.")

def cari_jadwal_pengingat():
    data = load_data("data/data_jadwal_pengingat.json")
    id_jadwal = input("Masukkan ID jadwal pengingat yang dicari: ")
    if id_jadwal in data:
        print(f"Mencari jadwal pengingat dengan ID: {id_jadwal}")
    else:
        print("Jadwal pengingat tidak ditemukan.")
