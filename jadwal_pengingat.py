import json
from datetime import datetime, timedelta
import time
import threading

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
    jadwal_pengingat_id = f"JP0{len(data) + 1}"
    while jadwal_pengingat_id in data:
        jadwal_pengingat_id = f"JP0{len(data) + 1}"
    return jadwal_pengingat_id

def add_jadwal_pengingat():
    data = load_data()

    print("\n=== Tambah Data Jadwal Pengingat Penyiraman dan Pemupukan ===")
    id_jadwal_pengingat = generate_id(data)
    waktu_pengingat = input("Masukkan waktu pengingat (HH:MM): ")
    frekuensi_hari = int(input("Masukkan frekuensi pengingat (dalam hari): "))

    data[id_jadwal_pengingat] = {
        "id": id_jadwal_pengingat,
        "waktu_pengingat": waktu_pengingat,
        "frekuensi_hari": frekuensi_hari,
        "status": "aktif"
    }

    save_data(data)
    print("Jadwal pengingat berhasil ditambahkan!")

def read_jadwal_pengingat():
    data = load_data()
    if data:
        print("\n=== Data Jadwal Pengingat Penyiraman dan Pemupukan ===")
        print(f"{'ID':<10} | {'Waktu Pengingat':<15} | {'Frekuensi (hari)':<20}")
        print("=" * 50)
        for jadwal_pengingat_id, pengingat in data.items():
            print(f"{pengingat['id']:<10} | {pengingat['waktu_pengingat']:<15} | {pengingat['frekuensi_hari']:<20}")
        print("-" * 50)
    else:
        print("Tidak ada data jadwal pengingat.")

def update_jadwal_pengingat():
    data = load_data()
    id_jadwal_pengingat = input("Masukkan ID Jadwal Pengingat yang akan diperbarui: ")

    if id_jadwal_pengingat not in data:
        print("Jadwal Pengingat dengan ID tersebut tidak ditemukan.")
        return
    
    print("\n=== Data Jadwal Pengingat Penyiraman dan Pemupukan Lama ===")
    print(f"{'ID':<10} | {'Waktu Pengingat':<15} | {'Frekuensi (hari)':<20}")
    print("=" * 50)
    print(f"{data[id_jadwal_pengingat]['id']:<10} | {data[id_jadwal_pengingat]['waktu_pengingat']:<15} | {data[id_jadwal_pengingat]['frekuensi_hari']:<20}")
    print("-" * 50)

    print("\n=== Update Data Jadwal Pengingat ===")
    waktu_pengingat = input("Masukkan waktu pengingat (HH:MM): ")
    frekuensi_hari = int(input("Masukkan frekuensi pengingat (dalam hari): "))

    data[id_jadwal_pengingat] = {
        "id": id_jadwal_pengingat,
        "waktu_pengingat": waktu_pengingat,
        "frekuensi_hari": frekuensi_hari,
        "status": "aktif"
    }

    save_data(data)
    print("Data Jadwal Pengingat berhasil diperbarui!")

def delete_jadwal_pengingat():
    data = load_data()
    id_jadwal_pengingat = input("Masukkan ID Jadwal Pengingat yang akan dihapus: ")

    if id_jadwal_pengingat in data:
        del data[id_jadwal_pengingat]
        save_data(data)
        print("Jadwal Pengingat berhasil dihapus!")
    else:
        print("Jadwal Pengingat dengan ID tersebut tidak ditemukan.")

def notifikasi():
    data = load_data()
    while True:
        now = datetime.now()
        for jadwal in data.values():
            waktu = datetime.strptime(jadwal['waktu_pengingat'], "%H:%M").time()
            if now.time() >= waktu and (now - datetime.now()).days % jadwal['frekuensi_hari'] == 0:
                print(f"Notifikasi: Saatnya melakukan penyiraman dan pemupukan! (ID: {jadwal['id']})")
        time.sleep(60)  # Cek setiap menit

def start_notifikasi_thread():
    thread = threading.Thread(target=notifikasi)
    thread.daemon = True  # Set thread sebagai daemon
    thread.start()

def menu_jadwal_pengingat():
    from main import main_menu
    start_notifikasi_thread()  # Mulai notifikasi saat menu dibuka
    while True:
        print("\n=== Menu Jadwal Pengingat Penyiraman dan Pemupukan ===")
        print("1. Tambah Data Jadwal Pengingat")
        print("2. Lihat Data Jadwal Pengingat")
        print("3. Update Data Jadwal Pengingat")
        print("4. Hapus Data Jadwal Pengingat")
        print("5. Kembali ke Awal")

        pilihan = input("Pilih menu: ")

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
        else:
            print("Pilihan tidak valid. Silahkan pilih lagi.")