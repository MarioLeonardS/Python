# Belajar Tipe Data List
# Seperti namanya tipe data ini berfungsi untuk malakukan list pada Index
# Hal ini cukup mempermudah jika ingin membuat variable nama yang banyak

# Membuat List
nama = ["Mario", "Leon", "Salim", "Elder"] # Pada index, nama paling depan berada pada index ke 0 dan seterusnya
# Menambah data
nama.append("Kumar")
# Mengakses List
print(nama[0])
print(nama[1])
print(nama[2])
print(nama[3])
print(nama[4])

# Untuk mengetahui jumlah data pada list, gunakan len(variable)
print(len(nama))

#Untuk menghapus data gunakan perintah variable.remove()
nama.remove("Elder") #Jika data Elder dihapus, maka nama setelah elder akan menempati posisi indexnya. 
print(nama)
print(nama[0])
print(nama[1])
print(nama[2])
print(nama[3]) # Nama elder yang sebelumnya berada pada index 3 diubah/bergeser menjadi milik Kumar

# Jadi jika sebuah data list dihapus, maka data yang ada dibelakang akan maju dan menggantikan index data yang telah dihapus

# Mengubah Data Didalah List (variable[index] = "nama yang baru")
nama[0] = "Mario Leonard Salim"
print(nama)