# I årskurs 4 i amerikanska skolan lär sig barnen att omvandla mellan olika volymsenheter.
# De använder följande formel: 1 gallon = 16 cups
# Skriv en funktion som läser in ett helt antal cups och omvandlar till gallons och cups.
# Funktionen ska returnera en tupel bestående av två tal som motsvarar antalet gallons
# respektive antalet cups.
def gallons_cups(cups):
    gallons = cups // 16
    cups = cups % 16
    return gallons, cups


if __name__ == '__main__':
    print(gallons_cups(35))    # returnerar (2, 3)
    print(gallons_cups(93))    # returnerar (5, 13)
    