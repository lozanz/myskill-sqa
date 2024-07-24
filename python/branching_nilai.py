# Menerima masukan nilai dari pengguna
nilai = float(input('Masukkan nilai: '))
grade = ""
# Memeriksa rentang nilai dan menentukan grade
if nilai > 90:
    grade = "A"
elif nilai > 80:
    grade = "B+"
elif nilai > 70:
    grade = "B"
else:
    grade = "F"
# Menampilkan grade
print("Grade adalah =", grade)