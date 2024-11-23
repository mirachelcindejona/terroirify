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
    nama = input("Nama: ")
    username = input("Username: ")
    email = input("Email: ")
    password = input("Password: ")
    no_telepon = input("Nomor Telepon: ")
    alamat_kebun = input("Alamat Kebun: ")
    id_kebun = input("ID Unik Kebun: ")
    tanggal_registrasi = datetime.now().strftime("%Y-%m-%d")

    for user in data.values():
        if user['email'] == email:
            print("Email sudah terdaftar! Gunakan email lain.")
            return False, None
        elif user['username'] == username:
            print("Username sudah terdaftar! Gunakan username lain.")
            return False, None

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
        email = input("Email: ")
        password = input("Password: ")

        hashed_password = hash_password(password)

        for user in data.values():
            if user["email"] == email and user["password"] == hashed_password:
                print("Login berhasil! Selamat datang,", user["nama"])
                save_login_data(user)
                return True, user

        print("Email atau password salah. Coba lagi.")
        retry = input("Apakah ingin mencoba login lagi? (y/n): ")
        if retry.lower() != 'y':
            return False, None
