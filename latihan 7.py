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
        d = ord(m)
    else :
        a = ord(m)
        d = a - n
        if (d < 65) :
            d = d + 26
        elif (90 < d and d <97) :
            d = d + 26
    kars = chr(d)
    isi.append(kars)
joined = ','.join(isi)

#menambahkan file
buka_open = open('latihan7.txt', 'w')
buka_open.write(joined)
buka_open.close()
    
