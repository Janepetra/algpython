import datetime
jwb = "Y"
while jwb== "Y" or jwb=="y":
    print("         SLIP GAJI         ")
    x = datetime.datetime.now()
    print(x)

    nama = input("Nama             = ")
    golongan = input("Golongan         = ")
    jenisKlmn = input("Jenis Kelamin    = ")
    status = input("Status Kawin     = ")

    #GAJI POKOK
    kodeGol = ['1','2','3']
    gajiPokok = [2500000,4500000,6500000]

    i = 0;
    while i < 3:
        if kodeGol[i]==golongan:
            gaji_pokok = gajiPokok[i]
        i = i + 1;
    
    #TUNJANGAN ISTRI
    if jenisKlmn=="laki laki" and status=="kawin":
        if golongan==1:
            tunjIstri = 0.01*gaji_pokok
        elif golongan==2:
            tunjIstri = 0.03*gaji_pokok
        elif golongan==3:
            tunjIstri = 0.05*gaji_pokok
        else:
            tunjIstri=0
    else:
        tunjIstri=0
    
    #TUNJANGAN ANAK
    if status=="kawin" or status=="KAWIN":
        tunjAnak=0.02*gaji_pokok
    else:
        tunjAnak=0
    
    #GAJI BRUTO
    gajiBruto = gaji_pokok + tunjIstri + tunjAnak

    #BIAYA JABATAN
    biayaJbtnAwal = gajiBruto*0.05
    biayaJabatan = gajiBruto - biayaJbtnAwal

    #IURAN PENSIUN
    iuranPensiun = 15500

    #IURAN ORGANISASI
    iuranOrganisasi = 3500

    #GAJI NETTO
    gajiNetto = gajiBruto - iuranPensiun - iuranOrganisasi

    print("Gaji Pokok       = Rp {:,}" .format(int(gaji_pokok)).replace(',','.'))
    print("Tunjangan Istri  = Rp {:,}" .format(int(tunjIstri)).replace(',','.'))
    print("Tunjangan Anak   = Rp {:,}" .format(int(tunjAnak)).replace(',','.'))
    print(">>Gaji Bruto     = Rp {:,}" .format(int(gajiBruto)).replace(',','.'))
    print("Biaya Jabatan    = Rp {:,}" .format(int(biayaJabatan)).replace(',','.'))
    print("Iuran Pensiun    = Rp {:,}" .format(int(iuranPensiun)).replace(',','.'))
    print("Iuran Organisasi = Rp {:,}" .format(int(iuranOrganisasi)).replace(',','.'))
    print(">>Gaji Netto     = Rp {:,}" .format(int(gajiNetto)).replace(',','.'))

    jwb = input (">> Transaksi lagi? Y/T = ")
    if jwb== "T" or jwb== "t":
        break