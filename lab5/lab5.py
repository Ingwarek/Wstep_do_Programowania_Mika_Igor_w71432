# #zad1
# import random
# numerek = random.randint (a:1, b: 22)
# print("dzisiejszy szczesliwy numerek to :",numerek)
#b
# import random
# roczniki = [2000,2001,2002,2003,2004,2005]
# szczesliwy_rocznik = random.choice(roczniki)
# print(szczesliwy_rocznik)
#zad2
#c
# import math
# w1 = math.sqrt(2) + math.sqrt(3) + math.sqrt(6)
# w1 = math.floor(w1)
# print(w1)
# print(math.sqrt(2))
# print(math.sqrt(3))
# print(math.sqrt(6))
#zad3

# import time

# def sekundnik(czas):

#     if czas <= 0:
#         print("Czas musi byc liczba dodatnia")
#         return
#     for sekunda in range(czas, 0, -1):
#         print(f"Pozostalo: {sekunda} sekund.")
#         time.sleep(1)
#     print("Czas uplynal")

# try:
#     czas = int(input("Podaj czas do odliczenia: "))
#     sekundnik(czas)
# except ValueError:
#     print("Podaj liczbe")

# #zad4

# from datetime import datetime, timedelta

# def oblicz_czas(ostatnie_laboratoria, data_kolokwium):

#     try:
#         data_lab = datetime.strptime(ostatnie_laboratoria, "%Y-%m-%d")
#         data_kol = datetime.strptime(data_kolokwium, "%Y-%m-%d")
#         dzis = datetime.today()
        
#         dni_od_lab = (dzis - data_lab).days
#         dni_do_kol = (data_kol - dzis).days
        
#         print(f"Ostatnie laboratoria odbyły się {dni_od_lab} dni temu.")
#         if dni_do_kol > 0:
#             print(f"Do kolokwium pozostało {dni_do_kol} dni.")
#         elif dni_do_kol == 0:
#             print("Kolokwium jest dzis")
#         else:
#             print(f"Kolokwium odbyło się {-dni_do_kol} dni temu.")
#     except ValueError:
#         print("zly format użyj formatu YYYY-MM-DD.")


# ostatnie_laboratoria = input("Podaj date ostatnich laboratoriow (YYYY-MM-DD): ")
# data_kolokwium = input("Podaj date kolokwium (YYYY-MM-DD): ")
# oblicz_czas(ostatnie_laboratoria, data_kolokwium)

#zad5

# import keyword

# def kluczowe(slowa):

#     for slowo in slowa:
#         if keyword.iskeyword(slowo):
#             print(f"'{slowo}' jest slowem kluczowym.")
#         else:
#             print(f"'{slowo}' NIE jest slowem kluczowym.")

# slowa_spr = ["for", "print", "break", "done", "bad"]

# kluczowe(slowa_spr)

#zad6

# import math
# import keyword


# def fmodulu(modul, nmodulu):

#     funkcje = dir(modul)
#     print(f"Funkcje w module '{nmodulu}':")
#     for funkcja in funkcje:
#         print(funkcja)
#     print("\n")  

# fmodulu(math, "math")
# fmodulu(tuple, "tuple")  
# fmodulu(keyword, "keyword")
#zad10
import random
import math

def srednia_geometryczna(krotka):
    if len(krotka) == 0 or any(x <= 0 for x in krotka):
        print("Wszystkie elementy  musza byc dodatnie")
        return
    iloczyn = 1
    for liczba in krotka:
        iloczyn *= liczba
    srednia = iloczyn ** (1 / len(krotka))
    print(f"Srednia geometryczna krotki {krotka} wynosi: {srednia:.2f}")

try:
    dolny_zakres = int(input("Podaj dolna granice : "))
    gorny_zakres = int(input("Podaj gorna granice : "))
    if dolny_zakres >= gorny_zakres:
        print("Dolna granica ma byc mniejsza")
    else:
        krotka = tuple(random.randint(dolny_zakres, gorny_zakres) for _ in range(10))
        print(f"Wylosowana krotka: {krotka}")
        srednia_geometryczna(krotka)
except ValueError:
    print("Prosze podac liczby ")
