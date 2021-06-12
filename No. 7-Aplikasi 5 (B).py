#mengecek tingkat usia
print ("-----------------------------")
print ("    Mengecek Tingkat Usia    ")
print ("-----------------------------")
jwb = "Y"
while jwb== "Y" or jwb== "y":
    u=1
    while int(u)>0 and int(u)<=100:
        #input usia
        u = input (">> Masukkan Usia = ")
        #cek batasan usia
        if int(u)>0 and int(u)<=100:
            if int(u)>=60: 
                sts="=> Lansia"
            elif int(u)>=35: 
                sts="=> Dewasa"
            elif int(u)>=18: 
                sts="=> Pemuda"
            elif int(u)>=15: 
                sts="=> Remaja"
            else: 
                sts="=> Anak-anak"
            print (sts)
            #inputan untuk break
            jwb = input (">> Ulang Program? Y/T = ")
            if jwb =="T" or jwb =="t":
                break
        else:
            pesan=("=> Masukkan usia hanya 0-100")
            print (pesan)
            break