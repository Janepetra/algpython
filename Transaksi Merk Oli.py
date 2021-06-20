#menghitung transaksi merk oli di bengkel motor UD Matahari
jwb = "Y"
while jwb== "Y" or jwb=="y":
    oli = ['Duration SW20 1L','Castrol Magnatec 1L','Federal Supreme XX 1L','Yamalube 1L','Shell 1L']
    harga = [53000,50000,54000,45000,46000]
    print("------------------------------------------------")
    print("       Transaksi Bengkel Motor UD Matahari      ")
    print("------------------------------------------------")
    print("Kode 1 ",oli[0],"Harga = Rp {:,}" .format(int(harga[0])).replace(',','.'))
    print("Kode 2 ",oli[1],"Harga = Rp {:,}" .format(int(harga[1])).replace(',','.'))
    print("Kode 3 ",oli[2],"Harga = Rp {:,}" .format(int(harga[2])).replace(',','.'))
    print("Kode 4 ",oli[3],"Harga = Rp {:,}" .format(int(harga[3])).replace(',','.'))
    print("Kode 5 ",oli[4],"Harga = Rp {:,}" .format(int(harga[4])).replace(',','.'))
    print("================================================")
    pilihan = input(">> Masukkan Kode Merk Oli = ")
    jmlholi = input(">> Masukkan Jumlah Barang = ")
    #identifikasi pilihan
    idx = 0
    while idx >=0 and idx < 5 :
        idx = idx + 1
        if idx == 0 :
            pilihan = 1
            break
        else:
            idx = int(pilihan) - 1
            break      
    #hitung transksi
    totAwal = int(harga[idx]) * int(jmlholi)
    ppn = int(totAwal * 0.01)
    if totAwal>200000:
        nilaiDisc = int(totAwal * 0.05)
        totalharga = int(totAwal - nilaiDisc + ppn)
    else:
        nilaiDisc = 0
        totalharga = int(totAwal - nilaiDisc + ppn)

    #tampilkan total ongkir
    print("================================================")
    print(">> Merk Oli        = " + oli[idx])
    print(">> Harga           = Rp {:,}" .format(int(harga[idx])).replace(',','.'))
    print(">> Total Barang    = " + str(jmlholi))
    print(">> Total Harga     = Rp {:,}" .format(int(totalharga)).replace(',','.'))
    print("------------------------------------------------")
    
    #inputan untuk break
    jwb = input (">> Transaksi lagi? Y/T = ")
    if jwb== "T" or jwb== "t":
        break