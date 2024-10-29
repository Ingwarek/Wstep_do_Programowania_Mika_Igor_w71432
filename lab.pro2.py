# zadanie8
wiek = int(input("Podaj swoj wiek"))
if wiek >= 18:
    print("uzytkownik jest pelnoletni")
else:
    print("uzytkownik jest niepelnoletni")

# zad9
wiek2 = int(input("Podaj swoj wiek"))

if wiek2 <= 4:
    print("Wstęp bezpłatny")
elif wiek2 < 18:
    print("bilet kosztuje 10 zl")
elif wiek2 >= 18:
    student = str(input("Czy jestes studentem?"))
    if student == "tak" or student == "TAK" or student == "Tak":
        print("Koszt biletu to 15 zl")
    else:
        print("Koszt biletu to 20 zl")
#zadanie 10
x = int(input("podaj pierwsza liczbe:"))
y = int(input("podaj druga liczbe: "))
z = int(input("podaj trzecia liczbe :"))

if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y
print("Liczby w kolejności od najmniejszej do najwiekszej to:", x, y , z)
#zadanie 11
import math
a = int(input("Podaj liczbe a:"))
b = int(input("Podaj liczbe b:"))
c = int(input("Podaj liczbe c:"))
delta = b**2 -4*a*c
if delta > 0:
    x1 = (-b-math.sqrt(delta))/(2*a)
    x2 = (-b+math.sqrt(delta))/(2*a)
    print(f"Miejsce zerowe: x1 = {x1}, x2 = {x2}")
elif delta == 0:
    x3 = -b/(2*a)
    


