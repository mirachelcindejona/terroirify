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
   try:
      with open(DATA_TANAMAN, "w") as file:
         json.dump(data, file, indent=4)
   except Exception as e:
      print(f"Error saat menyimpan data: {str(e)}")

def generate_id(data):
   try:
      counter = 1
      while True:
         id_tanaman = f"TNMN{counter:03d}"
         if id_tanaman not in data:
            return id_tanaman
         counter += 1
   except Exception as e:
      print(f"Error saat generate ID: {str(e)}")
      return None

def add_tanaman():
   try:
      data = load_data()
      
      print("\n=== Tambah Tanaman Baru ===")
      id_tanaman = generate_id(data)
      if not id_tanaman:
         print("Gagal membuat ID tanaman")
         return
      
      while True:
         nama_tanaman = input("Masukkan Nama Tanaman: ").strip().lower()
         if not nama_tanaman:
            print("Error: Nama tanaman tidak boleh kosong!\n")
            continue
         break
       
      while True:  
         jenis_tanaman = input("Masukkan Jenis Tanaman: ").strip().lower()
         if not jenis_tanaman:
            print("Error: Jenis tanaman tidak boleh kosong!\n")
            continue
         break
      
      while True: 
         tanggal_tanam = input("Tanggal Tanam (YYYY-MM-DD): ").strip()
         if not tanggal_tanam:
            print("Error: Tanggal tanam tidak boleh kosong!\n")
            continue
         try:
            datetime.strptime(tanggal_tanam, "%Y-%m-%d")
            break
         except ValueError:
            print("Error: Pastikan tanggal dalam format YYYY-MM-DD yang benar.\n")
            continue
            
      while True:       
         kondisi_tanaman = input("Kondisi Tanaman: ").strip().lower()
         if not kondisi_tanaman:
            print("Error: Kondisi tanaman tidak boleh kosong!\n")
            continue
         break
         
      while True:    
         lokasi_tanaman = input("Lokasi Tanaman: ").strip().lower()
         if not lokasi_tanaman:
            print("Error: Lokasi tanaman tidak boleh kosong!\n")
            continue
         break

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
   except Exception as e:
      print(f"Error saat menambah tanaman: {str(e)}")

def read_tanaman():
   try:
      data = load_data()
      if data:
         print("\n=== Data Tanaman ===\n")
         print("=" * 100)
         print(f"{'ID':<10} | {'Nama Tanaman':<20} | {'Jenis Tanaman':<20} | {'Tanggal Tanam':<15} | {'Kondisi':<15} | {'Lokasi':<20}")
         print("=" * 100)
         for id_tanaman, tanaman in data.items():
            print(f"{tanaman['id']:<10} | {tanaman['nama_tanaman']:<20} | {tanaman['jenis_tanaman']:<20} | {tanaman['tanggal_tanam']:<15} | {tanaman['kondisi_tanaman']:<15} | {tanaman['lokasi_tanaman']:<20}")
            print("-" * 100)
      else:
         print("Tidak ada data tanaman.")
   except Exception as e:
      print(f"Error saat membaca data: {str(e)}")

def update_tanaman():
   try:
      data = load_data()
      id_tanaman = input("\nMasukkan ID tanaman yang akan diperbarui: ").strip()
      
      if not id_tanaman:
         print("Error: ID tanaman tidak boleh kosong!\n")
         return
      if id_tanaman not in data:
         print("Tanaman dengan ID tersebut tidak ditemukan.")
         return
      
      print(f"\n=== Data tanaman saat ini dengan ID {id_tanaman} ===\n")
      print("=" * 100)
      print(f"{'ID':<10} | {'Nama Tanaman':<20} | {'Jenis Tanaman':<20} | {'Tanggal Tanam':<15} | {'Kondisi':<15} | {'Lokasi':<20}")
      print("=" * 100)
      print(f"{data[id_tanaman]['id']:<10} | {data[id_tanaman]['nama_tanaman']:<20} | {data[id_tanaman]['jenis_tanaman']:<20} | {data[id_tanaman]['tanggal_tanam']:<15} | {data[id_tanaman]['kondisi_tanaman']:<15} | {data[id_tanaman]['lokasi_tanaman']:<20}")
      print("-" * 100)

      print("\n=== Update Data Tanaman ===\n(Tidak perlu diisi jika tidak ingin diubah)")
      nama_tanaman = input(f"Nama Tanaman [{data[id_tanaman]['nama_tanaman']}]: ").strip().lower() or data[id_tanaman]['nama_tanaman']
      jenis_tanaman = input(f"Jenis Tanaman [{data[id_tanaman]['jenis_tanaman']}]: ").strip().lower() or data[id_tanaman]['jenis_tanaman']
      
      while True:
         tanggal_tanam = input(f"Tanggal Tanam (YYYY-MM-DD) [{data[id_tanaman]['tanggal_tanam']}]: ").strip() or data[id_tanaman]['tanggal_tanam']
         try:
            datetime.strptime(tanggal_tanam, "%Y-%m-%d")
            break
         except ValueError:
            print("Error: Pastikan tanggal tanam dalam format YYYY-MM-DD yang benar.\n")
            continue

      kondisi_tanaman = input(f"Kondisi Tanaman [{data[id_tanaman]['kondisi_tanaman']}]: ").strip().lower() or data[id_tanaman]['kondisi_tanaman']
      lokasi_tanaman = input(f"Lokasi Tanaman [{data[id_tanaman]['lokasi_tanaman']}]: ").strip().lower() or data[id_tanaman]['lokasi_tanaman']

      data[id_tanaman] = {
         "id": id_tanaman,
         "nama_tanaman": nama_tanaman,
         "jenis_tanaman": jenis_tanaman,
         "tanggal_tanam": tanggal_tanam,
         "kondisi_tanaman": kondisi_tanaman,
         "lokasi_tanaman": lokasi_tanaman
      }
      
      save_data(data)
      print("\nData tanaman berhasil diperbarui!")
   except Exception as e:
      print(f"Error saat update tanaman: {str(e)}")

def delete_tanaman():
   try:
      data = load_data()
      id_tanaman = input("\nMasukkan ID tanaman yang akan dihapus: ").strip()
      
      if not id_tanaman:
         print("Error: ID tanaman tidak boleh kosong!\n")
         return
      
      if id_tanaman in data:
         konfirmasi = input(f"Anda yakin ingin menghapus tanaman {id_tanaman}? (y/n): ").lower()
         if konfirmasi == 'y':
            del data[id_tanaman]
            save_data(data)
            print("Tanaman berhasil dihapus!")
         else:
            print("Penghapusan dibatalkan.")
      else:
         print("Tanaman dengan ID tersebut tidak ditemukan.")
   except Exception as e:
      print(f"Error saat menghapus tanaman: {str(e)}")
   
def menu_tanaman():
   try:
      from main import main_menu
      while True:
         print("\n=== Menu Tanaman ===")
         print("1. Tambah Data Tanaman")
         print("2. Lihat Data Tanaman")
         print("3. Update Data Tanaman")
         print("4. Hapus Data Tanaman")
         print("5. Kembali ke Awal")
         
         pilihan = input("Pilih menu: ").strip()
         
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
   except Exception as e:
      print(f"Error pada menu: {str(e)}")