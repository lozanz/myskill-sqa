# Import modul untuk menerima masukan dari pengguna
from getpass import getpass
# Meminta masukan password dari pengguna
username=input('Enter username: ')
password = getpass('Enter password: ')
valid_password = 'password'
# Memeriksa apakah password yang dimasukkan adalah valid
if password == valid_password:
    print("Selamat datang bos!")
else:
    print("Password Salah, coba lagi!")
# Pesan terimakasih
print("Terimakasih sudah menggunakan aplikasi kami")