import json
import os

DATAFILE = "panen.json"

#Fungsi untuk memuat data dari file JSON
def loaddata():
    if os.path.exists(DATAFILE):
        with open(DATAFILE, "r") as file:
            data = json.load(file)
    else:
        data = []
    return data

#Fungsi untuk menyimpan data ke file JSON
def savedata(data):
    with open(DATAFILE, "w") as file:
        json.dump(data, file)

#Fungsi untuk menambah catatan panen
def tambahpanen():
    nama = input("Nama petani: ")
    tanaman = input("Jenis tanaman: ")
    hasil = input("Hasil panen (kg): ")

    #Membuat catatan baru
    catatan = {"nama": nama, "tanaman": tanaman, "hasil": hasil}

    #Memuat data lama dan menambah catatan baru
    data = loaddata()
    data.append(catatan)
    savedata(data)

    print("Catatan panen ditambahkan!")

#Fungsi untuk menampilkan semua catatan panen
def tampilkanpanen():
    data = loaddata()
    if not data:
        print("Belum ada data panen.")
        return

    for idx, catatan in enumerate(data, start=1):
        print(f"{idx}. {catatan['nama']} - {catatan['tanaman']} - {catatan['hasil']} kg")

#Menu utama
def main():
    while True:
        print("\n1. Tambah Panen")
        print("2. Tampilkan Panen")
        print("3. Keluar")

        pilihan = input("Pilih (1/2/3): ")

        if pilihan == "1":
            tambahpanen()
        elif pilihan == "2":
            tampilkanpanen()
        elif pilihan == "3":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()
