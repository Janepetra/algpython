jwb = "Y"
while jwb== "Y" or jwb=="y":
    print("----------------------------------------------------------------------")
    print("                 Kantin Fakultas Teknologi Informasi                  ")
    print("----------------------------------------------------------------------")
    print("======================================================================")
    print("          Menu Makanan                        Menu Minuman") 
    print("|Kode|Nama Makanan     |Harga |   |Kode|Nama Minuman           |Harga|")
    print("|A.  |Nasi Goreng      |15.000|   |G.  |Teh Dingin/Hangat/panas|2.500|")
    print("|B.  |Lontong Goreng   |14.900|   |H.  |Kopi Dingin            |5.000|") 
    print("|C.  |Bakso Goreng     |12.900|   |I.  |Kopi Teh Panas         |6.500|") 
    print("|D.  |Rujak Goreng     |13.000|   |J.  |Coca Cola Dingin       |3.500|") 
    print("|E.  |Rujak Bakso      |15.000|   |K.  |Coca Cola Panas        |5.000|") 
    print("|F.  |Rujak Bakso Pecel|17.000|") 
    print("======================================================================")
    
    kode = ['a','b','c','d','e','f','g','h','i','j','k']
    namaPesanan = ['Nasi Goreng','Lontong Goreng','Bakso Goreng','Rujak Goreng','Rujak Bakso','Rujak Bakso Pecel',
                   'Teh Dingin/Hangat/panas','Kopi Dingin','Kopi Teh Panas','Coca Cola Dingin','Coca Cola Panas']
    harga = [15000,14900,12900,13000,15000,17000,2500,5000,6500,3500,5000]
    pilihan = input(">> Masukkan Kode Pesanan   = ")
    qty     = input(">> Masukkan Jumlah Pesanan = ")

    i = 0;
    while i < 11:
        if kode[i]==pilihan:
            nama_Pesanan = namaPesanan[i]
            hrgsat = harga[i]
        i = i + 1;

    totAkhir = hrgsat * int(qty)
    print("-----------------------------------")
    print(">> Nama Pesanan   :", nama_Pesanan)
    print(">> Harga Pesanan  : Rp {:,}" .format(int(hrgsat)).replace(',','.'))
    print(">> Jumlah Pesanan :", qty)
    print("-----------------------------------")
    print(">> Total Biaya    : Rp {:,}" .format(int(totAkhir)).replace(',','.'))
    print("-----------------------------------")
    bayar = int(input(">> Bayar          : Rp "))
    kembalian = bayar - totAkhir 
    print(">> Kembalian      : Rp {:,}" .format(int(kembalian)).replace(',','.'))
    print("-----------------------------------")
    print("            Terima Kasih           ")
    print("-----------------------------------")

    jwb = input (">> Transaksi lagi? Y/T = ")
    if jwb== "T" or jwb== "t":
        break