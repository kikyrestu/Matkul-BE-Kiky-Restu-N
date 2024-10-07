def hitung_gaji(golongan, jam_kerja):
    upah_per_jam = {
        'A': 5000,
        'B': 7000,
        'C': 8000,
        'D': 10000
    }
    
    if golongan not in upah_per_jam:
        return "Error: Golongan tidak valid"
    
    gaji_pokok = upah_per_jam[golongan] * jam_kerja
    
    if jam_kerja > 48:
        uang_lembur = (jam_kerja - 48) * 4000
        total_gaji = gaji_pokok + uang_lembur
    else:
        total_gaji = gaji_pokok
    
    return total_gaji

print("Program Python Menghitung Gaji Karyawan")
print("-" * 40)

nama = input("Nama karyawan: ")
golongan = input("Golongan: ").upper()
jam_kerja = int(input("Jumlah jam kerja: "))

gaji = hitung_gaji(golongan, jam_kerja)

print("\nHasil Perhitungan Gaji:")
print("-" * 40)
print(f"{'Nama Karyawan':<20}: {nama}")
print(f"{'Golongan':<20}: {golongan}")
print(f"{'Jumlah Jam Kerja':<20}: {jam_kerja}")
print(f"{'Total Gaji':<20}: Rp {gaji:,}")
print("-" * 40)