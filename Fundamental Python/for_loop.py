# Belajar For Loop

pelanggan = ["Mario", "Leon", "Salim", "Elder", "Leonard", "MarFly"]
pelanggan.append("Kelvin")
pelanggan.append("Raditya")
pelanggan.append("Nadif")
pelanggan.append("Agil")
pelanggan.append("Fahri")
pelanggan.append("Nabil")

# Cara Mengakses Semua Nama Pelanggan? Kita bisa gunakan fungsi "For"
# Semua aang ada didalam fungsi "For" ini akan mengulangi perintah dari data/index pertama sampai terakhir
for nama in pelanggan: # for (variable baru untuk mengisi data yang dipanggil) in (variable yang ingin diambil datanya)
    print("-------------------------")
    print(f"Nama Pelanggan : {nama}")
    print("-------------------------")