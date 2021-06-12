#mengencek kelulusan, jika > 60 maka status Lulus
print ("------------------------------")
print ("        Cek Kelulusan         ")
print ("------------------------------")
jwb = "Y"
while jwb== "Y" or jwb=="y":
    #input nilai
    n = input(">> Masukan Nilai = ")
    #cek nilai
    if int(n)>60:
        sts = "=> Lulus"
    else:
        sts = "=> Tidak Lulus"
    print (sts)
    #inputan untuk break
    jwb = input (">> Mulai lagi? Y/T = ")
    if jwb== "T" or jwb== "t":
        break