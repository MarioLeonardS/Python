#String format adalah teknik untuk menggabungkan variabel atau nilai dengan teks pada tempat yang telah ditentukan dalam sebuah string, sehingga Anda dapat dengan mudah memanipulasi dan menyusun teks yang dinamis
#Contoh : Membuat teks yang menyapa nama 
nama_depan = "Mario"
nama_tengah = "Leonard"
nama_belakang =  "Salim"

#Contoh tanpa penggunaan String Format
sapa = "Halo" + " " + nama_depan + " " + nama_tengah + " " + nama_belakang
print(sapa)

#Contoh pengguaan String Format
sapa = f"Halo {nama_depan} {nama_tengah} {nama_belakang}"
print(sapa)
#Hasilnya akan sama

#Fungsi "f" pada string format adalah umtuk menandai bahwa string{nama_depan} adalah string format. Tanpa tanda "f" maka string akan terbaca sebagai teks biasa
nama = "{nama_depan}"
print(nama)

#Fungsi tanda kurung kurawal {} adalah untuk mensubtitusikan variable yang sudah ada, contoh kita mau mensubtitusikan variable nama_depan ke variable sapa, berarti codenya yaitu (sapa = f"{nama_depan})

sapa = f"{nama_depan}"
print(sapa)