import json
from datetime import datetime

DATA_PEKERJA = "data/data_pekerja.json"

def load_data():
    try:
        with open(DATA_PEKERJA, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_data(data):
    with open(DATA_PEKERJA, "w") as file:
        json.dump(data, file, indent=4)

def generate_id(data):
    pekerja_id = f"PKJ0{len(data) + 1}"
    while pekerja_id in data:
        pekerja_id = f"PKJ0{len(data) + 1}"
    return pekerja_id

def get_data_login():
    try:
        with open("data/data_login.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def add_pekerja():
    data = load_data()
    user_login = get_data_login()
    
    print("\n=== Tambah Pekerja Baru ===")
    id_pekerja = generate_id(data)
    id_kebun = user_login['id_kebun']
    
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
        break
    for pekerja in data.values():
        if pekerja['email'] == email:
            print("Email sudah terdaftar! Gunakan email lain.\n")
            return
    
    while True:
        kontak = input("Kontak: ").strip()
        if not kontak:
            print("Error: Kontak tidak boleh kosong!\n")
            continue 
        try:
            kontak = int(kontak)
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
        else:
            try:
                datetime.strptime(tanggal_bergabung, "%Y-%m-%d")
            except ValueError:
                print("Error: Pastikan tanggal dalam format yang benar.\n")
                continue
            break
    
    while True:
        posisi_jabatan = input("Posisi/Jabatan: ").strip()
        if not posisi_jabatan:
            print("Error: Posisi/Jabatan tidak boleh kosong!\n")
            continue
        break
    
    while True:
        if id_pekerja in data:
            hari_kerja_default = '_ '.join([id_pekerja, 'hari_kerja'])
        else:
            hari_kerja_default = " "
            
        hari_kerja = input(f"Masukkan hari Kerja (pisahkan dengan koma, misalnya: Senin, Selasa) [{hari_kerja_default}]: ").split(",") or (data[id_pekerja]['hari_kerja'] if id_pekerja in data else [])
        hari_kerja = [hari.strip().capitalize() for hari in hari_kerja]        
        
        if all(hari in ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"] for hari in hari_kerja):
            break
        print("Masukkan hari yang valid!\n")
    
    while True:
        if id_pekerja in data:
            jam_kerja_default = ' - '.join(data[id_pekerja]['jam_kerja'])
        else:
            jam_kerja_default = ""

        jam_kerja_input = input(f"Masukkan jam Kerja (format HH:MM - HH:MM) [{jam_kerja_default}]: ").strip()

        if not jam_kerja_input and jam_kerja_default:
            jam_kerja = jam_kerja_default.split(" - ")
            break

        jam_kerja = jam_kerja_input.split(" - ")

        try:
            if len(jam_kerja) != 2:
                print("Error: Format jam tidak valid. Gunakan format HH:MM - HH:MM.")
                continue
            
            for jam in jam_kerja:
                datetime.strptime(jam.strip(), "%H:%M")
            break
        except ValueError:
            print("Error: Format waktu tidak valid! Gunakan format HH:MM\n")
    
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
    print("Data pekerja berhasil ditambahkan!")

def read_pekerja():
    data = load_data()
    user_login = get_data_login()
    if data:
        print("\n=== Data Pekerja ===\n")
        print("=" * 100)
        print(f"{'ID':<10} | {'Lokasi Kebun':<20} | {'Nama':<20} | {'Email':<20} | {'Kontak':<20} | {'Status':<20} | {'Tanggal Bergabung':<20} | {'Posisi/Jabatan':<20} | ""{'Hari Kerja':<20} | {'Jam Kerja':<20}""")
        print("=" * 100)
        for pekerja_id, pekerja in data.items():
            if pekerja['id_kebun'] == user_login['id_kebun']:
                print(f"{pekerja['id_pekerja']:<10} | {user_login['alamat_kebun']:<20} | {pekerja['nama']:<20} | {pekerja['email']:<20} | {pekerja['kontak']:<20} | {pekerja['status']:<20} | {pekerja['tanggal_bergabung']:<20} | {pekerja['posisi_jabatan']:<20} | ""{', '.join(pekerja['hari_kerja']):<20} | {pekerja['jam_kerja']:<20}""")
                print("-" * 100)
    else:
        print("Tidak ada data pekerja.")

def update_pekerja():
    data = load_data()
    user_login = get_data_login()
        
    id_pekerja = input("Masukkan ID pekerja yang akan diperbarui: ").strip()
    
    if id_pekerja not in data:
        print("Pekerja dengan ID tersebut tidak ditemukan.")
        return
        
    if data[id_pekerja]['id_kebun'] != user_login['id_kebun']:
        print("Anda tidak memiliki akses untuk mengubah data pekerja ini!")
        return
    
    print(f"\n=== Data pekerja saat ini dengan ID {id_pekerja} ===")
    print("=" * 100)
    print(f"{'ID':<10} | {'Lokasi Kebun':<20} | {'Nama':<20} | {'Email':<20} | {'Kontak':<20} | {'Status':<20} | {'Tanggal Bergabung':<20} | {'Posisi/Jabatan':<20} | ""{'Hari Kerja':<20} | {'Jam Kerja':<20}""")
    print("=" * 100)
    print(f"{data[id_pekerja]['id_pekerja']:<10} | {user_login['alamat_kebun']:<20} | {data[id_pekerja]['nama']:<20} | {data[id_pekerja]['email']:<20} | {data[id_pekerja]['kontak']:<20} | {data[id_pekerja]['status']:<20} | {data[id_pekerja]['tanggal_bergabung']:<20} | {data[id_pekerja]['posisi_jabatan']:<20} | ""{', '.join(data[id_pekerja]['hari_kerja']):<20} | {data[id_pekerja]['jam_kerja']:<20}""")
    print("-" * 100)

    print(f"\n=== Update Data Pekerja ===\n(Tidak perlu diisi jika tidak ingin diubah)")
    nama = input(f"Nama Lengkap [{data[id_pekerja]['nama']}]: ").strip().lower() or data[id_pekerja]['nama']
    
    while True:
        email = input(f"Email [{data[id_pekerja]['email']}]: ").strip().lower() or data[id_pekerja]['email']
        if email == data[id_pekerja]['email']:
            break
        if "@" not in email or "." not in email.split("@")[-1]:
            print("Error: Format email tidak valid!\n")
            continue
    
    for pekerja in data.values():
        if email: 
            if pekerja['email'] == email and pekerja['id_pekerja'] != id_pekerja:
                print("Email sudah terdaftar! Gunakan email lain.\n")
                return
        break
        
    while True:
        kontak = input(f"Kontak [{data[id_pekerja]['kontak']}]: ").strip() or data[id_pekerja]['kontak']
        try:
            kontak = int(kontak)
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
      tanggal_bergabung = input(f"Tanggal Bergabung (YYYY-MM-DD) [{data[id_pekerja]['tanggal_bergabung']}]: ").strip() or data[id_pekerja]['tanggal_bergabung']
      try:
         datetime.strptime(tanggal_bergabung, "%Y-%m-%d")
      except ValueError:
         print("Error:  Pastikan tanggal bergabung dalam format yang benar.\n")
         continue
      break
    
    posisi_jabatan = input(f"Posisi/Jabatan [{data[id_pekerja]['posisi_jabatan']}]: ") or data[id_pekerja]['posisi_jabatan']
   
    while True:
        hari_kerja_default = ', '.join(data[id_pekerja]['hari_kerja'])
        hari_kerja_input = input(f"Masukkan hari Kerja (pisahkan dengan koma, misalnya: Senin, Selasa) [{hari_kerja_default}]: ").strip()
 
        if not hari_kerja_input:
            hari_kerja = data[id_pekerja]['hari_kerja']
            break

        hari_kerja = [hari.strip().capitalize() for hari in hari_kerja_input.split(",")]

        if all(hari in ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"] for hari in hari_kerja):
            break
        else:
            print("Masukkan hari yang valid!\n")
    
    while True:
        if id_pekerja in data:
            jam_kerja_default = ' - '.join(data[id_pekerja]['jam_kerja'])
        else:
            jam_kerja_default = ""

        jam_kerja_input = input(f"Masukkan jam Kerja (format HH:MM - HH:MM) [{jam_kerja_default}]: ").strip()

        if not jam_kerja_input and jam_kerja_default:
            jam_kerja = jam_kerja_default.split(" - ")
            break

        jam_kerja = jam_kerja_input.split(" - ")

        try:
            if len(jam_kerja) != 2:
                print("Error: Format jam tidak valid. Gunakan format HH:MM - HH:MM.")
                continue
            
            for jam in jam_kerja:
                datetime.strptime(jam.strip(), "%H:%M")
            break
        except ValueError:
            print("Error: Format waktu tidak valid! Gunakan format HH:MM\n")
            
    for pid, pekerja in data.items():
        if pekerja['email'] == email and pid != id_pekerja:
            print("Email sudah terdaftar! Gunakan email lain.")
            return

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

def delete_pekerja():
    data = load_data()
    user_login = get_data_login()
        
    id_pekerja = input("\nMasukkan ID pekerja yang akan dihapus: ")
    
    if id_pekerja not in data:
        print("Pekerja dengan ID tersebut tidak ditemukan.")
        return
        
    if data[id_pekerja]['id_kebun'] != user_login['id_kebun']:
        print("\nAnda tidak memiliki akses untuk menghapus data pekerja ini!")
        return
    
    konfirmasi = input(f"Anda yakin ingin menghapus pekerja {data[id_pekerja]['nama']}? (y/n): ")
    if konfirmasi.lower() == 'y':
        del data[id_pekerja]
        save_data(data)
        print("Pekerja berhasil dihapus!")
    else:
        print("Penghapusan dibatalkan.")

def menu_pekerja():
    from main import main_menu
    while True:
        print("\n=== Menu Pekerja ===")
        print("1. Tambah Data Pekerja")
        print("2. Lihat Data Pekerja")
        print("3. Update Data Pekerja")
        print("4. Hapus Data Pekerja")
        print("5. Kembali ke Awal")
        
        pilihan = input("Pilih menu: ")
        
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
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")
