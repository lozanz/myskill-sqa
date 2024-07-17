class Car:
    # Properti
    type = "Fiat"
    model = "500"
    color = "white"
# Method
def start(self):
    print("ini method start")
def drive(self):
    print("ini method drive")
def brake(self):
    print("ini method brake")
def stop(self):
    print("ini method stop")

#akses object
# Membuat objek mobil
car = Car()
print(car.type)
print(car.color)
# Memanggil method
# car.start()
# car.drive()
# car.brake()
# car.stop()
