# pogoda

from temperatura import cf, fc, ck

def main():
    try:
        celsius = 21
        fahrenheit = cf(celsius)
        print(f"{celsius} stopni Celsjusza to {fahrenheit:.2f} stopni Fahrenheita.")
        
        fahrenheit = 89
        celsius = fc(fahrenheit)
        print(f"{fahrenheit} stopni Fahrenheita to {celsius:.2f} stopni Celsjusza.")
    
        celsius = 35
        kelwin = ck(celsius)
        print(f"{celsius} stopni Celsjusza to {kelwin:.2f} Kelwinow.")
    except Exception as e:
        print(f"Wystapil blad: {e}")

if __name__ == "__main__":
    main()
