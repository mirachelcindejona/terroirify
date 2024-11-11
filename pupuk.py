import json
import os
from datetime import datetime

# File untuk menyimpan data pupuk
DATA_FILE = 'data/fertilizer_data.json'

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
def add_fertilizer():
    data = load_data()
    id_pupuk = generate_id(data)
    name = input("Masukkan nama pupuk: ")
    stock = input("Masukkan jumlah stok pupuk: ")
    reception_date = input("Masukkan tanggal penerimaan stok (YYYY-MM-DD): ")
    usage_notes = input("Masukkan catatan penggunaan pupuk: ")

    try:
        id_pupuk = id_pupuk
        stock = int(stock)
        datetime.strptime(reception_date, '%Y-%m-%d')  # Validasi format tanggal
    except ValueError as e:
        print(f"Error: {e}")
        return

    data = load_data()
    data[id_pupuk] = {
        'id_pupuk': id_pupuk,
        'name': name,
        'stock': stock,
        'reception_date': reception_date,
        'usage_notes': usage_notes
    }
    save_data(data)
    print("Data pupuk berhasil ditambahkan.")

# Fungsi untuk melihat semua data pupuk
def view_fertilizers():
    data = load_data()
    if data:
        for pupuk_id, fertilizer in data.items():
            print(f"ID: {fertilizer['id_pupuk']}, Name: {fertilizer['name']}, Stock: {fertilizer['stock']}, Reception Date: {fertilizer['reception_date']}, Usage Notes: {fertilizer['usage_notes']}")
    else:
        print("Tidak ada data pupuk.")

# Fungsi untuk memperbarui data pupuk
def update_fertilizer():
    id_pupuk = input("Masukkan ID pupuk yang ingin diperbarui: ")
    name = input("Masukkan nama baru pupuk: ")
    stock = input("Masukkan jumlah stok baru pupuk: ")
    reception_date = input("Masukkan tanggal penerimaan stok baru (YYYY-MM-DD): ")
    usage_notes = input("Masukkan catatan penggunaan baru pupuk: ")

    try:
        stock = int(stock)
        datetime.strptime(reception_date, '%Y-%m-%d')  # Validasi format tanggal
    except ValueError as e:
        print(f"Error: {e}")
        return

    data = load_data()
    if id_pupuk in data:
        data[id_pupuk] = {
            'id_pupuk': id_pupuk,
            'name': name,
            'stock': stock,
            'reception_date': reception_date,
            'usage_notes': usage_notes
        }
        save_data(data)
        print("Data pupuk berhasil diperbarui.")
    else:
        print("Pupuk dengan ID yang ditentukan tidak ditemukan.")

# Fungsi untuk menghapus data pupuk
def delete_fertilizer():
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
            add_fertilizer()
        elif command == 'view':
            view_fertilizers()
        elif command == 'update':
            update_fertilizer()
        elif command == 'delete':
            delete_fertilizer()
        elif command == 'exit':
            print("Keluar dari program.")
            break
        else:
            print("Perintah tidak dikenali. Silakan coba lagi.")

if __name__ == '__main__':
    main()
