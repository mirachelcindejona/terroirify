from auth import register, login

def main():
   while True:
      print("\n1. Registrasi")
      print("2. Login")
      print("3. Keluar")
      choice = input("Pilih menu: ")

      if choice == "1":
         register()
      elif choice == "2":
         if login():
               print("Anda berhasil login.")
         else:
               print("Login gagal.")
      elif choice == "3":
         print("Terima kasih. Sampai jumpa!")
         break
      else:
         print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
   main()
