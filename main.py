import matematik
import sapa


def menu():
    while True:
        print("\n=== MENU PROGRAM ===")
        print("1. Cek Bilangan Prima")
        print("2. Cek Ganjil Genap")
        print("3. Sapa Nama")
        print("4. Cek Nilai")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            n = int(input("Masukkan angka: "))

            if matematik.cek_bilangan_prima(n):
                print(f"{n} adalah bilangan prima.")
            else:
                print(f"{n} bukan bilangan prima.")

        elif pilihan == "2":
            n = int(input("Masukkan angka: "))

            hasil = matematik.cek_ganjil_genap(n)
            print(f"Angka {n} adalah {hasil}.")

        elif pilihan == "3":
            nama = input("Masukkan nama Anda: ")
            sapa.sapa(nama)

        elif pilihan == "4":
            nilai = int(input("Masukkan nilai: "))
            sapa.cek_nilai(nilai)

        elif pilihan == "5":
            print("Terima kasih!")
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi.")


if __name__ == "__main__":
    menu()