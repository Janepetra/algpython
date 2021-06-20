#menghitung biaya total pengiriman barang di perusahaan Ekspedisi Lorena di Malang
jwb = "Y"
while jwb== "Y" or jwb=="y":
    kota = ["Surabaya","Bandung"]
    jarak = [169,452]
    ongkirperkm = [2500,4000]
    print("--------------------------------------------------")
    print("    Transaksi Biaya Ekspedisi Lorena di Malang    ")
    print("--------------------------------------------------")
    print("Kode 1 ",kota[0],"Jarak = ",jarak[0],"Ongkir PerKm = ",ongkirperkm[0])
    print("Kode 2 ",kota[1],"Jarak = ",jarak[1],"Ongkir PerKm = ",ongkirperkm[1])
    print("==================================================")
    pilihan = input(">> Masukkan Kode Tujuan = ")
    #identifikasi pilihan
    idx = 0
    while idx >=0 and idx < 2 :
        idx = idx + 1
        if idx == 0 :
            pilihan = 1
            break
        else:
            idx = int(pilihan) - 1
            break 
    totongkir = jarak[idx]*ongkirperkm[idx]
    #cetak tampilan layar
    print("--------------------------------------------------")
    print(">> Pilihan Tujuan = " + kota[idx])
    print(">> Jarak          = " + str(jarak[idx]) + " Km")
    print(">> Ongkir per km  = Rp {:,}" .format(int(ongkirperkm[idx])).replace(',','.'))
    print("==================================================")
    print(">> Total Biaya    = Rp {:,}" .format(int(totongkir)).replace(',','.'))
    print("--------------------------------------------------")
    #inputan untuk break
    jwb = input (">> Transaksi lagi? Y/T = ")
    if jwb== "T" or jwb== "t":
        break