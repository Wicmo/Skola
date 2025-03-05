# Skriv en funktion som för vart och ett av talen i en lista avrundar nedåt
# till närmaste jämna multipel av ett givet tal n. Funktionen ska ändra listans
# element men inte returnera något.
def floor_multiple(lst, n):
    for i in range(len(lst)):
        lst[i] -= lst[i] % n


if __name__ == '__main__':
    numbers = [13, 7, 25, 83, 16]
    floor_multiple(numbers, 4)
    print(numbers)                    # [12, 4, 24, 80, 16]
    values = [8, 18, 47, 97, 23, 3]
    floor_multiple(values, 3)
    print(values)                     # [6, 18, 45, 96, 21, 3]

    l1 = [259, 3108, 222, 1961, 518, 222]
    floor_multiple(l1, 37)
    print(l1)                         # [259, 3108, 222, 1961, 518, 222]
    l2 = [249, 332, 83, 249, 5976, 83, 747, 913]
    floor_multiple(l2, 83)
    print(l2)                         # [249, 332, 83, 249, 5976, 83, 747, 913]

    l3 = [19, 93, 2, 40, 51, 78, 57, 3, 83, 74, 64, 97, 8, 27, 95, 36, 46, 18, 28, 47]
    floor_multiple(l3, 110)
    print(l3)                         # zeroes
    l4 = [3, 5, 38, 25, 49, 44, 2, 38, 8, 10, 13, 11, 48]
    floor_multiple(l4, 53)
    print(l4)                         # zeroes

    l5 = [23, 65, 63, 70, 42, 99, 60, 90, 38, 44]
    floor_multiple(l5, 8)
    print(l5)                         # [16, 64, 56, 64, 40, 96, 56, 88, 32, 40]
    l6 = [40, 79, 44, 21, 37, 47, 26, 91, 55, 26]
    floor_multiple(l6, 7)
    print(l6)                         # [35, 77, 42, 21, 35, 42, 21, 91, 49, 21]
