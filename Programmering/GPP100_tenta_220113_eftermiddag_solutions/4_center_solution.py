# Ett vanligt steg när man analyserar datamängder är att centrera data, det vill säga att
# istället för mätvärdena ange avståndet från medelvärdet med tecken.
# Vi tar följande lista som exempel: [12, 5, 9, 13, 11]
# medelvärdet är (12 + 5 + 9 + 13 + 11) / 5 = 10
# den centrerade listan blir då [12 - 10, 5 - 10, 9 - 10, 13 - 10, 11 - 10] = [2, -5, -1, 3, 1]
# Skriv en funktion som tar en lista som input och centrerar den runt dess medelvärde.
# Funktionen ska returnera det ursprungliga medelvärdet. Listan som ges som argument ska förändras.
# För att förenkla så är det okej om listans värden är float efter funktionsanropet, även om det var
# int från början.
def center_list(lst):
    mean = sum(lst) / len(lst)
    for i in range(len(lst)):
        lst[i] -= mean
    return mean


if __name__ == '__main__':
    values = [12, 5, 9, 13, 11]
    avg = center_list(values)
    print(avg)       # 10.0
    print(values)    # [2.0, -5.0, -1.0, 3.0, 1.0]

    import random
    my_list = [random.randint(1, 99) for i in range(10)]
    print(my_list)

    l1 = [20.5, 29.5, -9.5, 2.5, -43.5, -29.5, 39.5, -13.5, -3.5, 7.5]
    l1 = [-27.1, -4.1, -10.1, 8.9, -46.1, -6.1, 16.9, 21.9, 13.9, 31.9]
    l1 = [79, 88, 49, 61, 15, 29, 98, 45, 55, 66]
    l1 = [20, 43, 37, 56, 1, 41, 64, 69, 61, 79]
    m1 = center_list(l1)
    print(m1)
    print(l1)
