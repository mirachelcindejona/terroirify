import json
from datetime import datetime

DATA_TANAMAN = "data/data_tanaman.json"

def load_data():
   try:
      with open(DATA_TANAMAN, "r") as file:
         return json.load(file)
   except (FileNotFoundError, json.JSONDecodeError):
      return {}

def save_data(data):
   with open(DATA_TANAMAN, "w") as file:
      json.dump(data, file, indent=4)

def generate_id(data):
   id_tanaman = f"TNMN0{len(data) + 1}"
   while id_tanaman in data:
      id_tanaman = f"TNMN0{len(data) + 1}"
   return id_tanaman

def add_tanaman():
   data = load_data()
   
   print("\n=== Tambah Tanaman Baru ===")
   id_tanaman = generate_id(data)
   nama_tanaman = input("Masukkan Nama Tanaman: ")
   jenis_tanaman = input("Masukkan Jenis Tanaman: ")
   tanggal_tanam = input("Tanggal Tanam (YYYY-MM-DD): ")
   kondisi_tanaman = input("Kondisi Tanaman: ")
   lokasi_tanaman = input("Lokasi Tanaman: ")

   try:
      datetime.strptime(tanggal_tanam, "%Y-%m-%d")
   except ValueError:
      print("Error: Input tidak valid. Pastikan jumlah stok adalah angka dan tanggal dalam format yang benar.")
      return

   data[id_tanaman] = {
      "id": id_tanaman,
      "nama_tanaman": nama_tanaman,
      "jenis_tanaman": jenis_tanaman,
      "tanggal_tanam": tanggal_tanam,
      "kondisi_tanaman": kondisi_tanaman,
      "lokasi_tanaman": lokasi_tanaman
   }
   
   save_data(data)
   print("Data tanaman berhasil ditambahkan!")

def read_tanaman():
   data = load_data()
   if data:
      print("\n=== Data Tanaman ===")
      for id_tanaman, tanaman in data.items():
         print(f"ID: {tanaman['id']}")
         print(f"Nama Tanaman: {tanaman['nama_tanaman']}")
         print(f"Jenis Tanaman: {tanaman['jenis_tanaman']}")
         print(f"Tanggal Tanam: {tanaman['tanggal_tanam']}")
         print(f"Kondisi Tanaman: {tanaman['kondisi_tanaman']}")
         print(f"Lokasi Tanaman: {tanaman['lokasi_tanaman']}")
         print("-" * 30)
   else:
      print("Tidak ada data tanaman.")

def update_tanaman():
   data = load_data()
   id_tanaman = input("Masukkan ID tanaman yang akan diperbarui: ")
   
   if id_tanaman not in data:
      print("Tanaman dengan ID tersebut tidak ditemukan.")
      return
      
   print("\n=== Update Data Tanaman ===")
   nama_tanaman = input("Nama Tanaman: ")
   jenis_tanaman = input("Jenis Tanaman: ")
   tanggal_tanam = input("Tanggal Tanam (YYYY-MM-DD): ")
   kondisi_tanaman = input("Kondisi Tanaman: ")
   lokasi_tanaman = input("Lokasi Tanaman: ")

   try:
      datetime.strptime(tanggal_tanam, "%Y-%m-%d")
   except ValueError:
      print("Error: Input tidak valid. Pastikan tanggal tanam dalam format yang benar.")
      return

   data[id_tanaman] = {
      "id": id_tanaman,
      "nama_tanaman": nama_tanaman,
      "jenis_tanaman": jenis_tanaman,
      "tanggal_tanam": tanggal_tanam,
      "kondisi_tanaman": kondisi_tanaman,
      "lokasi_tanaman": lokasi_tanaman
   }
   
   save_data(data)
   print("Data tanaman berhasil diperbarui!")

def delete_tanaman():
   data = load_data()
   id_tanaman = input("Masukkan ID tanaman yang akan dihapus: ")
   
   if id_tanaman in data:
      del data[id_tanaman]
      save_data(data)
      print("Tanaman berhasil dihapus!")
   else:
      print("Tanaman dengan ID tersebut tidak ditemukan.")

def menu_tanaman():
   from main import main_menu
   while True:
      print("\n=== Menu Tanaman ===")
      print("1. Tambah Data Tanaman")
      print("2. Lihat Data Tanaman")
      print("3. Update Data Tanaman")
      print("4. Hapus Data Tanaman")
      print("5. Kembali ke Awal")
      
      pilihan = input("Pilih menu: ")
      
      if pilihan == "1":
         add_tanaman()
      elif pilihan == "2":
         read_tanaman()
      elif pilihan == "3":
         update_tanaman()
      elif pilihan == "4":
         delete_tanaman()
      elif pilihan == "5":
         main_menu()
      else:
         print("Pilihan tidak valid. Silakan pilih lagi.")