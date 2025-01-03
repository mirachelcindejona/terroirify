import json
import hashlib
from datetime import datetime

DATA_PENGELOLA = "data/data_pengelola.json"
DATA_LOGIN = "data/data_login.json"

def load_data():
    try:
        with open(DATA_PENGELOLA, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca data: {str(e)}")
        return {}

def save_data(data):
    try:
        with open(DATA_PENGELOLA, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan data: {str(e)}")

def save_login_data(user_data):
    try:
        with open(DATA_LOGIN, "w") as file:
            json.dump(user_data, file, indent=4)
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan data login: {str(e)}")

def clear_login_data():
    try:
        with open(DATA_LOGIN, "w") as file:
            json.dump({}, file, indent=4)
    except Exception as e:
        print(f"Terjadi kesalahan saat menghapus data login: {str(e)}")

def hash_password(password):
    try:
        return hashlib.sha256(password.encode()).hexdigest()
    except Exception as e:
        print(f"Terjadi kesalahan saat mengenkripsi password: {str(e)}")
        return None

def generate_user_id(data):
    try:
        counter = 1
        while True:
            id_pengelola = f"PNGL{counter:02d}"
            if id_pengelola not in data:
                return id_pengelola
            counter += 1
    except Exception as e:
        print(f"Error saat generate ID: {str(e)}")
        return None

def register():
    try:
        data = load_data()
        print("\n=== Registrasi Pengelola ===")
        id_pengelola = generate_user_id(data)
        
        if not id_pengelola:
            print("Gagal membuat ID pengelola!")
            return False, None
        
        while True:
            nama = input("Nama: ").strip()
            if not nama:
                print("Error: Nama tidak boleh kosong!\n")
                continue
            break
            
        while True:
            username = input("Username: ").strip()
            if not username:
                print("Error: Username tidak boleh kosong!\n") 
                continue
            if any(user['username'] == username for user in data.values()):
                print("Error: Username sudah terdaftar! Gunakan username lain.\n")
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
            if any(user['email'] == email for user in data.values()):
                print("Error: Email sudah terdaftar! Gunakan email lain.\n")
                continue
            break
            
        while True:
            password = input("Password: ").strip()
            if not password:
                print("Error: Password tidak boleh kosong!\n")
                continue
            if len(password) < 6:
                print("Error: Password minimal 6 karakter!\n")
                continue
            break
            
        while True:
            no_telepon = input("Nomor Telepon: ").strip()
            if not no_telepon:
                print("Error: Nomor telepon tidak boleh kosong!\n")
                continue
            if not no_telepon.isdigit():
                print("Error: Nomor telepon harus berupa angka!\n")
                continue
            break
            
        while True:
            alamat_kebun = input("Alamat Kebun: ").strip()
            if not alamat_kebun:
                print("Error: Alamat kebun tidak boleh kosong!\n")
                continue
            break
            
        while True:
            id_kebun = input("ID Unik Kebun: ").strip()
            if not id_kebun:
                print("Error: ID kebun tidak boleh kosong!\n")
                continue
            if any(user['id_kebun'] == id_kebun for user in data.values()):
                print("Error: ID kebun sudah terdaftar! Gunakan ID lain.\n")
                continue
            break

        tanggal_registrasi = datetime.now().strftime("%Y-%m-%d")
        hashed_password = hash_password(password)
        
        if not hashed_password:
            print("Gagal mengenkripsi password!")
            return False, None

        data[id_pengelola] = {
            "id_pengelola": id_pengelola,
            "nama": nama,
            "username": username,
            "email": email,
            "password": hashed_password,
            "no_telepon": no_telepon,
            "alamat_kebun": alamat_kebun,
            "id_kebun": id_kebun,
            "tanggal_registrasi": tanggal_registrasi
        }

        save_data(data)
        print("Registrasi berhasil!")
        print("Silakan login dengan akun baru Anda.")
        return True, None
        
    except Exception as e:
        print(f"Terjadi kesalahan saat registrasi: {str(e)}")
        return False, None

def login():
    try:
        data = load_data()
        print("\n=== Login Pengelola ===")
        while True:
            email = input("\nEmail: ")
            password = input("Password: ")

            hashed_password = hash_password(password)
            if not hashed_password:
                print("Gagal memverifikasi password!")
                return False, None

            for user in data.values():
                if user["email"] == email and user["password"] == hashed_password:
                    print("\n🌱 Login berhasil! Selamat datang,", user["nama"], "🌱")
                    save_login_data(user)
                    return True, user

            print("Email atau password salah. Coba lagi.\n")
            retry = input("Apakah ingin mencoba login lagi? (y/n): ")
            if retry.lower() != 'y':
                return False, None
                
    except Exception as e:
        print(f"Terjadi kesalahan saat login: {str(e)}")
        return False, None
