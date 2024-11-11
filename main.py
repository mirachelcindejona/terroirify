from auth import register, login
from daftar_pekerja import create_pekerja, read_pekerja, update_pekerja, delete_pekerja
# from pupuk import 
# from kebun import (
#    catat_tanaman,
#    pengingat_penyiraman_pemupukan,
#    catat_panen,
#    kelola_pupuk,
#    catat_keuangan,
#    catat_pekerja,
#    pencarian
# )

# Variabel global untuk menyimpan status login dan informasi pengguna
is_logged_in = False
current_user = None

def main_menu():
   global is_logged_in, current_user
   print("\n=== Aplikasi Manajemen Kebun ===\n")

   while True:
      if not is_logged_in:
         print("\n1. Registrasi Pengelola")
         print("2. Login Pengelola")
         print("3. Keluar")  # Tambahkan opsi Keluar
         pilihan = input("Pilih opsi (1/2/3): ")

         if pilihan == "1":
               register()
         elif pilihan == "2":
               is_logged_in, current_user = login()
               if is_logged_in:
                  print(f"\nAnda berhasil login sebagai {current_user['nama']}")
         elif pilihan == "3":
               print("Terima kasih telah menggunakan Aplikasi Manajemen Kebun.")
               break  # Keluar dari aplikasi
         else:
               print("\nPilihan tidak valid!")
      else:
         # Menu khusus setelah login
         print(f"\nAnda sudah login sebagai {current_user['nama']}")
         print("\n=== Menu Pengelola ===\n")
         print("1. Pencatatan Tanaman")
         print("2. Pengingat Penyiraman dan Pemupukan")
         print("3. Pencatatan Panen")
         print("4. Pengelolaan Pupuk")
         print("5. Manajemen Keuangan")
         print("6. Daftar Pekerja")
         print("7. Pencarian")
         print("8. Logout")

         pilihan = input("Pilih opsi (1-8): ")

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
         elif pilihan == "8":
               is_logged_in = False
               current_user = None
               print("\nAnda berhasil logout.")
         else:
               print("\nPilihan tidak valid!")

if __name__ == "__main__":
   main_menu()
