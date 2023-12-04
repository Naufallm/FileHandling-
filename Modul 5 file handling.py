import os

def tambah_data():
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")
    matkul = input("Masukkan Mata Kuliah: ")
    semester = input("Masukkan Semester: ")

    data_mahasiswa = f"{nama},{nim},{matkul},{semester}\n"

    with open("data_mahasiswa.txt", "a") as file:
        file.write(data_mahasiswa)

    print("Data mahasiswa berhasil ditambahkan.")

def tampilkan_data():
    with open("data_mahasiswa.txt", "r") as file:
        lines = file.readlines()

    if not lines:
        print("Tidak ada data mahasiswa.")
        return

    print("Menampilkan Data:")
    for i, line in enumerate(lines, start=1):
        data = line.strip().split(',')
        print(f"Data ke-{i}:")
        print(f"Nama: {data[0]}")
        print(f"NIM: {data[1]}")
        print(f"Mata Kuliah: {data[2]}")
        print(f"Semester: {data[3]}")
        print()

def update_data():
    nim_target = input("Masukkan NIM mahasiswa yang akan diupdate: ")

    with open("data_mahasiswa.txt", "r") as file:
        lines = file.readlines()

    found = False
    with open("data_mahasiswa.txt", "w") as file:
        for line in lines:
            data = line.strip().split(',')
            if data[1] == nim_target:
                nama = input("Masukkan Nama baru: ")
                matkul = input("Masukkan Mata Kuliah baru: ")
                semester = input("Masukkan Semester baru: ")
                updated_data = f"{nama},{nim_target},{matkul},{semester}\n"
                file.write(updated_data)
                found = True
            else:
                file.write(line)

    if found:
        print("Data mahasiswa berhasil diupdate.")
    else:
        print("Data mahasiswa tidak ditemukan.")

def delete_data():
    nim_target = input("Masukkan NIM mahasiswa yang akan dihapus: ")

    with open("data_mahasiswa.txt", "r") as file:
        lines = file.readlines()

    found = False
    with open("data_mahasiswa.txt", "w") as file:
        for line in lines:
            data = line.strip().split(',')
            if data[1] == nim_target:
                found = True
            else:
                file.write(line)

    if found:
        print("Data mahasiswa berhasil dihapus.")
    else:
        print("Data mahasiswa tidak ditemukan.")

def main():
    while True:
        print("=====APLIKASI KELOLA DATA MAHASISWA=====")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            tampilkan_data()
        elif pilihan == "3":
            update_data()
        elif pilihan == "4":
            delete_data()
        elif pilihan == "5":
            print("Keluar dari aplikasi.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()
