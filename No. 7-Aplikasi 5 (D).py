#penilaian mahaiswa
print ("-------------------------------")
print ("    Menampilkan Nilai Huruf    ")
print ("-------------------------------")
jwb = "Y"
while jwb== "Y" or jwb== "y":
    n=1
    while int(n)>0 and int(n)<=100:
        #input nilai
        n = input (">> Masukkan Nilai = ")
        #cek batasan nilai
        if int(n)>0 and int(n)<=100:
            if int(n)>=90: 
                sts="=> A"
            elif int(n)>=81 and int(n)<91: 
                sts="=> B"
            elif int(n)>=71 and int(n)<81: 
                sts="=> C"
            else: 
                sts="=> D"
            print (sts)
            #inputan untuk break
            jwb = input (">> Ulang Program? Y/T = ")
            if jwb =="T" or jwb =="t":
                break
        else:
            pesan=("=> Masukkan nilai hanya 0-100")
            print (pesan)
            break