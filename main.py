import json
from auth import register, login, clear_login_data
from tanaman import menu_tanaman
from daftar_pekerja import menu_pekerja
from pupuk import menu_pupuk
from panen import menu_panen
from pemasukan import menu_pemasukan
from pengeluaran import menu_pengeluaran

DATA_LOGIN = "data/data_login.json"

def get_current_user():
    try:
        with open(DATA_LOGIN, "r") as file:
            data = json.load(file)
            if data and len(data) > 0:
                return data
            return None
    except (FileNotFoundError, json.JSONDecodeError):
        return None

current_user = get_current_user()
is_logged_in = current_user is not None

def main_menu():
    global is_logged_in, current_user
    print("\n=== Aplikasi Manajemen Kebun ===\n")

    while True:
        if not is_logged_in:
            print("\n1. Registrasi Pengelola")
            print("2. Login Pengelola") 
            print("3. Keluar")
            pilihan = input("Pilih opsi (1/2/3): ")

            if pilihan == "1":
                success, _ = register()
                if success:
                    is_logged_in, current_user = login()
                    if is_logged_in:
                        current_user = get_current_user()
                        print(f"\nAnda berhasil login sebagai {current_user['nama']}")
            elif pilihan == "2":
                is_logged_in, current_user = login()
                if is_logged_in:
                    current_user = get_current_user()
                    print(f"\nAnda berhasil login sebagai {current_user['nama']}")
            elif pilihan == "3":
                print("Terima kasih telah menggunakan Aplikasi Manajemen Kebun.")
                exit()
            else:
                print("\nPilihan tidak valid!")
        else:
            current_user = get_current_user()
            print(f"\nAnda sudah login sebagai {current_user['nama']}")
            print("\n=== Menu Pengelola ===\n")
            print("1. Pencatatan Tanaman")
            print("2. Pengingat Penyiraman dan Pemupukan")
            print("3. Pencatatan Panen")
            print("4. Pengelolaan Pupuk")
            print("5. Pemasukan")
            print("6. Pengeluaran")
            print("7. Daftar Pekerja")
            print("8. Pencarian")
            print("9. Logout")

            pilihan = input("Pilih opsi (1-9): ")

            if pilihan == "1":
                menu_tanaman()
            elif pilihan == "2":
                menu_pengingat()
            elif pilihan == "3":
                menu_panen()
            elif pilihan == "4":
                menu_pupuk()
            elif pilihan == "5":
                menu_pemasukan()
            elif pilihan == "6":
                menu_pengeluaran()
            elif pilihan == "7":
                menu_pekerja()
            elif pilihan == "8":
                pencarian()
            elif pilihan == "9":
                is_logged_in = False
                current_user = None
                clear_login_data()
                print("\nAnda berhasil logout.")
            else:
                print("\nPilihan tidak valid!")

if __name__ == "__main__":
    main_menu()
