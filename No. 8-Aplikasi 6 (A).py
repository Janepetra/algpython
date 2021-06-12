#Menghitung transaksi pembelian printer
print ("------------------------------------------")
print ("  Menghitung Transaksi Printer Epson T20  ")
print ("------------------------------------------")
jwb = "Y"
while jwb== "Y" or jwb=="y":
    hrgprinter = 660000
    #input jumlah barang
    jmlhbeli = input (">> Masukan Jumlah Printer yang Dibeli = ")
    #menghitung total
    total = int(hrgprinter) * int(jmlhbeli)
    print (">> Total Transaksi = Rp " + str(total))
    #inputan untuk break
    jwb = input (">> Mulai lagi? Y/T = ")
    if jwb== "T" or jwb== "t":
        break
