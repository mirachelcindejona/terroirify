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
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca data: {str(e)}")
        return {}

def save_data(data):
    try:
        with open(DATA_JADWAL_PENGINGAT, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan data: {str(e)}")

def generate_id(data):
    try:
        counter = 1
        while True:
            jadwal_pengingat_id = f"JP{counter:02d}"
            if jadwal_pengingat_id not in data:
                return jadwal_pengingat_id
            counter += 1
    except Exception as e:
        print(f"Error saat generate ID: {str(e)}")
        return None

def add_jadwal_pengingat():
    try:
        data = load_data()
        data_tanaman = load_data_tanaman()

        if not data_tanaman:
            print("\nTidak ada data tanaman. Silakan tambahkan tanaman terlebih dahulu!")
            return

        print("\n=== Tambah Data Jadwal Pengingat Penyiraman dan Pemupukan ===")
        print("\nDaftar Tanaman:")
        print("=" * 80)
        print(f"{'ID':<10} | {'Nama Tanaman':<25} | {'Jenis Tanaman':<25} | {'Lokasi':<25}")
        print("=" * 80)
        for id_tanaman, tanaman in data_tanaman.items():
            print(f"{tanaman['id']:<10} | {tanaman['nama_tanaman']:<25} | {tanaman['jenis_tanaman']:<25} | {tanaman['lokasi_tanaman']:<25}")
        print("-" * 80)

        while True:
            id_tanaman = input("\nMasukkan ID tanaman yang ingin dijadwalkan: ").strip()
            if not id_tanaman:
                print("Error: ID tanaman tidak boleh kosong!")
                continue
            if id_tanaman not in data_tanaman:
                print("Error: ID tanaman tidak valid!")
                continue
            break

        id_jadwal_pengingat = generate_id(data)
        if not id_jadwal_pengingat:
            return
        
        while True:
            try:
                waktu_pengingat = input("Masukkan waktu pengingat (HH:MM): ").strip()
                if not waktu_pengingat:
                    print("Error: Waktu pengingat tidak boleh kosong!")
                    continue
                datetime.strptime(waktu_pengingat, "%H:%M")
                break
            except ValueError:
                print("Error: Format waktu tidak valid! Gunakan format HH:MM\n")

        while True:
            hari_input = input("Masukkan hari notifikasi (pisahkan dengan koma, misalnya: Senin, Selasa): ").strip()
            if not hari_input:
                print("Error: Hari notifikasi tidak boleh kosong!")
                continue
                
            hari_notifikasi = [hari.strip().capitalize() for hari in hari_input.split(",")]
            valid_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
            
            if all(hari in valid_hari for hari in hari_notifikasi):
                break
            print("Error: Masukkan hari yang valid!\n")

        while True:
            tipe = input("Masukkan tipe pengingat (penyiraman/pemupukan): ").strip().lower()
            if not tipe:
                print("Error: Tipe pengingat tidak boleh kosong!")
                continue
            if tipe not in ["penyiraman", "pemupukan"]:
                print("Error: Tipe tidak valid! Silakan masukkan 'penyiraman' atau 'pemupukan'.\n")
                continue
            break

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
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")

def read_jadwal_pengingat():
    try:
        data = load_data()
        if data:
            print("\n=== Data Jadwal Pengingat Penyiraman dan Pemupukan ===\n")
            print("=" * 120)
            print(f"{'ID':<10} | {'Nama Tanaman':<25} | {'Waktu Pengingat':<20} | {'Hari Notifikasi':<35} | {'Tipe':<20} | {'Status':<15}")
            print("=" * 120)
            for jadwal_pengingat_id, pengingat in data.items():
                print(f"{pengingat['id']:<10} | {pengingat['nama_tanaman']:<25} | {pengingat['waktu_pengingat']:<20} | {', '.join(pengingat['hari_notifikasi']):<35} | {pengingat['tipe']:<20} | {pengingat['status']:<15}")
            print("-" * 120)
        else:
            print("Tidak ada data jadwal pengingat.")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")

def update_jadwal_pengingat():
    try:
        data = load_data()
        data_tanaman = load_data_tanaman()
        
        while True:
            id_jadwal_pengingat = input("\nMasukkan ID Jadwal Pengingat yang akan diperbarui: ").strip()
            if not id_jadwal_pengingat:
                print("Error: ID jadwal pengingat tidak boleh kosong!")
                continue
            if id_jadwal_pengingat not in data:
                print("Jadwal Pengingat dengan ID tersebut tidak ditemukan.\n")
                return
            break

        print(f"\n=== Data jadwal pengingat saat ini dengan ID {id_jadwal_pengingat} ===\n")
        print("=" * 120)
        print(f"{'ID':<10} | {'Nama Tanaman':<25} | {'Waktu Pengingat':<20} | {'Hari Notifikasi':<35} | {'Tipe':<20} | {'Status':<15}")
        print("=" * 120)
        jadwal = data[id_jadwal_pengingat]
        print(f"{jadwal['id']:<10} | {jadwal['nama_tanaman']:<25} | {jadwal['waktu_pengingat']:<20} | {', '.join(jadwal['hari_notifikasi']):<35} | {jadwal['tipe']:<20} | {jadwal['status']:<15}")
        print("-" * 120)

        print("\n=== Update Data Jadwal Pengingat ===\n(Tidak perlu diisi jika tidak ingin diubah)")

        print("\nDaftar Tanaman:")
        print("=" * 80)
        print(f"{'ID':<10} | {'Nama Tanaman':<25} | {'Jenis Tanaman':<25} | {'Lokasi':<25}")
        print("=" * 80)
        for id_tanaman, tanaman in data_tanaman.items():
            print(f"{tanaman['id']:<10} | {tanaman['nama_tanaman']:<25} | {tanaman['jenis_tanaman']:<25} | {tanaman['lokasi_tanaman']:<25}")
        print("-" * 80)

        while True:
            id_tanaman = input(f"\nMasukkan ID tanaman yang ingin dijadwalkan [{data[id_jadwal_pengingat]['id_tanaman']}]: ").strip() or data[id_jadwal_pengingat]['id_tanaman']
            if id_tanaman not in data_tanaman:
                print("Error: ID tanaman tidak valid!")
                continue
            break

        while True:
            try:
                waktu_pengingat = input(f"Masukkan waktu pengingat (HH:MM) [{data[id_jadwal_pengingat]['waktu_pengingat']}]: ").strip() or data[id_jadwal_pengingat]['waktu_pengingat']
                datetime.strptime(waktu_pengingat, "%H:%M")
                break
            except ValueError:
                print("Error: Format waktu tidak valid! Gunakan format HH:MM\n")

        while True:
            hari_default = ', '.join(data[id_jadwal_pengingat]['hari_notifikasi'])
            hari_input = input(f"Masukkan hari notifikasi (pisahkan dengan koma) [{hari_default}]: ").strip()

            if not hari_input:
                hari_notifikasi = data[id_jadwal_pengingat]['hari_notifikasi']
                break
                
            hari_notifikasi = [hari.strip().capitalize() for hari in hari_input.split(",")]
            valid_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
            
            if all(hari in valid_hari for hari in hari_notifikasi):
                break
            print("Error: Masukkan hari yang valid!\n")

        while True:
            status = input(f"Masukkan status (aktif/non-aktif) [{data[id_jadwal_pengingat]['status']}]: ").strip().lower() or data[id_jadwal_pengingat]['status']
            if status not in ["aktif", "non-aktif"]:
                print("Error: Status tidak valid! Masukkan 'aktif' atau 'non-aktif'.\n")
                continue
            break

        data[id_jadwal_pengingat].update({
            "id_tanaman": id_tanaman,
            "nama_tanaman": data_tanaman[id_tanaman]["nama_tanaman"],
            "waktu_pengingat": waktu_pengingat,
            "hari_notifikasi": hari_notifikasi,
            "status": status
        })

        save_data(data)
        print("\nData Jadwal Pengingat berhasil diperbarui!")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")

def delete_jadwal_pengingat():
    try:
        data = load_data()
        while True:
            id_jadwal_pengingat = input("\nMasukkan ID Jadwal Pengingat yang akan dihapus: ").strip()
            if not id_jadwal_pengingat:
                print("Error: ID jadwal pengingat tidak boleh kosong!")
                continue
            if id_jadwal_pengingat not in data:
                print("Jadwal Pengingat dengan ID tersebut tidak ditemukan.\n")
                return
            break

        while True:
            konfirmasi = input(f"Anda yakin ingin menghapus jadwal pengingat {id_jadwal_pengingat}? (y/n): ").lower()
            if konfirmasi not in ['y', 'n']:
                print("Pilihan tidak valid! Masukkan 'y' untuk ya atau 'n' untuk tidak.\n")
                continue
            if konfirmasi == 'y':
                del data[id_jadwal_pengingat]
                save_data(data)
                print("Jadwal Pengingat berhasil dihapus!")
            else:
                print("Penghapusan dibatalkan.")
            break
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")

def notifikasi():
    while True:
        try:
            data = load_data()
            now = datetime.now()
            hari_sekarang = now.strftime("%A")
            
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
        except Exception as e:
            print(f"Terjadi kesalahan pada notifikasi: {str(e)}")
            time.sleep(20)
            continue

def start_notifikasi_thread():
    try:
        thread = threading.Thread(target=notifikasi)
        thread.daemon = True
        thread.start()
    except Exception as e:
        print(f"Terjadi kesalahan saat memulai thread notifikasi: {str(e)}")

def menu_jadwal_pengingat():
    from main import main_menu
    try:
        start_notifikasi_thread()
        
        while True:
            print("\n=== Menu Jadwal Pengingat Penyiraman dan Pemupukan ===")
            print("1. Tambah Data Jadwal Pengingat")
            print("2. Lihat Data Jadwal Pengingat") 
            print("3. Update Data Jadwal Pengingat")
            print("4. Hapus Data Jadwal Pengingat")
            print("5. Kembali ke Menu Utama")

            pilihan = input("\nPilih menu (1-5): ").strip()

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
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")
        main_menu()