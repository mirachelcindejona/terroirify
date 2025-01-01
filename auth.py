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

def save_data(data):
    with open(DATA_PENGELOLA, "w") as file:
        json.dump(data, file, indent=4)

def save_login_data(user_data):
    with open(DATA_LOGIN, "w") as file:
        json.dump(user_data, file, indent=4)

def clear_login_data():
    with open(DATA_LOGIN, "w") as file:
        json.dump({}, file, indent=4)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def generate_user_id(data):
    id_pengelola = f"PNGL0{len(data) + 1}"
    while id_pengelola in data:
        id_pengelola = f"PNGL0{len(data) + 1}"
    return id_pengelola

def register():
    data = load_data()
    print("\n=== Registrasi Pengelola ===")
    id_pengelola = generate_user_id(data)
    
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

    data[id_pengelola] = {
        "id_pengelola": id_pengelola,
        "nama": nama,
        "username": username,
        "email": email,
        "password": hash_password(password),
        "no_telepon": no_telepon,
        "alamat_kebun": alamat_kebun,
        "id_kebun": id_kebun,
        "tanggal_registrasi": tanggal_registrasi
    }

    save_data(data)
    print("Registrasi berhasil!")
    print("Silakan login dengan akun baru Anda.")
    return True, None

def login():
    data = load_data()
    print("\n=== Login Pengelola ===")
    while True:
        email = input("\nEmail: ")
        password = input("Password: ")

        hashed_password = hash_password(password)

        for user in data.values():
            if user["email"] == email and user["password"] == hashed_password:
                print("\n🌱 Login berhasil! Selamat datang,", user["nama"], "🌱")
                save_login_data(user)
                return True, user

        print("Email atau password salah. Coba lagi.\n")
        retry = input("Apakah ingin mencoba login lagi? (y/n): ")
        if retry.lower() != 'y':
            return False, None
