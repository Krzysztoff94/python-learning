print("==== Cost Analyzer ===")
print("1. Add cost")
print("2. Show all")
print("3. Show sum")
print("4. Show max")
print("5. Show min")
print("6. Show average")
print("7. Exit")

costs = []

def add_cost(costs_list):

    single_cost = {
        'name': input("Give name: "),
        'value': int(input("Give value: ")),
        'category': input("Give category: "),
    }
    costs_list.append(single_cost)
    
while True:
    choose = int(input("Choose: "))
    while True:
        if choose == 1:
            add_cost(costs)
            break
        elif choose == 2:
            print(costs)
            break
        else:
            break
    if choose == 7:
        break