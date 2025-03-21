# Else adalah suatu kondisi dimana akan dieksekusi jika syarat "If" tidak terpenuhi
# Perintah Else hanya akan berjalan pada if diatasnya salah

print("=== Masukan Nilai ===")
nilai = int(input("Nilai : "))


if nilai == 100:
    print("Perfect!")


if nilai > 75:  # If pertama
    # Jika ada "If" di dalam "If", ini dinamakan Nested If dimana kondisi paling atas akan dijalankan terlebih dahulu, begitu pun selanjutnya
    if nilai != 100:
        print("Bagus") # Kode yang dieksekusi jika kondisi_pertama dan kondisi_kedua benar

elif nilai == 75:
        print("Pas KKM")
        
else: # Perintah Else ini hanya akan berjalan jika perintah IF diatasnya salah (Untuk Nested-If yang utama adalah if yang pertama)
    print("Ayo Coba Lagi")