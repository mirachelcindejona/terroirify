import json
from datetime import datetime, timedelta
import time
import threading
from tanaman import load_data as load_data_tanaman

DATA_JADWAL_PENGINGAT = "data/data_jadwal_pengingat.json"

def load_data():
    try:
        with open(DATA_JADWAL_PENGINGAT, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_data(data):
    with open(DATA_JADWAL_PENGINGAT, "w") as file:
        json.dump(data, file, indent=4)

def generate_id(data):
    jadwal_pengingat_id = f"JP{str(len(data) + 1).zfill(3)}"
    while jadwal_pengingat_id in data:
        num = int(jadwal_pengingat_id[2:]) + 1
        jadwal_pengingat_id = f"JP{str(num).zfill(3)}"
    return jadwal_pengingat_id

def add_jadwal_pengingat():
    data = load_data()
    data_tanaman = load_data_tanaman()

    if not data_tanaman:
        print("\nTidak ada data tanaman. Silakan tambahkan tanaman terlebih dahulu!")
        return

    print("\n=== Tambah Data Jadwal Pengingat Penyiraman dan Pemupukan ===")
    print("\nDaftar Tanaman:")
    print("=" * 70)
    print(f"{'ID':<10} {'Nama Tanaman':<20} {'Jenis Tanaman':<20} {'Lokasi':<20}")
    print("=" * 70)
    for id_tanaman, tanaman in data_tanaman.items():
        print(f"{tanaman['id']:<10} {tanaman['nama_tanaman']:<20} {tanaman['jenis_tanaman']:<20} {tanaman['lokasi_tanaman']:<20}")
    print("-" * 70)

    id_tanaman = input("\nMasukkan ID tanaman yang ingin dijadwalkan: ")
    if id_tanaman not in data_tanaman:
        print("ID tanaman tidak valid!")
        return

    id_jadwal_pengingat = generate_id(data)
    
    while True:
        try:
            waktu_pengingat = input("Masukkan waktu pengingat (HH:MM): ")
            datetime.strptime(waktu_pengingat, "%H:%M")
            break
        except ValueError:
            print("Format waktu tidak valid! Gunakan format HH:MM")

    while True:
        hari_notifikasi = input("Masukkan hari notifikasi (pisahkan dengan koma, misalnya: Senin, Selasa): ").split(",")
        hari_notifikasi = [hari.strip().capitalize() for hari in hari_notifikasi]
        if all(hari in ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"] for hari in hari_notifikasi):
            break
        print("Masukkan hari yang valid!")

    tipe = input("Masukkan tipe pengingat (penyiraman/pemupukan): ").strip().lower()
    while tipe not in ["penyiraman", "pemupukan"]:
        print("Tipe tidak valid! Silakan masukkan 'penyiraman' atau 'pemupukan'.")
        tipe = input("Masukkan tipe pengingat (penyiraman/pemupukan): ").strip().lower()

    data[id_jadwal_pengingat] = {
        "id": id_jadwal_pengingat,
        "id_tanaman": id_tanaman,
        "nama_tanaman": data_tanaman[id_tanaman]["nama_tanaman"],
        "waktu_pengingat": waktu_pengingat,
        "hari_notifikasi": hari_notifikasi,
        "status": "aktif",
        "tipe": tipe
    }

    save_data(data)
    print(f"\nJadwal pengingat {tipe} untuk tanaman {data_tanaman[id_tanaman]['nama_tanaman']} berhasil ditambahkan!")

def read_jadwal_pengingat():
    data = load_data()
    if data:
        print("\n=== Data Jadwal Pengingat Penyiraman dan Pemupukan ===")
        print("=" * 105)
        print(f"{'ID':<10} | {'Nama Tanaman':<20} | {'Waktu Pengingat':<15} | {'Hari Notifikasi':<30} | {'Tipe':<15} | {'Status':<10}")
        print("=" * 105)
        for jadwal_pengingat_id, pengingat in data.items():
            print(f"{pengingat['id']:<10} | {pengingat['nama_tanaman']:<20} | {pengingat['waktu_pengingat']:<15} | {', '.join(pengingat['hari_notifikasi']):<30} | {pengingat['tipe']:<15} | {pengingat['status']:<10}")
        print("-" * 105)
    else:
        print("Tidak ada data jadwal pengingat.")

def update_jadwal_pengingat():
    data = load_data()
    data_tanaman = load_data_tanaman()
    id_jadwal_pengingat = input("Masukkan ID Jadwal Pengingat yang akan diperbarui: ")

    if id_jadwal_pengingat not in data:
        print("Jadwal Pengingat dengan ID tersebut tidak ditemukan.")
        return
    
    print("\n=== Data Jadwal Pengingat Lama ===")
    print("=" * 105)
    print(f"{'ID':<10} | {'Nama Tanaman':<20} | {'Waktu Pengingat':<15} | {'Hari Notifikasi':<30} | {'Tipe':<15} | {'Status':<10}")
    print("=" * 105)
    jadwal = data[id_jadwal_pengingat]
    print(f"{jadwal['id']:<10} | {jadwal['nama_tanaman']:<20} | {jadwal['waktu_pengingat']:<15} | {', '.join(jadwal['hari_notifikasi']):<30} | {jadwal['tipe']:<15} | {jadwal['status']:<10}")
    print("-" * 105)

    print("\nDaftar Tanaman:")
    print("=" * 70)
    print(f"{'ID':<10} | {'Nama Tanaman':<20} | {'Jenis Tanaman':<20} | {'Lokasi':<20}")
    print("=" * 70)
    for id_tanaman, tanaman in data_tanaman.items():
        print(f"{tanaman['id']:<10} | {tanaman['nama_tanaman']:<20} | {tanaman['jenis_tanaman']:<20} | {tanaman['lokasi_tanaman']:<20}")
    print("-" * 70)

    id_tanaman = input("\nMasukkan ID tanaman yang ingin dijadwalkan: ")
    if id_tanaman not in data_tanaman:
        print("ID tanaman tidak valid!")
        return

    print("\n=== Update Data Jadwal Pengingat ===")
    while True:
        try:
            waktu_pengingat = input("Masukkan waktu pengingat (HH:MM): ")
            datetime.strptime(waktu_pengingat, "%H:%M")
            break
        except ValueError:
            print("Format waktu tidak valid! Gunakan format HH:MM")

    while True:
        hari_notifikasi = input("Masukkan hari notifikasi (pisahkan dengan koma, misalnya: Senin, Selasa): ").split(",")
        hari_notifikasi = [hari.strip().capitalize() for hari in hari_notifikasi]
        if all(hari in ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"] for hari in hari_notifikasi):
            break
        print("Masukkan hari yang valid!")

    status = input("Masukkan status (aktif/non-aktif): ").strip().lower()
    while status not in ["aktif", "non-aktif"]:
        print("Status tidak valid! Masukkan 'aktif' atau 'non-aktif'")
        status = input("Masukkan status (aktif/non-aktif): ").strip().lower()

    data[id_jadwal_pengingat].update({
        "id_tanaman": id_tanaman,
        "nama_tanaman": data_tanaman[id_tanaman]["nama_tanaman"],
        "waktu_pengingat": waktu_pengingat,
        "hari_notifikasi": hari_notifikasi,
        "status": status
    })

    save_data(data)
    print("Data Jadwal Pengingat berhasil diperbarui!")

def delete_jadwal_pengingat():
    data = load_data()
    id_jadwal_pengingat = input("Masukkan ID Jadwal Pengingat yang akan dihapus: ")

    if id_jadwal_pengingat in data:
        konfirmasi = input(f"Anda yakin ingin menghapus jadwal pengingat {id_jadwal_pengingat}? (y/n): ").lower()
        if konfirmasi == 'y':
            del data[id_jadwal_pengingat]
            save_data(data)
            print("Jadwal Pengingat berhasil dihapus!")
        else:
            print("Penghapusan dibatalkan.")
    else:
        print("Jadwal Pengingat dengan ID tersebut tidak ditemukan.")

def notifikasi():
    while True:
        data = load_data()
        now = datetime.now()
        hari_sekarang = now.strftime("%A")
        
        # Konversi nama hari ke Bahasa Indonesia
        hari_indo = {
            'Monday': 'Senin',
            'Tuesday': 'Selasa', 
            'Wednesday': 'Rabu',
            'Thursday': 'Kamis',
            'Friday': 'Jumat',
            'Saturday': 'Sabtu',
            'Sunday': 'Minggu'
        }
        
        hari_sekarang = hari_indo[hari_sekarang]
        
        for jadwal in data.values():
            if jadwal['status'] != 'aktif':
                continue
                
            waktu = datetime.strptime(jadwal['waktu_pengingat'], "%H:%M").time()
            if (now.time().hour == waktu.hour and 
                now.time().minute == waktu.minute and 
                hari_sekarang in jadwal['hari_notifikasi']):
                print(f"\n\nNOTIFIKASI: Saatnya melakukan {jadwal['tipe']}!")
                print(f"ID Jadwal: {jadwal['id']}")
                print(f"Tanaman: {jadwal['nama_tanaman']}")
                print(f"Waktu: {waktu.strftime('%H:%M')}")
                print("-" * 50)
                
        time.sleep(20)

def start_notifikasi_thread():
    thread = threading.Thread(target=notifikasi)
    thread.daemon = True
    thread.start()

def menu_jadwal_pengingat():
    from main import main_menu
    start_notifikasi_thread()
    
    while True:
        print("\n=== Menu Jadwal Pengingat Penyiraman dan Pemupukan ===")
        print("1. Tambah Data Jadwal Pengingat")
        print("2. Lihat Data Jadwal Pengingat") 
        print("3. Update Data Jadwal Pengingat")
        print("4. Hapus Data Jadwal Pengingat")
        print("5. Kembali ke Menu Utama")

        pilihan = input("\nPilih menu (1-5): ")

        if pilihan == "1":
            add_jadwal_pengingat()
        elif pilihan == "2":
            read_jadwal_pengingat()
        elif pilihan == "3":
            update_jadwal_pengingat()
        elif pilihan == "4":
            delete_jadwal_pengingat()
        elif pilihan == "5":
            main_menu()
            break
        else:
            print("Pilihan tidak valid! Silakan pilih menu 1-5.")