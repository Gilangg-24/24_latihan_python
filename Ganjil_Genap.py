# Program cek bilangan ganjil atau genap

for i in range(100):
    bilangan = int(input("Masukkan bilangan: "))

    if bilangan % 2 == 0:
        print("Bilangan", bilangan, "adalah bilangan genap")
    else:
        print("Bilangan", bilangan, "adalah bilangan ganjil")

    pilihan = input("Apakah ingin mengecek lagi? (y/n): ")

    if pilihan.lower() == "n":
        print("Program berhenti.")
        break

    elif pilihan.lower() == "y":
        continue
    else:
        print("Input tidak valid! Masukkan hanya y atau n.")