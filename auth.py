import json
import hashlib
import os
from datetime import datetime


# Nama file JSON untuk menyimpan data pengguna
DATA_FILE = "data/data_pengelola.json"

# Fungsi untuk memuat data dari file JSON
def load_data():
   if os.path.exists(DATA_FILE):

DATA_FILE = "data/data_pengelola.json"

def initialize_data_directory():
   os.makedirs("data", exist_ok=True)

def load_data():
   initialize_data_directory()
   if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:

      with open(DATA_FILE, "r") as file:
         return json.load(file)
   return {}


# Fungsi untuk menyimpan data ke file JSON
def save_data(data):
   with open(DATA_FILE, "w") as file:
      json.dump(data, file, indent=4)

# Fungsi untuk hash password
def hash_password(password):
   return hashlib.sha256(password.encode()).hexdigest()

# Fungsi registrasi
def register():
   data = load_data()
   print("=== Registrasi Pengelola ===")
   id_pengelola = input("ID Pengelola: ")

def save_data(data):
   initialize_data_directory()
   with open(DATA_FILE, "w") as file:
      json.dump(data, file, indent=4)

def hash_password(password):
   return hashlib.sha256(password.encode()).hexdigest()

def generate_user_id(data):
   user_id = f"user{len(data) + 1}"
   while user_id in data:
      user_id = f"user{len(data) + 1}"
   return user_id

def register():
   data = load_data()
   print("\n=== Registrasi Pengelola ===\n")

   nama = input("Nama: ")
   username = input("Username: ")
   email = input("Email: ")
   password = input("Password: ")
   no_telepon = input("Nomor Telepon: ")
   alamat_kebun = input("Alamat Kebun: ")
   tanggal_registrasi = datetime.now().strftime("%Y-%m-%d")


   # Cek apakah email sudah terdaftar

   for user in data.values():
      if user['email'] == email:
         print("Email sudah terdaftar! Gunakan email lain.")
         return


   # Simpan data pengelola baru


   data[id_pengelola] = {
      "id": id_pengelola,
      "nama": nama,
      "username": username,
      "email": email,
      "password": hash_password(password),
      "no_telepon": no_telepon,
      "alamat_kebun": alamat_kebun,
      "tanggal_registrasi": tanggal_registrasi
   }

   save_data(data)
   print("Registrasi berhasil!")


# Fungsi login
def login():
   data = load_data()
   print("=== Login Pengelola ===")
   email = input("Email: ")
   password = input("Password: ")

   # Hash password yang diinputkan
   hashed_password = hash_password(password)

   # Verifikasi email dan password
   for user in data.values():
      if user["email"] == email and user["password"] == hashed_password:
         print("Login berhasil! Selamat datang,", user["nama"])
         return True

   print("Email atau password salah.")
   return False

   print("Silakan login dengan akun baru Anda.")
   login()

def login():
   data = load_data()
   print("\n=== Login Pengelola ===\n")
   while True:
      email = input("Email: ")
      password = input("Password: ")

      hashed_password = hash_password(password)

      for user in data.values():
         if user["email"] == email and user["password"] == hashed_password:
               print("Login berhasil! Selamat datang,", user["nama"])
               return True, user

      print("Email atau password salah. Coba lagi.")
      retry = input("Apakah ingin mencoba login lagi? (y/n): ")
      if retry.lower() != 'y':
         return False, None
 main
