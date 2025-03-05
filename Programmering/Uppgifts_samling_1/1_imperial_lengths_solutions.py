# I årskurs 4 i amerikanska skolan lär sig barnen att omvandla mellan olika längdenheter.
# De använder följande formel: 1 ft = 12 in
# Skriv en funktion som läser in ett helt antal inches (in) och omvandlar till feet (ft) och inches (in).
# Funktionen ska returnera en tupel bestående av två tal som motsvarar feet och inches.
def feet_inches(inches):
    feet = inches // 12
    inches = inches % 12
    return feet, inches


if __name__ == '__main__':
    print(feet_inches(27))    # returnerar (2, 3)
    print(feet_inches(93))    # returnerar (7, 9)