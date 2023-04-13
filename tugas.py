class atm:
    def __init__(self):
        self.kartu=eval(input("MASUKAN NO REKENING ANDA : "))
        self.pin=eval  (input("MASUKAN NO PIN ANDA  : "))
    def kartu(self):
        print(self.kartu,self.pin)
    def pin(self):
        print(self.pin,self.katu)
option1=(input("SILAHKAN PILIH BAHASA  :"))
obj=atm()
print("1.________CEK SALDO__________")
print("2._______TARIK TUNAI_________")
print("3._______SETOR TUNAI__________")
option2=int(input(' PILIH TRANSAKSI YANG ANDA INGINKAN :'))
uang_kamu=800000
if option2==1:
    print('SALDO REKENING ANDA Rp.800.000')
elif option2==2:
    print('UANG ANDA BERJUMLAH Rp.800.000, SILAHKAN PILIH JUMLAH PENARIKAN?')
    print('1. Rp.200.000')
    print('2. Rp.100.000')
    option2=int(input('MASUKAN JUMLAH PENARIKAN TUNAI YANG ANDA INGINKAN:'))
    if option2==1:
        hasil=uang_kamu-200000
        print('UANG ANDA SEKARANG BERJUMLAH', hasil)
    elif option2==2:
        hasil2=uang_kamu-100000
        print('UANG ANDA SEKARANG BERJUMLAH', hasil2)
    else:
        print('PILIHAN ANDA SALAH, MOHON ULANGI LAGI  !')
elif option2==3:
    print('SALDO REKENING ANDA Rp.800.0000')
    option3=int(input('SILAHKAN MASUKAN UANG YANG AKAN DISETOR :'))
    hasil3=uang_kamu+option3
    print('SALDO REKENING ANDA ',hasil3)
else:
    print("PILIHAN ANDA SALAH, SILAHKAN ULANGI LAGI !")
        