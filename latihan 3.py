buka = open("d:\latihan2.txt" , 'r')
data = buka.readlines()

data_Mhs = {}
for x in range(len(data)) :
    mhs = data[x]
    value,values,valuess = mhs.split('|')
    a,b,c= value,values,valuess.replace('\n', '')
    data_mahasiswa = {'nim' : value, 'nama' : values, 'alamat' : valuess}
    data_Mhs[value] = data_mahasiswa

print(data_Mhs)
buka.close
