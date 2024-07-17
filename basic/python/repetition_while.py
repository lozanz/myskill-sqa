ulangi = input("Are you ready? ") # Input 1
print("Start")
counter = 0
while ulangi:
    jawab = input("Apakah anda mau mengulang? (yes/no) : ") #
counter += 1
if jawab == "no":
    ulangi = False
print("Pengulangan ke-" + str(counter))