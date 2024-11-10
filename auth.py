import json
import os
import datetime

DATA_FILE = "data/kebun_data.json"

def load_data():
   if os.path.exists(DATA_FILE):
      with open(DATA_FILE, "r") as file:
         return json.load(file)
   return {
      "tanaman": [],
      "pengingat": [],
      "panen": [],
      "pupuk": [],
      "keuangan": [],
      "pekerja": []
   }

def save_data(data):
   with open(DATA_FILE, "w") as file:
      json.dump(data, file, indent=4)

# Fitur 1: Pencatatan Tanaman
def catat_tanaman():
   data = load_data()
   print("\n=== Pencatatan Tanaman ===")
   tanggal_tanam = input("Tanggal Penanaman (YYYY-MM-DD): ")
   jenis_tanaman = input("Jenis Tanaman: ")
   kategori = input("Kategori Tanaman: ")
   pertumbuhan = input("Kondisi Pertumbuhan: ")

   tanaman = {
      "tanggal_tanam": tanggal_tanam,
      "jenis_tanaman": jenis_tanaman,
      "kategori": kategori,
      "pertumbuhan": pertumbuhan
   }
   data["tanaman"].append(tanaman)
   save_data(data)
   print("Tanaman berhasil dicatat.")

# Fitur 2: Pengingat Penyiraman dan Pemupukan
def pengingat_penyiraman_pemupukan():
   data = load_data()
   print("\n=== Pengingat Penyiraman dan Pemupukan ===")
   tanggal_jadwal = input("Tanggal Penyiraman/Pemupukan (YYYY-MM-DD): ")
   jenis = input("Jenis Pengingat (Penyiraman/Pemupukan): ")
   tanaman_id = input("ID Tanaman: ")

   pengingat = {
      "tanggal_jadwal": tanggal_jadwal,
      "jenis": jenis,
      "tanaman_id": tanaman_id
   }
   data["pengingat"].append(pengingat)
   save_data(data)
   print("Pengingat berhasil disimpan.")

# Fitur 3: Pencatatan Panen
def catat_panen():
   data = load_data()
   print("\n=== Pencatatan Panen ===")
   tanggal_panen = input("Tanggal Panen (YYYY-MM-DD): ")
   tanaman_id = input("ID Tanaman: ")
   jumlah = input("Jumlah Panen: ")
   kualitas = input("Kualitas Panen: ")

   panen = {
      "tanggal_panen": tanggal_panen,
      "tanaman_id": tanaman_id,
      "jumlah": jumlah,
      "kualitas": kualitas
   }
   data["panen"].append(panen)
   save_data(data)
   print("Hasil panen berhasil dicatat.")

# Fitur 4: Pengelolaan Pupuk
def kelola_pupuk():
   data = load_data()
   print("\n=== Pengelolaan Pupuk ===")
   nama_pupuk = input("Nama Pupuk: ")
   jumlah_awal = int(input("Jumlah Awal (kg): "))
   jumlah_digunakan = int(input("Jumlah Digunakan (kg): "))
   jumlah_tersisa = jumlah_awal - jumlah_digunakan

   pupuk = {
      "nama_pupuk": nama_pupuk,
      "jumlah_awal": jumlah_awal,
      "jumlah_digunakan": jumlah_digunakan,
      "jumlah_tersisa": jumlah_tersisa
   }
   data["pupuk"].append(pupuk)
   save_data(data)
   print("Data pupuk berhasil disimpan.")

# Fitur 5: Manajemen Keuangan
def catat_keuangan():
   data = load_data()
   print("\n=== Manajemen Keuangan ===")
   tipe_transaksi = input("Jenis Transaksi (Pemasukan/Pengeluaran): ")
   jumlah = int(input("Jumlah: "))
   keterangan = input("Keterangan: ")

   transaksi = {
      "tipe_transaksi": tipe_transaksi,
      "jumlah": jumlah,
      "keterangan": keterangan,
      "tanggal": datetime.datetime.now().strftime("%Y-%m-%d")
   }
   data["keuangan"].append(transaksi)
   save_data(data)
   print("Transaksi keuangan berhasil dicatat.")

# Fitur 6: Daftar Pekerja
def catat_pekerja():
   data = load_data()
   print("\n=== Daftar Pekerja ===")
   nama = input("Nama Pekerja: ")
   peran = input("Peran: ")

   pekerja = {
      "nama": nama,
      "peran": peran
   }
   data["pekerja"].append(pekerja)
   save_data(data)
   print("Data pekerja berhasil disimpan.")

# Fitur 7: Pencarian
def pencarian():
   data = load_data()
   print("\n=== Fitur Pencarian ===")
   keyword = input("Masukkan kata kunci pencarian: ").lower()

   results = {
      "tanaman": [tanaman for tanaman in data["tanaman"] if keyword in tanaman["jenis_tanaman"].lower()],
      "pengingat": [pengingat for pengingat in data["pengingat"] if keyword in pengingat["jenis"].lower()],
      "panen": [panen for panen in data["panen"] if keyword in panen["tanaman_id"]],
      "pupuk": [pupuk for pupuk in data["pupuk"] if keyword in pupuk["nama_pupuk"].lower()],
      "keuangan": [transaksi for transaksi in data["keuangan"] if keyword in transaksi["keterangan"].lower()],
      "pekerja": [pekerja for pekerja in data["pekerja"] if keyword in pekerja["nama"].lower()]
   }
   
   print(f"Hasil pencarian untuk '{keyword}':")
   for category, items in results.items():
      if items:
         print(f"\n{category.capitalize()}:")
         for item in items:
               print(item)
      else:
         print(f"\n{category.capitalize()}: Tidak ada hasil yang ditemukan")

# Fungsi untuk menampilkan menu utama
def main_menu():
   while True:
      print("\n=== Aplikasi Manajemen Kebun ===")
      print("1. Pencatatan Tanaman")
      print("2. Pengingat Penyiraman dan Pemupukan")
      print("3. Pencatatan Panen")
      print("4. Pengelolaan Pupuk")
      print("5. Manajemen Keuangan")
      print("6. Daftar Pekerja")
      print("7. Pencarian")
      print("0. Keluar")

      pilihan = input("Pilih opsi (0-7): ")

      if pilihan == "1":
         catat_tanaman()
      elif pilihan == "2":
         pengingat_penyiraman_pemupukan()
      elif pilihan == "3":
         catat_panen()
      elif pilihan == "4":
         kelola_pupuk()
      elif pilihan == "5":
         catat_keuangan()
      elif pilihan == "6":
         catat_pekerja()
      elif pilihan == "7":
         pencarian()
      elif pilihan == "0":
         print("Keluar dari aplikasi.")
         break
      else:
         print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
   main_menu()
