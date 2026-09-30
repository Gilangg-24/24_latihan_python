import tkinter as tk
from tkinter import messagebox
import sqlite3
import json
from datetime import datetime


# =========================================================
# KONFIGURASI FILE
# =========================================================

DATABASE_FILE = "database.db"
JSON_FILE = "riwayat.json"

# Menyimpan username yang sedang login
current_username = ""


# =========================================================
# DATABASE SQLITE
# =========================================================

def inisialisasi_database():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    # Membuat akun admin jika belum ada
    cursor.execute(
        "SELECT COUNT(*) FROM users"
    )

    jumlah_user = cursor.fetchone()[0]

    if jumlah_user == 0:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            ("admin", "1234")
        )

    conn.commit()
    conn.close()


# =========================================================
# JSON - RIWAYAT
# =========================================================

def simpan_riwayat(fitur, input_data, hasil):
    """
    Menyimpan aktivitas pengguna ke file JSON.
    """

    data = []

    # Membaca data JSON yang sudah ada
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

            # Memastikan data berbentuk list
            if not isinstance(data, list):
                data = []

    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    # Membuat data riwayat baru
    riwayat_baru = {
        "username": current_username,
        "fitur": fitur,
        "input": input_data,
        "hasil": hasil,
        "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Menambahkan riwayat
    data.append(riwayat_baru)

    # Menyimpan kembali ke JSON
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )


# =========================================================
# FUNGSI PROGRAM
# =========================================================

def cek_ganjil_genap(bilangan):
    if bilangan % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"


def cek_bilangan_prima(bilangan):
    if bilangan < 2:
        return False

    for i in range(2, bilangan):
        if bilangan % i == 0:
            return False

    return True


def cek_nilai(nilai):
    if nilai >= 75:
        return "LULUS"
    else:
        return "TIDAK LULUS"


# =========================================================
# LOGIN
# =========================================================

def login():

    global current_username

    username = entry_username.get().strip()
    password = entry_password.get()

    # Validasi
    if username == "" or password == "":
        messagebox.showwarning(
            "Peringatan",
            "Username dan password harus diisi!"
        )
        return

    # Koneksi database
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM users
        WHERE username = ? AND password = ?
        """,
        (username, password)
    )

    user = cursor.fetchone()

    conn.close()

    # Jika login berhasil
    if user:

        current_username = username

        messagebox.showinfo(
            "Login Berhasil",
            f"Selamat datang, {username}!"
        )

        login_window.destroy()

        buka_menu_utama(username)

    else:

        messagebox.showerror(
            "Login Gagal",
            "Username atau password salah!"
        )


# =========================================================
# REGISTRASI
# =========================================================

def registrasi():

    username = entry_reg_username.get().strip()
    password = entry_reg_password.get()

    # Validasi
    if username == "" or password == "":
        messagebox.showwarning(
            "Peringatan",
            "Username dan password harus diisi!"
        )
        return

    # Koneksi database
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            INSERT INTO users (username, password)
            VALUES (?, ?)
            """,
            (username, password)
        )

        conn.commit()

        messagebox.showinfo(
            "Berhasil",
            "Akun berhasil dibuat!"
        )

        register_window.destroy()

    except sqlite3.IntegrityError:

        messagebox.showerror(
            "Gagal",
            "Username sudah digunakan!"
        )

    finally:

        conn.close()


# =========================================================
# WINDOW REGISTRASI
# =========================================================

def buka_registrasi():

    global register_window
    global entry_reg_username
    global entry_reg_password

    register_window = tk.Toplevel(login_window)

    register_window.title("Registrasi Akun")
    register_window.geometry("350x300")
    register_window.resizable(False, False)

    tk.Label(
        register_window,
        text="BUAT AKUN BARU",
        font=("Arial", 18, "bold")
    ).pack(pady=20)

    tk.Label(
        register_window,
        text="Username"
    ).pack()

    entry_reg_username = tk.Entry(
        register_window,
        width=30
    )

    entry_reg_username.pack(pady=5)

    tk.Label(
        register_window,
        text="Password"
    ).pack()

    entry_reg_password = tk.Entry(
        register_window,
        width=30,
        show="*"
    )

    entry_reg_password.pack(pady=5)

    tk.Button(
        register_window,
        text="Daftar",
        width=20,
        command=registrasi
    ).pack(pady=20)


# =========================================================
# MENU UTAMA
# =========================================================

def buka_menu_utama(username):

    global main_window

    main_window = tk.Tk()

    main_window.title("Program Python")
    main_window.geometry("500x600")
    main_window.resizable(False, False)

    tk.Label(
        main_window,
        text="MENU PROGRAM PYTHON",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    tk.Label(
        main_window,
        text=f"Selamat datang, {username}",
        font=("Arial", 12)
    ).pack(pady=5)

    # =====================================================
    # TOMBOL GANJIL GENAP
    # =====================================================

    tk.Button(
        main_window,
        text="1. Cek Ganjil Genap",
        width=30,
        height=2,
        command=menu_ganjil_genap
    ).pack(pady=7)

    # =====================================================
    # TOMBOL BILANGAN PRIMA
    # =====================================================

    tk.Button(
        main_window,
        text="2. Cek Bilangan Prima",
        width=30,
        height=2,
        command=menu_prima
    ).pack(pady=7)

    # =====================================================
    # TOMBOL SAPA NAMA
    # =====================================================

    tk.Button(
        main_window,
        text="3. Sapa Nama",
        width=30,
        height=2,
        command=menu_sapa
    ).pack(pady=7)

    # =====================================================
    # TOMBOL CEK NILAI
    # =====================================================

    tk.Button(
        main_window,
        text="4. Cek Nilai",
        width=30,
        height=2,
        command=menu_nilai
    ).pack(pady=7)

    # =====================================================
    # TOMBOL RIWAYAT
    # =====================================================

    tk.Button(
        main_window,
        text="5. Lihat Riwayat",
        width=30,
        height=2,
        command=lihat_riwayat
    ).pack(pady=7)

    # =====================================================
    # TOMBOL LOGOUT
    # =====================================================

    tk.Button(
        main_window,
        text="6. Logout",
        width=30,
        height=2,
        command=logout
    ).pack(pady=7)

    main_window.mainloop()


# =========================================================
# MENU GANJIL GENAP
# =========================================================

def menu_ganjil_genap():

    window = tk.Toplevel(main_window)

    window.title("Cek Ganjil Genap")
    window.geometry("350x250")
    window.resizable(False, False)

    tk.Label(
        window,
        text="CEK GANJIL / GENAP",
        font=("Arial", 16, "bold")
    ).pack(pady=20)

    tk.Label(
        window,
        text="Masukkan Bilangan:"
    ).pack()

    entry = tk.Entry(window)
    entry.pack(pady=10)

    def proses():

        try:

            bilangan = int(entry.get())

            hasil = cek_ganjil_genap(bilangan)

            # Simpan ke JSON
            simpan_riwayat(
                "Ganjil Genap",
                bilangan,
                hasil
            )

            messagebox.showinfo(
                "Hasil",
                f"Bilangan {bilangan} adalah {hasil}"
            )

        except ValueError:

            messagebox.showerror(
                "Error",
                "Masukkan angka yang benar!"
            )

    tk.Button(
        window,
        text="Cek",
        width=15,
        command=proses
    ).pack(pady=10)


# =========================================================
# MENU BILANGAN PRIMA
# =========================================================

def menu_prima():

    window = tk.Toplevel(main_window)

    window.title("Cek Bilangan Prima")
    window.geometry("350x250")
    window.resizable(False, False)

    tk.Label(
        window,
        text="CEK BILANGAN PRIMA",
        font=("Arial", 16, "bold")
    ).pack(pady=20)

    tk.Label(
        window,
        text="Masukkan Bilangan:"
    ).pack()

    entry = tk.Entry(window)
    entry.pack(pady=10)

    def proses():

        try:

            bilangan = int(entry.get())

            if cek_bilangan_prima(bilangan):

                hasil = "Bilangan Prima"

            else:

                hasil = "Bukan Bilangan Prima"

            # Simpan ke JSON
            simpan_riwayat(
                "Bilangan Prima",
                bilangan,
                hasil
            )

            messagebox.showinfo(
                "Hasil",
                f"{bilangan} adalah {hasil}"
            )

        except ValueError:

            messagebox.showerror(
                "Error",
                "Masukkan angka yang benar!"
            )

    tk.Button(
        window,
        text="Cek",
        width=15,
        command=proses
    ).pack(pady=10)


# =========================================================
# MENU SAPA NAMA
# =========================================================

def menu_sapa():

    window = tk.Toplevel(main_window)

    window.title("Sapa Nama")
    window.geometry("350x250")
    window.resizable(False, False)

    tk.Label(
        window,
        text="SAPA NAMA",
        font=("Arial", 16, "bold")
    ).pack(pady=20)

    tk.Label(
        window,
        text="Masukkan Nama:"
    ).pack()

    entry = tk.Entry(window)
    entry.pack(pady=10)

    def proses():

        nama = entry.get().strip()

        if nama == "":

            messagebox.showwarning(
                "Peringatan",
                "Nama harus diisi!"
            )

        else:

            hasil = (
                f"Halo, {nama}! "
                f"Selamat datang di program Python!"
            )

            # Simpan ke JSON
            simpan_riwayat(
                "Sapa Nama",
                nama,
                hasil
            )

            messagebox.showinfo(
                "Sapaan",
                hasil
            )

    tk.Button(
        window,
        text="Sapa",
        width=15,
        command=proses
    ).pack(pady=10)


# =========================================================
# MENU CEK NILAI
# =========================================================

def menu_nilai():

    window = tk.Toplevel(main_window)

    window.title("Cek Nilai")
    window.geometry("350x250")
    window.resizable(False, False)

    tk.Label(
        window,
        text="CEK NILAI",
        font=("Arial", 16, "bold")
    ).pack(pady=20)

    tk.Label(
        window,
        text="Masukkan Nilai:"
    ).pack()

    entry = tk.Entry(window)
    entry.pack(pady=10)

    def proses():

        try:

            nilai = int(entry.get())

            # Validasi nilai
            if nilai < 0 or nilai > 100:

                messagebox.showwarning(
                    "Peringatan",
                    "Nilai harus berada di antara 0 sampai 100!"
                )

                return

            hasil = cek_nilai(nilai)

            # Simpan ke JSON
            simpan_riwayat(
                "Cek Nilai",
                nilai,
                hasil
            )

            messagebox.showinfo(
                "Hasil",
                f"Nilai: {nilai}\n"
                f"Status: {hasil}"
            )

        except ValueError:

            messagebox.showerror(
                "Error",
                "Masukkan nilai berupa angka!"
            )

    tk.Button(
        window,
        text="Cek Nilai",
        width=15,
        command=proses
    ).pack(pady=10)


# =========================================================
# LIHAT RIWAYAT JSON
# =========================================================

def lihat_riwayat():

    window = tk.Toplevel(main_window)

    window.title("Riwayat Aktivitas")
    window.geometry("650x500")
    window.resizable(False, False)

    tk.Label(
        window,
        text="RIWAYAT AKTIVITAS",
        font=("Arial", 18, "bold")
    ).pack(pady=15)

    # Frame untuk text
    frame = tk.Frame(window)
    frame.pack(
        fill="both",
        expand=True,
        padx=15,
        pady=10
    )

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(
        side="right",
        fill="y"
    )

    text_riwayat = tk.Text(
        frame,
        width=75,
        height=22,
        yscrollcommand=scrollbar.set
    )

    text_riwayat.pack(
        side="left",
        fill="both",
        expand=True
    )

    scrollbar.config(
        command=text_riwayat.yview
    )

    # Membaca JSON
    try:

        with open(
            JSON_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

    except (
        FileNotFoundError,
        json.JSONDecodeError
    ):

        data = []

    # Filter riwayat berdasarkan username
    data_user = []

    for item in data:

        if item.get("username") == current_username:

            data_user.append(item)

    # Jika belum ada riwayat
    if len(data_user) == 0:

        text_riwayat.insert(
            tk.END,
            "Belum ada riwayat aktivitas."
        )

    else:

        # Menampilkan dari yang terbaru
        data_user.reverse()

        for nomor, item in enumerate(
            data_user,
            start=1
        ):

            text_riwayat.insert(
                tk.END,
                f"Riwayat #{nomor}\n"
            )

            text_riwayat.insert(
                tk.END,
                f"Username : {item.get('username')}\n"
            )

            text_riwayat.insert(
                tk.END,
                f"Fitur    : {item.get('fitur')}\n"
            )

            text_riwayat.insert(
                tk.END,
                f"Input    : {item.get('input')}\n"
            )

            text_riwayat.insert(
                tk.END,
                f"Hasil    : {item.get('hasil')}\n"
            )

            text_riwayat.insert(
                tk.END,
                f"Waktu    : {item.get('waktu')}\n"
            )

            text_riwayat.insert(
                tk.END,
                "-" * 60 + "\n\n"
            )

    # Agar tidak bisa diedit
    text_riwayat.config(
        state="disabled"
    )


# =========================================================
# LOGOUT
# =========================================================

def logout():

    global current_username

    jawaban = messagebox.askyesno(
        "Logout",
        "Apakah kamu yakin ingin logout?"
    )

    if jawaban:

        current_username = ""

        main_window.destroy()

        buat_login()


# =========================================================
# LOGIN GUI
# =========================================================

def buat_login():

    global login_window
    global entry_username
    global entry_password

    login_window = tk.Tk()

    login_window.title(
        "System Authentication"
    )

    login_window.geometry(
        "400x400"
    )

    login_window.resizable(
        False,
        False
    )

    tk.Label(
        login_window,
        text="SYSTEM AUTHENTICATION",
        font=("Arial", 20, "bold")
    ).pack(pady=30)

    # Username
    tk.Label(
        login_window,
        text="Username"
    ).pack()

    entry_username = tk.Entry(
        login_window,
        width=30
    )

    entry_username.pack(pady=8)

    # Password
    tk.Label(
        login_window,
        text="Password"
    ).pack()

    entry_password = tk.Entry(
        login_window,
        width=30,
        show="*"
    )

    entry_password.pack(pady=8)

    # Login
    tk.Button(
        login_window,
        text="LOGIN",
        width=25,
        height=2,
        command=login
    ).pack(pady=15)

    # Registrasi
    tk.Button(
        login_window,
        text="BUAT AKUN BARU",
        width=25,
        height=2,
        command=buka_registrasi
    ).pack(pady=5)

    # Keluar
    tk.Button(
        login_window,
        text="KELUAR",
        width=25,
        command=login_window.destroy
    ).pack(pady=10)

    login_window.mainloop()


# =========================================================
# PROGRAM UTAMA
# =========================================================

if __name__ == "__main__":

    # Membuat database
    inisialisasi_database()

    # Membuka halaman login
    buat_login()
