# start 3.11.26 keep going
def analyze_text(text):
    split = text.split(sep=" ")
    print(split)

    print("Liczba słów: ", len(split))

    dict =[]
    for i in split:
      print(i)
      if i == i:
        dict.append(i)
    print(dict)
    
    

analyze_text(input("Wprowadź tekst: "))