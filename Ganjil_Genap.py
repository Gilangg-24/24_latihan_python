# Program cek bilangan ganjil atau genap

bilangan = int(input("Masukkan sebuah bilangan: "))

if bilangan % 2 == 0:
    print("Bilangan", bilangan, "adalah bilangan genap")
else:
    print("Bilangan", bilangan, "adalah bilangan ganjil")