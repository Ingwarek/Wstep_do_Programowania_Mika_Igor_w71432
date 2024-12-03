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
#zad4

from datetime import datetime, timedelta

def oblicz_czas(ostatnie_laboratoria, data_kolokwium):

    try:
        data_lab = datetime.strptime(ostatnie_laboratoria, "%Y-%m-%d")
        data_kol = datetime.strptime(data_kolokwium, "%Y-%m-%d")
        dzis = datetime.today()
        
        dni_od_lab = (dzis - data_lab).days
        dni_do_kol = (data_kol - dzis).days
        
        print(f"Ostatnie laboratoria odbyły się {dni_od_lab} dni temu.")
        if dni_do_kol > 0:
            print(f"Do kolokwium pozostało {dni_do_kol} dni.")
        elif dni_do_kol == 0:
            print("Kolokwium jest dzis")
        else:
            print(f"Kolokwium odbyło się {-dni_do_kol} dni temu.")
    except ValueError:
        print("zly format użyj formatu YYYY-MM-DD.")


ostatnie_laboratoria = input("Podaj date ostatnich laboratoriow (YYYY-MM-DD): ")
data_kolokwium = input("Podaj date kolokwium (YYYY-MM-DD): ")
oblicz_czas(ostatnie_laboratoria, data_kolokwium)

