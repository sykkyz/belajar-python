# program ini digunakan untuk mengonversi suhu dari fahrenhit ke kelvin
# program ini digunakan untuk mengonversi suhu dari kelvin dan fahrenheit

import math

print("\n===== PROGRAM KONVERSI SUHU ======\n")

fahrenheit = float(input("Masukkan suhu : "))

# properti math.floor digunakan untuk membulatkan angka ke atas
print("Suhu yang dimasukkan adalah sebesar",math.floor(fahrenheit),"fahrenheit \n")

# base formula : (x °F − 32) × 5/9 + 273,15 = ... K
kelvin = (fahrenheit - 32) * (5/9) + 273.15

print("Suhu dalam kelvin adalah sebesar",kelvin,"kelvin \n")

#base formula : (y K − 273,15) × 9/5 + 32 = ... °F
fahrenHeit = (kelvin - 273.15) * (9/5) + 32

print("Apabila suhu dalam kelvin dikembalikan ke fahrenheit adalah sebesar",math.floor(fahrenHeit),"fahrenheit")
print("\n")