import sqlite3

# --- KONEKSI & PERSIAPAN DATABASE SQL ---
def inisialisasi_database():
    # Menghubungkan/membuat file database SQL bernama database.db
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    # Membuat tabel 'users' jika belum ada
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    
    # Menambahkan akun 'admin' default jika tabel masih kosong
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", "1234"))
        conn.commit()
        
    conn.close()

# --- FUNGSI DATABASE USER (SQL) ---
def registrasi_user():
    print("\n=== BUAT USERNAME & PASSWORD BARU ===")
    username_baru = input("Masukkan Username Baru: ")
    password_baru = input("Masukkan Password Baru: ")
    
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    try:
        # Memasukkan data user baru ke tabel SQL
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username_baru, password_baru))
        conn.commit()
        print("User baru berhasil ditambahkan ke Database SQL!")
    except sqlite3.IntegrityError:
        print("Username sudah digunakan! Silakan pilih username lain.")
    finally:
        conn.close()

def login():
    print("\n=== LOGIN PENGGUNA ===")
    username = input("Username: ")
    password = input("Password: ")

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    # Memeriksa apakah username & password cocok di database SQL
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        print(f"\nLogin Berhasil! Selamat datang, {username}.")
        return True
    else:
        print("\nUsername atau Password salah!")
        return False


# --- FUNGSI PROGRAM UTAMA ---
def cek_ganjil_genap(bilangan):
    if bilangan % 2 == 0:
        return "genap"
    else:
        return "ganjil"

def cek_bilangan_prima(bilangan):
    if bilangan < 2:
        return False
    for i in range(2, bilangan):
        if bilangan % i == 0:
            return False
    return True

def sapa(nama):
    print("Halo,", nama)
    print("Selamat datang di program Python!")

def cek_nilai(nilai):
    if nilai >= 75:
        print("Status: LULUS")
    else:
        print("Status: TIDAK LULUS")


# --- MENU UTAMA ---
def main():
    # Jalankan persiapan database SQL di awal program
    inisialisasi_database()
    
    while True:
        print("\n===== SYSTEM AUTHENTICATION (SQL) =====")
        print("1. Login")
        print("2. Buat Akun Baru (Registrasi)")
        print("3. Keluar Program")
        
        pilihan_auth = input("Pilih menu (1-3): ")

        if pilihan_auth == "1":
            if login():
                # Masuk ke Menu Program Utama setelah Login Berhasil
                while True:
                    print("\n===== MENU PROGRAM PYTHON =====")
                    print("1. Cek Ganjil Genap")
                    print("2. Cek Bilangan Prima")
                    print("3. Sapa Nama")
                    print("4. Cek Nilai")
                    print("5. Logout")

                    pilihan = input("Pilih menu (1-5): ")

                    if pilihan == "1":
                        bilangan = int(input("Masukkan bilangan: "))
                        hasil = cek_ganjil_genap(bilangan)
                        print("Bilangan", bilangan, "adalah", hasil)

                    elif pilihan == "2":
                        bilangan = int(input("Masukkan bilangan: "))
                        if cek_bilangan_prima(bilangan):
                            print("Bilangan", bilangan, "adalah bilangan prima")
                        else:
                            print("Bilangan", bilangan, "bukan bilangan prima")

                    elif pilihan == "3":
                        nama = input("Masukkan nama: ")
                        sapa(nama)

                    elif pilihan == "4":
                        nilai = int(input("Masukkan nilai: "))
                        cek_nilai(nilai)

                    elif pilihan == "5":
                        print("Anda telah Logout.")
                        break

                    else:
                        print("Menu tidak tersedia! Silakan pilih 1-5.")

        elif pilihan_auth == "2":
            registrasi_user()

        elif pilihan_auth == "3":
            print("Terima kasih, program berhenti.")
            break

        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()

    import sqlite3

# --- KONEKSI & PERSIAPAN DATABASE SQL ---
def inisialisasi_database():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", "1234"))
        conn.commit()
        
    conn.close()

# --- FUNGSI DATABASE USER ---
def registrasi_user():
    print("\n=== BUAT USERNAME & PASSWORD BARU ===")
    username_baru = input("Masukkan Username Baru: ")
    password_baru = input("Masukkan Password Baru: ")
    
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username_baru, password_baru))
        conn.commit()
        print("User baru berhasil ditambahkan ke Database SQL!")
    except sqlite3.IntegrityError:
        print("Username sudah digunakan! Silakan pilih username lain.")
    finally:
        conn.close()

def login():
    print("\n=== LOGIN PENGGUNA ===")
    username = input("Username: ")
    password = input("Password: ")

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        print(f"\nLogin Berhasil! Selamat datang, {username}.")
        return True
    else:
        print("\nUsername atau Password salah!")
        return False


# --- FUNGSI PROGRAM LAMA KAMU ---
def cek_ganjil_genap(bilangan):
    if bilangan % 2 == 0:
        return "genap"
    else:
        return "ganjil"

def cek_bilangan_prima(bilangan):
    if bilangan < 2:
        return False
    for i in range(2, bilangan):
        if bilangan % i == 0:
            return False
    return True

def sapa(nama):
    print("Halo,", nama)
    print("Selamat datang di program Python!")

def cek_nilai(nilai):
    if nilai >= 75:
        print("Status: LULUS")
    else:
        print("Status: TIDAK LULUS")


# --- MENU UTAMA ---
def main():
    inisialisasi_database()
    
    while True:
        print("\n===== SYSTEM AUTHENTICATION (SQL) =====")
        print("1. Login")
        print("2. Buat Akun Baru (Registrasi)")
        print("3. Keluar Program")
        
        pilihan_auth = input("Pilih menu (1-3): ")

        if pilihan_auth == "1":
            # Jika login berhasil, baru masuk ke program kamu yang lama
            if login():
                while True:
                    print("\n===== MENU PROGRAM PYTHON =====")
                    print("1. Cek Ganjil Genap")
                    print("2. Cek Bilangan Prima")
                    print("3. Sapa Nama")
                    print("4. Cek Nilai")
                    print("5. Logout")

                    pilihan = input("Pilih menu (1-5): ")

                    if pilihan == "1":
                        bilangan = int(input("Masukkan bilangan: "))
                        hasil = cek_ganjil_genap(bilangan)
                        print("Bilangan", bilangan, "adalah", hasil)

                    elif pilihan == "2":
                        bilangan = int(input("Masukkan bilangan: "))
                        if cek_bilangan_prima(bilangan):
                            print("Bilangan", bilangan, "adalah bilangan prima")
                        else:
                            print("Bilangan", bilangan, "bukan bilangan prima")

                    elif pilihan == "3":
                        nama = input("Masukkan nama: ")
                        sapa(nama)

                    elif pilihan == "4":
                        nilai = int(input("Masukkan nilai: "))
                        cek_nilai(nilai)

                    elif pilihan == "5":
                        print("Anda telah Logout.")
                        break

                    else:
                        print("Menu tidak tersedia! Silakan pilih 1-5.")

        elif pilihan_auth == "2":
            registrasi_user()

        elif pilihan_auth == "3":
            print("Program berhenti.")
            break

        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
