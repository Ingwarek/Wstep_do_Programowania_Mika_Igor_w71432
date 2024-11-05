#zad1
#imiona = []
#for i in range(4):
#    imie = input(f"Podaj imie osoby {i + 1}: ")
#    imiona.append(imie)
#imiona.sort()
#print("Lista po sortowaniu:", imiona)

#imiona.append(input("Podaj imie numer 5: "))
#imiona.append(input("Podaj imie numer 6: "))
#print("Lista po dodaniu dwoch osob:", imiona)
#imiona.pop()
#print("Lista po usunieciu ostaniego imiona:", imiona)

#imiona.insert(2, input("Podaj imie osoby do dodania na 3 pozyjce:"))
#print("Lista po dodaniu osoby na trzecia pozycje:", imiona)
#imiona.reverse()
#print("Lista po odwroceniu kolejnosci:",imiona)

#imiona *= 2
#print("Lista po zdublowaniu:", imiona)

#zad 4
#n1 = 3
#x1 = 6
#lista = []
#slowo = ""
#dlugosc_slowa = 0

#for i in range(n):

#zad 5
#lista zakupow
#zakupy={"chleb":5.0, "maslo":7.0, "czekolada":12.0, "czipsy":12.0, "woda":2.0}
#suma_zakupy = 0

#for el in zakupy:
    
#     suma_zakupy += zakupy[el]
#     print(f"{el} za {zakupy[el]} zl")
# print(f"Za zakupy zaplacimy: {suma_zakupy} zl.")


#zad7
zbior_x = {5,6,1}
zbior_y = {3,5,7,9,1,4,6}
print(5 in zbior_x)

print(zbior_x.issubset(zbior_y))

print(zbior_y.issubset(zbior_x))

print(zbior_x.union(zbior_y))

print(zbior_x.difference(zbior_y))

print(zbior_y.difference(zbior_x))

print(zbior_x.intersection(zbior_y))

