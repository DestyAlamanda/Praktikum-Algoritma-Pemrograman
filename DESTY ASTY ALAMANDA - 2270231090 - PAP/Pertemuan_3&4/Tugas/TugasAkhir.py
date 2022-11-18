print("==================== HI BEASTIE ==========================")
print("                 BEAUTY BY ALAMANDA          ")
print("      Jalan Raya Jatiwaringin, RT. 03 / RW. 04")
print("Jaticempaka, Kec. Pd. Gede, Kota Bks, Jawa Barat 13077")
print("==========================================================")

print("==========================================================")
print("                      PRICE LIST                          ")
print("                   EYELASH EXTENSION                      ")
print("==========================================================")
print(" Nomor                  Jenis                   Harga     ")
print("==========================================================")
print(" 01                     Single                  Rp.85000  ")
print(" 02                     Cat Eye                 Rp.100000 ")
print(" 03                     Russian                 Rp.140000 ")
print("==========================================================")

import datetime
Tanggal= datetime.datetime.today()
Nama_Pembeli=str(input("Nama Pembeli      : "))
Telfon=str(input("No.Telp           : "))
Pembayaran=str(input("Metode Pembayaran : "))
Banyak_Pesanan=int(input("Banyak Pesanan    : "))
Nomor_Pesanan=[]
Jumlah_Banyak=[]
Jenis_Pesanan=[]
Jumlah_Bayar=[]
Uang_Bayar=[]
Uang_Kembali=[]
Harga=[]
Jumlah=[]

i=0
while i<Banyak_Pesanan :
    print("pesanan ke-", i+1)

    Nomor_Pesanan.append(input("Nomor Pesanan : "))
    Jumlah_Banyak.append(int(input("Jumlah Banyak : ")))
    if Nomor_Pesanan[i] =="01" :
        Jenis_Pesanan.append("Single ")
        Harga.append("85000 ")
        Jumlah.append(Jumlah_Banyak[i]*int("85000     "))
    elif Nomor_Pesanan[i]=="02" :
        Jenis_Pesanan.append("Cat Eye")
        Harga.append("100000")
        Jumlah.append(Jumlah_Banyak[i]*int("100000"))
    elif Nomor_Pesanan[i]=="03" :
        Jenis_Pesanan.append("Russian")
        Harga.append("140000")
        Jumlah.append(Jumlah_Banyak[i]*int("140000 "))    
    else:
        Jenis_Pesanan.append("BELUMTERSEDIA")
        Harga.append("0")
        Jumlah.append(Jumlah_Banyak[i]*int("0"))
    i=i+1
def menu() :
    print("=======================STRUK BELANJA===========================")
    print("                     BEAUTY BY ALAMANDA          ")
    print("         Jalan Raya Jatiwaringin, RT. 03 / RW. 04")
    print("   Jaticempaka, Kec. Pd. Gede, Kota Bks, Jawa Barat 13077")
    print("===============================================================")
    print("Nama Pembeli      : {}".format(Nama_Pembeli))
    print("No. Telp          : {}".format(Telfon))
    print("Metode Pembayaran : {}".format(Pembayaran))
    print("Tanggal           : {}".format(Tanggal))
    print("================================================================")
    print(" No   Jenis             Harga           Jumlah         Jumlah")
    print("                                        Banyak         Harga ")
    print("================================================================")
menu()
Jumlah_Bayar=0
p=0
while p<Banyak_Pesanan :
    Jumlah_Bayar=Jumlah_Bayar+Jumlah[p]
    print(" %i   %s            %s            %i            %i"%(p+1, Jenis_Pesanan[p],Harga[p],Jumlah_Banyak[p], Jumlah[p]))
    p = p+1
print("================================================================")
print("                                 Harga Total     : Rp." , Jumlah_Bayar)
bayar = int(input("                                 Yang dibayarkan : Rp. "))
Uang_Kembali = bayar-Jumlah_Bayar
print("                                 Uang Kembali    : Rp." , Uang_Kembali)

print("================================================================")
print("===================== THANK YOU FOR COMING =====================")