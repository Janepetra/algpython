#menampilkan nilai huruf
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
            if int(n)>=80: 
                sts="=> Baik Sekali"
            elif int(n)>=65: 
                sts="=> Baik"
            elif int(n)>=55: 
                sts="=> Cukup"
            elif int(n)>=40: 
                sts="=> Kurang"
            else: 
                sts="=> Kurang Sekali"
            print (sts)
            #inputan untuk break
            jwb = input (">> Ulang Program? Y/T = ")
            if jwb =="T" or jwb =="t":
                break
        else:
            pesan=("=> Masukkan nilai hanya 0-100")
            print (pesan)
            break