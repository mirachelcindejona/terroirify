import json
import os
from datetime import datetime

# File untuk menyimpan data pupuk
DATA_FILE = 'data/data_pupuk.json'

def initialize_data_directory():
    os.makedirs("data", exist_ok=True)

# Memuat data dari file
def load_data():
    initialize_data_directory()
    if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

# Menyimpan data ke file
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def generate_id(data):
    pupuk_id = f"00{len(data) + 1}"
    while pupuk_id in data:
        pupuk_id = f"00{len(data) + 1}"
    return pupuk_id

# Fungsi untuk menambah data pupuk
def add_pupuk():
    data = load_data()
    id_pupuk = generate_id(data)
    nama = input("Masukkan nama pupuk: ")
    stok = input("Masukkan jumlah stok pupuk: ")
    tanggal_penerimaan = input("Masukkan tanggal penerimaan stok (YYYY-MM-DD): ")
    catatan = input("Masukkan catatan penggunaan pupuk: ")

    try:
        id_pupuk = id_pupuk
        stok = int(stok)
        datetime.strptime(tanggal_penerimaan, '%Y-%m-%d')  # Validasi format tanggal
    except ValueError as e:
        print(f"Error: {e}")
        return

    data = load_data()
    data[id_pupuk] = {
        'id_pupuk': id_pupuk,
        'nama': nama,
        'stok': stok,
        'tanggal_penerimaan': tanggal_penerimaan,
        'catatan': catatan
    }
    save_data(data)
    print("Data pupuk berhasil ditambahkan.")

# Fungsi untuk melihat semua data pupuk
def view_pupuk():
    data = load_data()
    if data:
        for pupuk_id, pupuk in data.items():
            print(f"ID: {pupuk['id_pupuk']}, Name: {pupuk['nama']}, Stock: {pupuk['stok']}, Reception Date: {pupuk['tanggal_penerimaan']}, Usage Notes: {pupuk['catatan']}")
    else:
        print("Tidak ada data pupuk.")

# Fungsi untuk memperbarui data pupuk
def update_pupuk():
    id_pupuk = input("Masukkan ID pupuk yang ingin diperbarui: ")
    nama = input("Masukkan nama baru pupuk: ")
    stok = input("Masukkan jumlah stok baru pupuk: ")
    tanggal_penerimaan = input("Masukkan tanggal penerimaan stok baru (YYYY-MM-DD): ")
    catatan = input("Masukkan catatan penggunaan baru pupuk: ")

    try:
        stok = int(stok)
        datetime.strptime(tanggal_penerimaan, '%Y-%m-%d')  # Validasi format tanggal
    except ValueError as e:
        print(f"Error: {e}")
        return

    data = load_data()
    if id_pupuk in data:
        data[id_pupuk] = {
            'id_pupuk': id_pupuk,
            'nama': nama,
            'stok': stok,
            'tanggal_penerimaan': tanggal_penerimaan,
            'catatan': catatan
        }
        save_data(data)
        print("Data pupuk berhasil diperbarui.")
    else:
        print("Pupuk dengan ID yang ditentukan tidak ditemukan.")

# Fungsi untuk menghapus data pupuk
def delete_pupuk():
    id_pupuk = input("Masukkan ID pupuk yang ingin dihapus: ")

    data = load_data()
    if id_pupuk in data:
        del data[id_pupuk]
        save_data(data)
        print("Data pupuk berhasil dihapus.")
    else:
        print("Pupuk dengan ID yang ditentukan tidak ditemukan.")

# Fungsi utama untuk menjalankan program secara interaktif
def main():
    while True:
        print("Pilih perintah: add, view, update, delete, atau exit")
        command = input("Masukkan perintah: ").strip().lower()
        if command == 'add':
            add_pupuk()
        elif command == 'view':
            view_pupuk()
        elif command == 'update':
            update_pupuk()
        elif command == 'delete':
            delete_pupuk()
        elif command == 'exit':
            print("Keluar dari program.")
            break
        else:
            print("Perintah tidak dikenali. Silakan coba lagi.")

if __name__ == '__main__':
    main()
