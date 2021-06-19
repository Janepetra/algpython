#Menghitung transaksi pembelian printer
print ("------------------------------------------")
print ("  Menghitung Transaksi Printer Epson T20  ")
print ("------------------------------------------")
jwb = "Y"
while jwb== "Y" or jwb=="y":
    hrgPrinter = 660000
    #input jumlah barang
    jmlhbeli = input (">> Masukan Jumlah Printer yang Dibeli = ")
    #menghitung total
    totAwal = int(hrgPrinter) * int(jmlhbeli)
    if totAwal>1500000:
        nilaiDisc = int(totAwal * 0.15)
    else:
        nilaiDisc = 0
    totBayar = int(totAwal) - int(nilaiDisc)
    print (">> Total Transaksi = Rp " + str(totBayar))
    #inputan untuk break
    jwb = input (">> Mulai lagi? Y/T = ")
    if jwb== "T" or jwb== "t":
        break
