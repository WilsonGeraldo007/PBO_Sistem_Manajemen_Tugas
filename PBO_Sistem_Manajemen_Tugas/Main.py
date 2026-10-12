
import subprocess


def buka_tambah_tugas():
    subprocess.run(["python", "tambah_tugas.py"])


def buka_tampil_tugas():
    subprocess.run(["python", "tampil_tugas.py"])


def menu_utama():
    while True:
        print("\n" + "=" * 40)
        print(" SISTEM MANAJEMEN TUGAS ".center(40, "="))
        print("=" * 40)
        print("1. Tambah Tugas")
        print("2. Tampilkan Tugas")
        print("0. Keluar")
        print("=" * 40)

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            buka_tambah_tugas()

        elif pilihan == "2":
            buka_tampil_tugas()

        elif pilihan == "0":
            print("Terima kasih.")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    menu_utama()
