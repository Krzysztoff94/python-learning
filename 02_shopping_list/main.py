zakupy_lista =[]

wybor = 0

print("1. Dodaj produkt")
print("2. Usun produkt")
print("3. Pokaż listę")
print("4. Wyjdz")

while True:
    wybor = int(input("Wybierz:"))

    if wybor == 1:
        print("Produkt do dodania:")
        zakupy_lista.append(input("Nazwa: "))
    elif wybor == 2:
        print("Produkt do usuniecia:")
        zakupy_lista.remove(input("Nazwa: "))
    elif wybor == 3:
        print(zakupy_lista)
    elif wybor == 4:
        break


    
