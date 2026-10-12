
import csv
import os
from models import Tugas


def simpan_tugas():
    print("\n=== TAMBAH DATA TUGAS ===")

    id_tugas = input("ID Tugas : ").strip()
    nama = input("Nama Tugas : ").strip()
    mapel = input("Mata Pelajaran : ").strip()
    deadline = input("Deadline : ").strip()

    if not id_tugas or not nama or not mapel or not deadline:
        print("\n[PERINGATAN] Semua kolom harus diisi!\n")
        return

    file_exists = os.path.exists("tugas.csv")

    tugas = Tugas(id_tugas, nama, mapel, deadline)

    with open("tugas.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "ID Tugas", "Nama Tugas",
                "Mata Pelajaran", "Deadline"
            ])

        writer.writerow(tugas.to_list())

    print("\n[BERHASIL] Tugas berhasil ditambahkan.\n")


def main():
    while True:
        print("=== MENU TAMBAH TUGAS ===")
        print("1. Tambah Tugas")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            simpan_tugas()

        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!\n")


if __name__ == "__main__":
    main()
