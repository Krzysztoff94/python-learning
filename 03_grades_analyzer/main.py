print("Witaj w elektronicznym dzienniku")

oceny = []

while True:
    wejscie = input("Podaj ocenę od 1 do 6 (lub wpisz 'koniec'): ")
    
    if wejscie.lower() == "koniec":
        break
        
    if wejscie.isdigit():
        ocena = int(wejscie)
        if 1 <= ocena <= 6:
            oceny.append(ocena)
        else:
            print("Błędna ocena! Wpisz liczbę od 1 do 6.")
    else:
        print("To nie jest poprawna ocena ani słowo 'koniec'.")

print(f"Oceny: {oceny}")

def srednia(lista):
    suma = sum(lista) / len(lista)
    print(f"Średnia: {suma}")
srednia(oceny)

def najwyzsza(lista):
    maks = max(lista)
    print(f"Najwyższa ocena: {maks}")
najwyzsza(oceny)

def najnizsza(lista):
    mininum = min(lista)
    print(f"Najniższa ocena: {mininum}")
najnizsza(oceny)

def pozytywne(lista):
    poz = []
    for i in lista:
        if i >= 3:
            poz.append(i)
    print(f"Pozytywne: {len(poz)}")
pozytywne(oceny)

def neagtywne(lista):
    poz = []
    for i in lista:
        if i < 3:
            poz.append(i)
    print(f"Negatywne: {len(poz)}")
neagtywne(oceny)
