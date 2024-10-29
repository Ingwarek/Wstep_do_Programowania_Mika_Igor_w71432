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