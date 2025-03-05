# Skriv en funktion som tar ett ord (string) som input och returnerar samma ord men med varannan
# bokstav liten och varannan bokstav stor. Den första bokstaven ska alltid vara liten. Funktionen
# ska inte ta hänsyn till små och stora bokstäver i det ursprungliga ordet.
def alt_case(word):
    res = ''
    for i in range(len(word)):
        if i % 2 == 0:
            res += word[i].lower()
        else:
            res += word[i].upper()
    return res


if __name__ == '__main__':
    print(alt_case('theory'))     # tHeOrY
    print(alt_case('SAAB'))       # sAaB
    print(alt_case('LÄKEMEDELSUTVECKLINGSPLATTFORMAR'))       # sAaB
    print(alt_case('HÖGSKOLEINGENJÖRSUTBILDNINGARNA'))       # sAaB
