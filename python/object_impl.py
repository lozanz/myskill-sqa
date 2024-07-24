#penggunaan keyword this
class Person:
    # Konstruktor
    def __init__(self, firstName, lastName):
# Properti
        self.firstName = firstName
        self.lastName = lastName
# Method
    def full_name(self):
        return f"{self.firstName} {self.lastName}"

    def show_name(self):
        print(self.full_name())
# Membuat objek Person
person1 = Person("Muhar", "Dian")
person2 = Person("Petani", "Kode")
# Memanggil method
person1.show_name()
person2.show_name()

#karyawan
class Karyawan:
    def __init__(self, nama, usia, pendapatan):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan

sharon = Karyawan('Sharon', 22, 6500000)
print(sharon.nama + ', Usia: ' + str(sharon.usia) + ', Pendapatan ' + str(sharon.pendapatan))