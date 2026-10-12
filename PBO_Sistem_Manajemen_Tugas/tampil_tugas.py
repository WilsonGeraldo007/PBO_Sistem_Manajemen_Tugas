
import csv
import os
from models import Tugas


def muat_data():
    daftar_tugas = []

    if not os.path.exists("tugas.csv"):
        print("File tugas.csv tidak ditemukan.")
        return daftar_tugas

    with open("tugas.csv", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)

        for row in reader:
            if len(row) == 4:
                tugas = Tugas(
                    id_tugas=row[0],
                    nama=row[1],
                    mapel=row[2],
                    deadline=row[3]
                )
                daftar_tugas.append(tugas)

    return daftar_tugas


def tampilkan_tugas():
    daftar_tugas = muat_data()

    if not daftar_tugas:
        print("Tidak ada data tugas.")
        return

    print("\n=== DAFTAR TUGAS ===\n")
    print(
        f"{'ID':10}{'Nama Tugas':25}"
        f"{'Mata Pelajaran':20}{'Deadline'}"
    )
    print("-" * 75)

    for tugas in daftar_tugas:
        print(
            f"{tugas.id_tugas:10}"
            f"{tugas.nama[:23]:25}"
            f"{tugas.mapel[:18]:20}"
            f"{tugas.deadline}"
        )

    print("-" * 75)
    print(f"Total Tugas: {len(daftar_tugas)}")


def main():
    while True:
        print("\n=== MENU ===")
        print("1. Tampilkan Tugas")
        print("2. Refresh Data")
        print("0. Keluar")

        pilihan = input("Pilih: ")

        if pilihan == "1":
            tampilkan_tugas()

        elif pilihan == "2":
            print("Data dimuat ulang...")
            tampilkan_tugas()

        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
