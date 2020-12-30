buka = open('d:\latihan5.txt','r')
tambah = open('d:\latihan5_hasil.txt','a')
read = buka.readlines()

for x in range(len(read)) :
    bilangan= read[x]
    kiri,kanan = bilangan.split('|')
    jumlah = int(kiri) + int(kanan)
    tambah.write(str(jumlah))
    tambah.write('\n')
    
tambah.close()
hasil = open('d:\latihan5_hasil.txt','r')

hasil = open('d:\latihan5_hasil.txt','r')
print(hasil.read())
hasil.close

