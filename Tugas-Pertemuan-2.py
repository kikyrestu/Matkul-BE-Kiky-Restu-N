# Script 1: Pengecekan total belanja
def cek_total_belanja():
    total_belanja = float(input("Masukkan total belanja: "))
    if total_belanja > 100000:
        print("Selamat, Anda dapat hadiah!")
    else:
        print("Terimakasih sudah berbelanja")
    print("Selesai")

# Script 2: Pengecekan password
def cek_password():
    password = input("Masukkan password: ")
    if password == "12345678":  # Ganti dengan password yang sesuai
        print("Selamat datang")
    else:
        print("Password salah")
    print("Terimakasih sudah menggunakan aplikasi kami")
    print("Selesai")

# Pilih script yang ingin dijalankan
pilihan = input("Pilih script (1 untuk cek belanja, 2 untuk cek password): ")
if pilihan == "1":
    cek_total_belanja()
elif pilihan == "2":
    cek_password()
else:
    print("Pilihan tidak ada")
