import json
from datetime import datetime

DATA_PEKERJA = "data/data_pekerja.json"

def load_data():
    try:
        with open(DATA_PEKERJA, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca data: {str(e)}")
        return {}

def save_data(data):
    try:
        with open(DATA_PEKERJA, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan data: {str(e)}")

def generate_id(data):
    try:
        pekerja_id = f"PKJ0{len(data) + 1}"
        while pekerja_id in data:
            num = int(pekerja_id[3:]) + 1
            pekerja_id = f"PKJ0{num}"
        return pekerja_id
    except Exception as e:
        print(f"Terjadi kesalahan saat generate ID: {str(e)}")
        return None

def get_data_login():
    try:
        with open("data/data_login.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca data login: {str(e)}")
        return {}

def add_pekerja():
    try:
        data = load_data()
        user_login = get_data_login()
        
        if not user_login:
            print("\nAnda harus login terlebih dahulu!")
            return
        
        print("\n=== Tambah Pekerja Baru ===")
        id_pekerja = generate_id(data)
        if not id_pekerja:
            print("Gagal membuat ID pekerja")
            return
            
        id_kebun = user_login.get('id_kebun')
        if not id_kebun:
            print("Data kebun tidak ditemukan!")
            return
        
        while True:
            nama = input("Nama Lengkap: ").strip()
            if not nama:
                print("Error: Nama lengkap tidak boleh kosong!\n")
                continue
            break

        while True:
            email = input("Email: ").strip().lower()
            if not email:
                print("Error: Email tidak boleh kosong!\n")
                continue
            if "@" not in email or "." not in email.split("@")[-1]:
                print("Error: Format email tidak valid!\n")
                continue
            if any(pekerja['email'] == email for pekerja in data.values()):
                print("Email sudah terdaftar! Gunakan email lain.\n")
                continue
            break
        
        while True:
            kontak = input("Kontak: ").strip()
            if not kontak:
                print("Error: Kontak tidak boleh kosong!\n")
                continue 
            try:
                kontak = int(kontak)
                if kontak <= 0:
                    print("Error: Kontak harus berupa angka positif!\n")
                    continue
                break
            except ValueError:
                print("Error: Kontak harus berupa angka!\n")
        
        while True:
            status = input("Status (aktif/non-aktif): ").strip().lower()
            if status not in ["aktif", "non-aktif"]:
                print("Error: Status harus 'aktif' atau 'non-aktif'!\n")
                continue
            break
        
        while True: 
            tanggal_bergabung = input("Tanggal bergabung (YYYY-MM-DD): ").strip()
            if not tanggal_bergabung:
                print("Error: Tanggal bergabung tidak boleh kosong!\n")
                continue
            try:
                datetime.strptime(tanggal_bergabung, "%Y-%m-%d")
                break
            except ValueError:
                print("Error: Pastikan tanggal dalam format yang benar (YYYY-MM-DD).\n")
                continue
        
        while True:
            posisi_jabatan = input("Posisi/Jabatan: ").strip()
            if not posisi_jabatan:
                print("Error: Posisi/Jabatan tidak boleh kosong!\n")
                continue
            break
        
        while True:
            hari_kerja_input = input("Masukkan hari Kerja (pisahkan dengan koma, misalnya: Senin, Selasa): ").strip()
            if not hari_kerja_input:
                print("Error: Hari kerja tidak boleh kosong!\n")
                continue
                
            hari_kerja = [hari.strip().capitalize() for hari in hari_kerja_input.split(",")]
            valid_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
            
            if all(hari in valid_hari for hari in hari_kerja):
                break
            print("Error: Masukkan hari yang valid (Senin-Minggu)!\n")
        
        while True:
            jam_kerja_input = input("Masukkan jam Kerja (format HH:MM - HH:MM): ").strip()
            if not jam_kerja_input:
                print("Error: Jam kerja tidak boleh kosong!\n")
                continue

            try:
                jam_kerja = jam_kerja_input.split(" - ")
                if len(jam_kerja) != 2:
                    print("Error: Format jam tidak valid. Gunakan format HH:MM - HH:MM\n")
                    continue
                
                for jam in jam_kerja:
                    waktu = datetime.strptime(jam.strip(), "%H:%M")
                    if waktu.hour > 23 or waktu.minute > 59:
                        raise ValueError
                break
            except ValueError:
                print("Error: Format waktu tidak valid! Gunakan format HH:MM (00:00-23:59)\n")
        
        data[id_pekerja] = {
            "id_pekerja": id_pekerja,
            "id_kebun": id_kebun,
            "nama": nama,
            "email": email,
            "kontak": kontak,
            "status": status,
            "tanggal_bergabung": tanggal_bergabung,
            "posisi_jabatan": posisi_jabatan,
            "hari_kerja": hari_kerja,
            "jam_kerja": jam_kerja
        }
        
        save_data(data)
        print("\nData pekerja berhasil ditambahkan!")
        
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")

def read_pekerja():
    try:
        data = load_data()
        user_login = get_data_login()
        
        if not user_login:
            print("\nAnda harus login terlebih dahulu!")
            return
            
        if not data:
            print("\nTidak ada data pekerja.")
            return
            
        print("\n=== Data Pekerja ===\n")
        print("=" * 100)
        print(f"{'ID':<10} | {'Lokasi Kebun':<20} | {'Nama':<20} | {'Email':<20} | {'Kontak':<20} | {'Status':<20} | {'Tanggal Bergabung':<20} | {'Posisi/Jabatan':<20} | {'Hari Kerja':<20} | {'Jam Kerja':<20}")
        print("=" * 100)
        
        found = False
        for pekerja in data.values():
            if pekerja['id_kebun'] == user_login['id_kebun']:
                found = True
                print(f"{pekerja['id_pekerja']:<10} | {user_login.get('alamat_kebun', '-'):<20} | {pekerja['nama']:<20} | {pekerja['email']:<20} | {pekerja['kontak']:<20} | {pekerja['status']:<20} | {pekerja['tanggal_bergabung']:<20} | {pekerja['posisi_jabatan']:<20} | {', '.join(pekerja['hari_kerja']):<20} | {' - '.join(pekerja['jam_kerja']):<20}")
                print("-" * 100)
                
        if not found:
            print("\nTidak ada data pekerja untuk kebun ini.")
            
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")

def update_pekerja():
    try:
        data = load_data()
        user_login = get_data_login()
        
        if not user_login:
            print("\nAnda harus login terlebih dahulu!")
            return
            
        id_pekerja = input("\nMasukkan ID pekerja yang akan diperbarui: ").strip()
        
        if id_pekerja not in data:
            print("\nPekerja dengan ID tersebut tidak ditemukan.")
            return
            
        if data[id_pekerja]['id_kebun'] != user_login['id_kebun']:
            print("\nAnda tidak memiliki akses untuk mengubah data pekerja ini!")
            return
        
        print(f"\n=== Data pekerja saat ini dengan ID {id_pekerja} ===")
        print("=" * 100)
        print(f"{'ID':<10} | {'Lokasi Kebun':<20} | {'Nama':<20} | {'Email':<20} | {'Kontak':<20} | {'Status':<20} | {'Tanggal Bergabung':<20} | {'Posisi/Jabatan':<20} | {'Hari Kerja':<20} | {'Jam Kerja':<20}")
        print("=" * 100)
        print(f"{data[id_pekerja]['id_pekerja']:<10} | {user_login.get('alamat_kebun', '-'):<20} | {data[id_pekerja]['nama']:<20} | {data[id_pekerja]['email']:<20} | {data[id_pekerja]['kontak']:<20} | {data[id_pekerja]['status']:<20} | {data[id_pekerja]['tanggal_bergabung']:<20} | {data[id_pekerja]['posisi_jabatan']:<20} | {', '.join(data[id_pekerja]['hari_kerja']):<20} | {' - '.join(data[id_pekerja]['jam_kerja']):<20}")
        print("-" * 100)

        print("\n=== Update Data Pekerja ===")
        print("(Tekan Enter untuk menggunakan data yang ada)\n")
        
        nama = input(f"Nama Lengkap [{data[id_pekerja]['nama']}]: ").strip() or data[id_pekerja]['nama']
        
        while True:
            email = input(f"Email [{data[id_pekerja]['email']}]: ").strip().lower() or data[id_pekerja]['email']
            if email == data[id_pekerja]['email']:
                break
            if "@" not in email or "." not in email.split("@")[-1]:
                print("Error: Format email tidak valid!\n")
                continue
            if any(p['email'] == email and p['id_pekerja'] != id_pekerja for p in data.values()):
                print("Error: Email sudah terdaftar! Gunakan email lain.\n")
                continue
            break
            
        while True:
            kontak_input = input(f"Kontak [{data[id_pekerja]['kontak']}]: ").strip()
            if not kontak_input:
                kontak = data[id_pekerja]['kontak']
                break
            try:
                kontak = int(kontak_input)
                if kontak <= 0:
                    print("Error: Kontak harus berupa angka positif!\n")
                    continue
                break
            except ValueError:
                print("Error: Kontak harus berupa angka!\n")
        
        while True:        
            status = input(f"Status (aktif/non-aktif) [{data[id_pekerja]['status']}]: ").strip().lower() or data[id_pekerja]['status']
            if status not in ["aktif", "non-aktif"]:
                print("Error: Status harus 'aktif' atau 'non-aktif'!\n")
                continue
            break
        
        while True:
            tanggal_input = input(f"Tanggal Bergabung (YYYY-MM-DD) [{data[id_pekerja]['tanggal_bergabung']}]: ").strip()
            if not tanggal_input:
                tanggal_bergabung = data[id_pekerja]['tanggal_bergabung']
                break
            try:
                datetime.strptime(tanggal_input, "%Y-%m-%d")
                tanggal_bergabung = tanggal_input
                break
            except ValueError:
                print("Error: Pastikan tanggal dalam format yang benar (YYYY-MM-DD).\n")
        
        posisi_jabatan = input(f"Posisi/Jabatan [{data[id_pekerja]['posisi_jabatan']}]: ").strip() or data[id_pekerja]['posisi_jabatan']
        
        while True:
            hari_kerja_default = ', '.join(data[id_pekerja]['hari_kerja'])
            hari_kerja_input = input(f"Masukkan hari Kerja (pisahkan dengan koma) [{hari_kerja_default}]: ").strip()
            
            if not hari_kerja_input:
                hari_kerja = data[id_pekerja]['hari_kerja']
                break
                
            hari_kerja = [hari.strip().capitalize() for hari in hari_kerja_input.split(",")]
            valid_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
            
            if all(hari in valid_hari for hari in hari_kerja):
                break
            print("Error: Masukkan hari yang valid (Senin-Minggu)!\n")
        
        while True:
            jam_kerja_default = ' - '.join(data[id_pekerja]['jam_kerja'])
            jam_kerja_input = input(f"Masukkan jam Kerja (HH:MM - HH:MM) [{jam_kerja_default}]: ").strip()
            
            if not jam_kerja_input:
                jam_kerja = data[id_pekerja]['jam_kerja']
                break
                
            try:
                jam_kerja = jam_kerja_input.split(" - ")
                if len(jam_kerja) != 2:
                    print("Error: Format jam tidak valid. Gunakan format HH:MM - HH:MM\n")
                    continue
                
                for jam in jam_kerja:
                    waktu = datetime.strptime(jam.strip(), "%H:%M")
                    if waktu.hour > 23 or waktu.minute > 59:
                        raise ValueError
                break
            except ValueError:
                print("Error: Format waktu tidak valid! Gunakan format HH:MM (00:00-23:59)\n")

        data[id_pekerja].update({
            "nama": nama,
            "email": email,
            "kontak": kontak,
            "status": status,
            "tanggal_bergabung": tanggal_bergabung,
            "posisi_jabatan": posisi_jabatan,
            "hari_kerja": hari_kerja,
            "jam_kerja": jam_kerja
        })
        
        save_data(data)
        print("\nData pekerja berhasil diperbarui!")
        
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")

def delete_pekerja():
    try:
        data = load_data()
        user_login = get_data_login()
        
        if not user_login:
            print("\nAnda harus login terlebih dahulu!")
            return
            
        id_pekerja = input("\nMasukkan ID pekerja yang akan dihapus: ").strip()
        
        if not id_pekerja:
            print("\nID pekerja tidak boleh kosong!")
            return
            
        if id_pekerja not in data:
            print("\nPekerja dengan ID tersebut tidak ditemukan.")
            return
            
        if data[id_pekerja]['id_kebun'] != user_login['id_kebun']:
            print("\nAnda tidak memiliki akses untuk menghapus data pekerja ini!")
            return
        
        while True:
            konfirmasi = input(f"\nAnda yakin ingin menghapus pekerja {data[id_pekerja]['nama']}? (y/n): ").lower()
            if konfirmasi not in ['y', 'n']:
                print("Pilihan tidak valid! Masukkan 'y' untuk ya atau 'n' untuk tidak.")
                continue
            if konfirmasi == 'y':
                del data[id_pekerja]
                save_data(data)
                print("\nPekerja berhasil dihapus!")
            else:
                print("\nPenghapusan dibatalkan.")
            break
            
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")

def menu_pekerja():
    try:
        from main import main_menu
        while True:
            print("\n=== Menu Pekerja ===")
            print("1. Tambah Data Pekerja")
            print("2. Lihat Data Pekerja")
            print("3. Update Data Pekerja")
            print("4. Hapus Data Pekerja")
            print("5. Kembali ke Menu Utama")
            
            pilihan = input("\nPilih menu (1-5): ").strip()
            
            if pilihan == "1":
                add_pekerja()
            elif pilihan == "2":
                read_pekerja()
            elif pilihan == "3":
                update_pekerja()
            elif pilihan == "4":
                delete_pekerja()
            elif pilihan == "5":
                main_menu()
                break
            else:
                print("\nPilihan tidak valid! Silakan pilih menu 1-5.")
                
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")
        main_menu()
