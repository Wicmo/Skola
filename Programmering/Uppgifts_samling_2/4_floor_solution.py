# Skriv en funktion som tar en lista och ett värde m som input. Funktionen ska sätta alla
# element i listan som är mindre än m lika med m och returnera antalet element som ändrats.
# För att förenkla så kan vi anta att alla värden i listan samt värdet m är heltal.
def floor_list(lst, m):
    n = 0
    for i in range(len(lst)):
        if lst[i] < m:
            lst[i] = m
            n += 1
    return n


if __name__ == '__main__':
    values = [25, 10, 31, 49, 28, 17]
    nb_changes = floor_list(values, 20)
    print(nb_changes)  # 2
    print(values)      # [25, 20, 31, 49, 28, 20]
