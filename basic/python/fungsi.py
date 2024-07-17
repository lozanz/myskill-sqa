#fungsi tanpa parameter
def nama_fungsi():
    print("Hello World!")
# Memanggil fungsi
nama_fungsi()

#fungsi dengan parameter
def kali(a, b):
    hasil_kali = a * b
    print("Hasil kali =", hasil_kali)
# Memanggil fungsi
kali(3, 2) # -> Hasil kali a*b = 6
kali(6,3)

#fungsi mengembalikan nilai
def bagi(a, b):
    hasil_bagi = a / b
    return hasil_bagi
# Memanggil fungsi
nilai1 = 20
nilai2 = 5
hasil_pembagian = bagi(nilai1, nilai2)
print(hasil_pembagian) # -> 4.0