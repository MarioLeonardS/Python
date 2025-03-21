# Belajar Elif
# Elif adalah perintah yang digunakan untuk mengevaluasi kondisi berurutan setelah kondisi if tidak terpenuhi. 
# Jika ada 3 kondisi IF, pada saat dieksekusi semua if akan terjalankan. Tetapi jika menggunakan elif, kita bisa menghentikan 2 IF lainnya saat IF Pertama Benar.  
# Contoh Pembuatan Menu 

pilihan_menu = int(input("Masukan Menu Yang Ingin Dipilih [1-3] : "))

if pilihan_menu == 1:
    print("Kamu memilih menu 1")

elif pilihan_menu == 2:
    print("Kamu memilih menu 2")

elif pilihan_menu == 3:
    print("Kamu memilih menu 3")

else:
    print("Menu yang kamu pilih tidak tersedia")