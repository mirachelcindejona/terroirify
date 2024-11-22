import json
from datetime import datetime

DATA_PENGELUARAN = "data/data_pengeluaran.json"

def load_data():
    try:
        with open(DATA_PENGELUARAN, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONdecodeError):
        return{}
    
def save_data(data):
    with open(DATA_PENGELUARAN, "w") as file:
        json.dump(data, file, indent=4)
        
def generate_id(data):
    pengeluaran_id = f"PLRN{len(data) + 1}"
    while pengeluaran_id in data:
       pengeluaran_id = f"PLRN{len(data) + 1}"
    return pengeluaran_id

def add_pengeluaran():
    data = load_data()
    
    print ("\n=== Tambah Data Pengeluaran")
    id_pengeluaran = generate_id(data) 
    pengeluaran_operasional = input("Masukan jumlah pengeluaran: ")
    nama_pengeluaran = input("Masukkan nama pengeluaran: ")
    tanggal_pengeluaran =input("Tanggal Pengeluaran (YYYY-MM-DD): ")
    kategori_pengeluaran = input("MAsukkan kategori pengeluaran (Biaya pupuk atau Biaya tenaga kerja): ")
    
    try:
        pengeluaran_operasional = float(pengeluaran_operasional)
        datetime.strptime(tanggal_pengeluaran, "%Y-%m-%d")
    except ValueError:
        print("Error: Input tidak valid. Pastikan pengeluaran operasional adlah angka dan tanggal pengeluaran dalam format yang benar! ")
        return

    data[id_pengeluaran] = {
        "id": id_pengeluaran, 
        "pengeluaran_operasional": pengeluaran_operasional,
        "tanggal_pengeluaran": tanggal_pengeluaran,
        "kategori_pengeluaran": kategori_pengeluaran
}

    save_data(data)
    print("Data pengeluaran berhasil ditambahkan!")

def read_pengeluara():
    data = load_data()
    if data:
        print (("\n=== Data Pengeluaran"))
        for pengeluaran_id, pengeluaran in data.items():
            print(f"ID: {pengeluaran["id"]}")
            print(f"Pengeluaran operasional: {pengeluaran["pengeluaran_operasional"]}")
            print(f"Tanggal pengeluaran: {pengeluaran["tanggal_pengeluaran"]}")  
            print(f"Kategori pengeluaran: {pengeluaran["kategori_pengeluaran"]}")
            print("-" * 30)
    else:
        print("Tidak ada data pengeluaran.")