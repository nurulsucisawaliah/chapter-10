#Input dari nama file text berisi teks asli
masukkan = input('Masukkan nama file : ')
#Input dari nilai keyword n 
n = int(input('Masukkan nilai n : '))
#membuka file
buka = open(masukkan, 'r')
#membaca file
baca = buka.read()
karakter = list(baca)
isi = []

for x in karakter :
    a_ascii = ord(x)
    if (a_ascii == 32) :
        b_ascii = a_ascii
    else :
        b_ascii = a_ascii +  n

        if (b_ascii > 122) :
            kurang = b_ascii -26
        elif (b_ascii > 90 and b_ascii < 97) :
            b_ascii = b_ascii -26
            
    kar = chr(b_ascii)
    isi = isi + [kar]
    if not karakter :
        break
joined = ''.join(isi)

# menambahkan isi ke dalam file
buka_open = open('hasilPenyandian', 'a')
buka_open.write(joined)
buka_open.close()
        
