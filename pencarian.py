import json
from datetime import datetime

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
    
def tampilkan_tabel(data, kolom):
    header = "| " + " | ".join(f"{kol[0]:<{kol[2]}}" for kol in kolom) + " |"
    separator = "+-" + "-+-".join("-" * kol[2] for kol in kolom) + "-+"

    print(separator)
    print(header)
    print(separator)
    
    for item in data:
        row = "| " + " | ".join(f"{str(item.get(kol[1], '')):<{kol[2]}}" for kol in kolom) + " |"
        print(row)
        print(separator)

def pencarian():
    from main import main_menu
    while True:
        print("\n=== Pencarian Data ===")
        print("1. Pencarian Tanaman")
        print("2. Pencarian Pemasukan")
        print("3. Pencarian Pengeluaran")
        print("4. Pencarian Pekerja")
        print("5. Pencarian Pupuk")
        print("6. Pencarian Jadwal Pengingat")
        print("7. Kembali ke awal")
        
        print("="*30)
            
        pilihan = input("\nPilih jenis pencarian (1-7): ")

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
            break
        else:
            print("Pilihan tidak valid! Silakan masukkan angka antara 1-7.")
            
def cari_tanaman():
    data = load_data("data/data_tanaman.json")
    print("\n=== Cari Tanaman Berdasarkan ===")
    print("1. Berdasarkan ID")
    print("2. Berdasarkan Nama")
    print("3. Berdasarkan Jenis Tanaman")
    print("4. Berdasarkan Tanggal Tanam")
    print("="*30)
    
    pilihan = input("\nPilih kriteria pencarian (1-4): ")
    
    hasil = []
    
    if pilihan == "1":
        id_tanaman = input("Masukkan ID tanaman yang ingin dicari: ").strip()
        if id_tanaman in data:
            hasil.append(data[id_tanaman])
            
    elif pilihan == "2":
        nama_tanaman = input("Masukkan nama tanaman yang dicari: ")
        hasil = [tanaman for tanaman in data.values() if tanaman['nama_tanaman'].lower() == nama_tanaman.lower()]
        
    elif pilihan == "3":
        jenis_tanaman = input("Masukkan jenis tanaman yang ingin dicari: ")
        hasil = [tanaman for tanaman in data.values() if tanaman['jenis_tanaman'].lower() == jenis_tanaman.lower()]
        
    elif pilihan == "4":
        tanggal_tanam = input("Masukkan tanggal tanam yang ingin dicari(YYYY-MM-DD): ").strip()
        try: 
            datetime.strptime(tanggal_tanam, "%Y-%m-%d")
            hasil = [tanaman for tanaman in data.values() if tanaman['tanggal_tanam'] == tanggal_tanam]
        except ValueError:
            print("Format tanggal tidak valid. Gunakan format YYYY-MM-DD.")
            return
        
    else:
        print("Pilihan tidak valid! Silakan coba lagi.")
        return
        
    if hasil: 
        print("\n=== Hasil Pencarian Tanaman ===")
        kolom_tanaman = [
            ("ID", "id", 10),
            ("Nama Tanaman", "nama_tanaman", 20),
            ("Jenis Tanaman", "jenis_tanaman", 20),
            ("Tanggal Tanam", "tanggal_tanam", 20),
            ("Kondisi Tanaman", "kondisi_tanaman", 20),
            ("Lokasi Tanaman", "lokasi_tanaman", 20)
        ]
        tampilkan_tabel(hasil, kolom_tanaman)
        
    else:
        print("Tanaman tidak ditemukan.")
    
    input("\nTekan Enter untuk kembali ke menu pencarian.")

def cari_pemasukan():
    data = load_data("data/data_pemasukan.json")
    print("\n=== Cari Pemasukan Berdasarkan ===")
    print("1. Berdasarkan ID")
    print("2. Berdasarkan Tanggal Penerimaan")
    print("="*30)
    
    pilihan = input("Pilih kriteria pencarian (1-2): ")
    
    hasil = []
    
    if pilihan == "1":
        id_pemasukan = input("Masukkan ID pemasukan yang ingin dicari: ").strip()
        if id_pemasukan in data:
            hasil.append(data[id_pemasukan])
            
    elif pilihan == "2":
        tanggal_penerimaaan = input("Masukkan tanggal penerimaan panen yang akan dicari (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(tanggal_penerimaaan, "%Y-%m-%d")
            hasil = [pemasukan for pemasukan in data.values() if pemasukan["tanggal_penerimaan"]== tanggal_penerimaaan]
        except ValueError:
            print("Format tanggal tidak valid. Gunakan format YYYY-MM-DD.")
            return
        
    else:
        print("Pilihan tidak valid! Silakan coba lagi.")
        
    if hasil:
        print("\n=== Hasil Pencarian Pemasukan ===")
        kolom_pemasukan = [
            ("ID", "id", 10),
            ("Jumlah Penjualan", "jumlah_penjualan", 20),
            ("Tanggal Pemasukan", "tanggal_penerimaan", 20),
            ("ID Panen", "id_panen", 20)
        ]
        tampilkan_tabel(hasil, kolom_pemasukan)
        
    else:
        print("Pemasukan tidak ditemukan.")
        
    input("\nTekan Enter untuk kembali ke menu pencarian")

def cari_pengeluaran():
    data = load_data("data/data_pengeluaran.json")
    print("\n=== Cari Pengeluaran Berdasarkan ===")
    print("1. Berdasarkan ID")
    print("2. Berdasarkan kategori")
    print("3. Berdasarkan Tanggal Penerimaan")
    print("="*30)
    
    pilihan = input("Pilih kriteria pencarian (1-3): ")
    
    hasil = []
    
    if pilihan == "1":
        id_pengeluaran = input("Masukkan ID pengeluaran yang ingin dicari: ").strip()
        if id_pengeluaran in data:
            hasil.append(data[id_pengeluaran])
            
    elif pilihan == "2":
        kategori_pengeluaran = input("Masukkan kategori pengeluaran yang ingin dicari: ").lower()
        hasil = [pengeluaran for pengeluaran in data.values() if pengeluaran["kategori_pengeluaran"] == kategori_pengeluaran]
            
    elif pilihan == "3":
        tanggal_pengeluaran = input("Masukkan tanggal pengeluaran yang akan dicari (YYYY-MM-DD): ")
        try:
            datetime.strptime(tanggal_pengeluaran, "%Y-%m-%d")
            hasil = [pengeluaran for pengeluaran in data.values() if pengeluaran["tanggal_pengeluaran"]== tanggal_pengeluaran]
        except ValueError:
            print("Format tanggal tidak valid. Gunakan format YYYY-MM-DD.")
            return

    else:
        print("Pilihan tidak valid! Silakan coba lagi.")
        
    if hasil:
        print("\n=== Hasil Pencarian Pengeluaran ===")
        kolom_pengeluaran = [
            ("ID", "id", 10), 
            ("Jumlah Pengeluaran", "jumlah_pengeluaran", 20),
            ("Tanggal Pengeluaran", "tanggal_pengeluaran", 20),
            ("Kategori Pengeluaran", "kategori_pengeluaran", 20),
            ("Keterangan", "keterangan", 20)
        ]
        tampilkan_tabel(hasil, kolom_pengeluaran)
    else:
        print("Pengeluaran tidak ditermukan.")
        
    input("\nTekan Enter untuk kembali ke menu pencarian")
    
def cari_pekerja():
    data = load_data("data/data_pekerja.json")
    user_login = get_data_login()
    print("\n=== Cari Pekerja Berdasarkan ===")
    print("1. Berdasarkan ID")
    print("2. Berdasarkan Nama")
    print("3. Berdasarkan Email")
    print("4. Berdasarkan Kontak")
    print("5. Berdasarkan Tanggal Bergabung")
    print("6. Berdasarkan Hari Kerja")
    print("="*30)
    
    pilihan = input("Masukan kriteria pencarian(1-6): ").strip()
    
    hasil = []
    
    if pilihan == "1":
        id_pekerja = input("Masukkan ID Pekerja yang ingin dicari: ").strip()
        if id_pekerja in data:
            hasil.append(data[id_pekerja])
    
    elif pilihan == "2":
        nama_pekerja = input("Masukkan nama pekerja yang dicari: ").lower()
        hasil = [pekerja for pekerja in data.values() if pekerja["nama"].lower() == nama_pekerja.lower()]
    
    elif pilihan == "3":
        email_pekerja = input("Masukkan email pekerja yang dicari: ").strip().lower()
        hasil = [pekerja for pekerja in data.values() if pekerja["email"].lower() == email_pekerja]
    
    elif pilihan == "4":
        kontak_pekerja = input("Masukkan kontak pekerja yang dicari: ").strip() 
        hasil = [pekerja for pekerja in data.values() if pekerja["kontak"] == kontak_pekerja]

    elif pilihan == "5":
            tanggal_bergabung = input("Masukkan tanggal bergabung (YYYY-MM-DD): ").strip()
            try:
                datetime.strptime(tanggal_bergabung, "%Y-%m-%d")
                hasil = [pekerja for pekerja in data.values() if pekerja["tanggal_bergabung"] == tanggal_bergabung]
            except ValueError:
                print("Format tanggal tidak valid. Gunakan format YYYY-MM-DD.")
                return

    elif pilihan == "6":
        hari_kerja = input("Masukkan hari kerja (contoh: Senin): ").lower()
        hasil = [pekerja for pekerja in data.values() if hari_kerja in map(str.lower, pekerja["hari_kerja"])]
    
    else:
        print("Pilihan tidak valid! Silakan coba lagi")
        return
    
    if hasil:
        print("\n=== Hasil Pencarian Pekerja ===")
        kolom_pekerja = [
            ("ID", "id_pekerja", 10),
            ("Nama", "nama", 20),
            ("Email", "email", 30),
            ("Kontak", "kontak", 15),
            ("Tanggal Bergabung", "tanggal_bergabung", 20),
            ("Jabatan", "posisi_jabatan", 20),
            ("Hari Kerja", "hari_kerja", 30),
            ("Jam Kerja", "jam_kerja", 15)
        ]
        tampilkan_tabel(hasil, kolom_pekerja)
    else:
        print("\nPekerja tidak ditemukan.")
        
    input("\nTekan Enter untuk kembali ke menu pencarian.")

def cari_pupuk():
    data = load_data("data/data_pupuk.json")
    print("\n=== Cari Pupuk Berdasarkan ===")
    print("1. Berdasarkan ID")
    print("2. Berdasarkan Nama")
    print("3. Berdasarkan Tanggal Penerimaan")
    print("="*30)
    
    pilihan = input("Masukan kriteria pencarian (1-3): ")
    
    hasil = []
    
    if pilihan == "1":
        id_pupuk = input("Masukkan ID pupuk yang ingin dicari: ")
        if id_pupuk in data:
            hasil.append(data[id_pupuk])
            
    elif pilihan == "2":
        nama_pupuk = input("Masukkan nama pupuk yang dicari: ").strip().lower()
        hasil = [pupuk for pupuk in data.values() if pupuk["nama_pupuk"].lower() == nama_pupuk]
    
    elif pilihan == "3":
        tanggal_penerimaan = input("Masukkan tanggal penerimaan pupuk (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(tanggal_penerimaan, "%Y-%m-%d")
            hasil = [pupuk for pupuk in data.values() if pupuk["tanggal_penerimaan"] == tanggal_penerimaan]
        except ValueError:
            print("Format tanggal tidak valid. Gunakan format YYYY-MM-DD.")
            return
        
    else:
        print("Pilihan tidak valid.")
        return
    
    if hasil:
        print("\n=== Hasil Pencarian Pupuk ===")
        kolom_pupuk = [
            ("ID", "id", 10),
            ("Nama Pupuk", "nama_pupuk", 20),
            ("Stok", "stok", 10),
            ("Tanggal Penerimaan", "tanggal_penerimaan", 20),
            ("Catatan", "catatan", 30)
        ]
        tampilkan_tabel(hasil, kolom_pupuk)
    else:
        print("\nPupuk tidak ditemukan.")
        
    input("\nTekan Enter untuk kembali ke menu pencarian")

def cari_jadwal_pengingat():
    data = load_data("data/data_jadwal_pengingat.json")
    print("\n=== Cari Jadwal Pengingat Berdasarkan ===")
    print("1. Berdasarkan ID")
    print("2. Berdasarkan Waktu Pengingat")
    print("="*30)
    
    pilihan = input("Masukkan Kriteria pencarian (1-2): ").strip()
    
    hasil = []
    
    if pilihan == "1":
        id_jadwal = input("Masukkan ID jadwal pengingat yang ingin dicari: ").strip()
        if id_jadwal in data:
            hasil.append(data[id_jadwal])
    
    elif pilihan == "2":
        waktu_pengingat = input("Masukkan waktu pengingat yang ingin dicari (HH:MM): ").strip()
        hasil = [jadwal for jadwal in data.values() if jadwal["waktu_pengingat"] == waktu_pengingat]
    
    else:
        print("Pilihan tidak valid! Silakan coba lagi")
        return
    
    if hasil:
        print("\n=== Hasil Pencarian Jadwal Pengingat ===")
        kolom_jadwal = [
            ("ID", "id", 10),
            ("Waktu Pengingat", "waktu_pengingat", 15),
            ("Frekuensi (hari)", "frekuensi_hari", 20),
            ("Status", "status", 10)
        ]
        tampilkan_tabel(hasil, kolom_jadwal)
    else:
        print("\nJadwal pengingat tidak ditemukan.")
        
    input("\nTekan Enter untuk kembali ke menu pencarian")