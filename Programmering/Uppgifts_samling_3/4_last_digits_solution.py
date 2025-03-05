# Skriv en funktion som tar en lista med heltal, vart och ett med en eller flera
# siffror. Funktionen ska byta ut vart och ett av talen mot talets sista siffra,
# entalssiffran. Funktionen ska alltså förändra listans innehåll men inte
# returnera något.

def last_digits(lst):
    for i in range(len(lst)):
        lst[i] = lst[i] % 10


if __name__ == '__main__':
    values = [133, 4, 90, 36, 9, 84, 572]
    last_digits(values)
    print(values)    # [3, 4, 0, 6, 9, 4, 2]

    import random
    permutation = list(range(10))
    random.shuffle(permutation)
    print(permutation)
    numbers = random.sample(range(0, 10000), 15)
    print(numbers)

    l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    l2 = [3, 6, 4, 0, 2, 1, 7, 9, 5, 8]
    l3 = [4, 3, 6, 4, 0, 3, 2, 9, 2, 1, 7, 9, 8, 5, 8, 1, 6, 0, 5, 7]
    l1_backup = l1.copy()
    l2_backup = l2.copy()
    l3_backup = l3.copy()
    assert last_digits(l1) is None
    assert last_digits(l2) is None
    assert last_digits(l3) is None
    for item, backup in zip(l1, l1_backup):
        assert item == backup
    for item, backup in zip(l2, l2_backup):
        assert item == backup
    for item, backup in zip(l3, l3_backup):
        assert item == backup

    l1 = [39, 87, 95, 17, 22, 24, 46, 50, 10, 47]
    l2 = [55, 94, 35, 36, 76, 38, 48, 11, 10, 53, 62, 21, 26, 39, 70]
    l3 = [20, 75, 60, 50, 54, 91, 17, 31]
    l1_backup = l1.copy()
    l2_backup = l2.copy()
    l3_backup = l3.copy()
    assert last_digits(l1) is None
    assert last_digits(l2) is None
    assert last_digits(l3) is None
    for item, backup in zip(l1, l1_backup):
        assert item == backup % 10
    for item, backup in zip(l2, l2_backup):
        assert item == backup % 10
    for item, backup in zip(l3, l3_backup):
        assert item == backup % 10

    l1 = [452, 7, 7914, 117, 16078, 25, 180, 648, 78, 639, 41, 17]
    l2 = [821, 24, 84, 450, 6, 3406, 18, 933, 72, 4, 7469, 91, 156, 863, 61]
    l3 = [63, 5, 7558, 102, 6202, 424, 8082, 9, 402, 39, 9017, 5, 516, 18, 866]
    l1_backup = l1.copy()
    l2_backup = l2.copy()
    l3_backup = l3.copy()
    assert last_digits(l1) is None
    assert last_digits(l2) is None
    assert last_digits(l3) is None
    for item, backup in zip(l1, l1_backup):
        assert item == backup % 10
    for item, backup in zip(l2, l2_backup):
        assert item == backup % 10
    for item, backup in zip(l3, l3_backup):
        assert item == backup % 10