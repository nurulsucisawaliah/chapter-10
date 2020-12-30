buka = open("d:\latihan2.txt", 'a')
benar = True
while (benar == True) :
    nim = input("masukkan nim : ")
    name = input("masukkan nama mhs : ")
    addres = input("masukkan alamat : ")
    buka.write(nim + "|" + name + "|" + addres + "\n")
    print("")
    ulangi = input("ulangi input lagi (y/n) : ")
    if (ulangi == "y") :
        benar = True
    elif  (ulangi == "n"):
        benar = False
    else:
        print("")
        continue
buka.close()
