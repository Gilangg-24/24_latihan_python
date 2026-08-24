# Program cek bilangan ganjil atau genap

def cek_ganjil_genap(bilangan):
    if bilangan % 2 == 0:
        print("Bilangan", bilangan, "adalah bilangan genap")
    else:
        print("Bilangan", bilangan, "adalah bilangan ganjil")


while True:
    bilangan = int(input("Masukkan bilangan: "))

    cek_ganjil_genap(bilangan)

    while True:
        pilihan = input("Apakah ingin mengecek lagi? (y/n): ").lower()

        if pilihan == "y":
            break
        elif pilihan == "n":
            print("Program berhenti.")
            exit()
        else:
            print("Input tidak valid! Masukkan hanya y atau n.")


