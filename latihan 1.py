my_file = open("d:\latihan1.txt", "r")
zero = 0
jumlah = 0
for numbers in my_file:
    bilangan_genap= int(numbers) + 1
    bilanganGanjil = int(numbers) + 1
    if bilangan_genap % 2 == 0:
        zero = zero + 1
    elif bilanganGanjil % 2 == 1:
        jumlah =jumlah + 1
print('Banyaknya bilangan genap : ' + str(zero))
print('Banyaknya bilangan ganjil : ' + str(jumlah))
