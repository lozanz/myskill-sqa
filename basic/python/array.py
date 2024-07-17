mobil = ["Avanza", "Yaris", "Alya"]
# Mengambil elemen pertama pada list
mobil[0] = "bebek"
# Mengisi elemen list dengan "Veloz"
# mobil = ["Avanza", "Yaris", "Alya"]
mobil.append("Veloz")
# Membuat list kosong
array_kosong = []
# Mencetak semua elemen list
# mobil = ["Avanza", "Yaris", "Alya", "Veloz"]
#hapus
# del mobil[1]
#hapus paling belakang
# mobil.pop()
#hapus paling depan
mobil=mobil[1:]
for i in range(len(mobil)):
    print("Cetak mobil ke-" + str(i) + ": " + mobil[i])