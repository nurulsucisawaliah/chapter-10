#memasukkan input NIM
search = input("Masukkan NIM yang mau dicari : ")
#membuka file
buka = open("d:\latihan2.txt", 'r')
#membaca file
baca_lines = buka.readlines()
for x in range(len(baca_lines)) :
    mhs = baca_lines[x]
    value,values,valuess= mhs.split("|")
    if (value == search) :
        data = "Ada"
        print("Data Mahasiswa")
        print("NIM   : ", value)
        print("Nama  : ", values)
        print("Alamat:", valuess)
        break
    else :
        print ("Data mahasiswa tidak ditemukan")

