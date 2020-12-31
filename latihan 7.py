# membuka file
buka = open("d:\hasilPenyandian", 'r')
#menginput nilai n
n = int(input('nilai n : '))
#membaca file
baca = buka.read()
baca_list = list(baca)
isi = []

for m in baca_list :
    if (m == ' ') :
        x = ord(m)
    else :
        i = ord(m)
        x = i - n
        if (d < 65) :
            d = x + 26
        elif (90 < x and x <97) :
            x = x + 26
    kars = chr(x)
    isi.append(kars)
joined = ','.join(isi)

#menambahkan file
buka_open = open('latihan7.txt', 'w')
buka_open.write(joined)
buka_open.close()
    
