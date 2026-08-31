import random

liczba = random.randint(1, 100)
strzal = 0
liczby = []


while strzal != liczba:
    strzal = int(input("Podaj Liczbe:"))

    if strzal in liczby:
        print("Już podawałeś tę liczbę!")
        continue
    liczby.append(strzal)

    if strzal > liczba:
        print("za duzo")
    elif strzal < liczba:
        print("za malo")
    else:
        ilosc = len(liczby)
        print(f"trafiles za {ilosc} razem")
        break
