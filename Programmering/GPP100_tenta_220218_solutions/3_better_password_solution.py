# Många användare väljer lösenord som är för enkla och därmed lätta att gissa.
# Ett enkelt lösenord bestående av ett ord skrivet med små bokstäver kan göras
# bättre genom att byta ut vissa bokstäver mot siffror enligt reglerna nedan.

# bokstav -> siffra
#    a         4
#    e         3
#    i         1
#    o         0
#    s         5
#    t         7

# Skriv en funktion som tar ett enkelt lösenord i form av en sträng och
# returnerar ett förslag på ett bättre lösenord enligt metoden ovan. Det
# returnerade lösenordet ska även det vara en sträng. Du kan anta att det
# enkla lösenordet består av enbart små bokstäver.

def better_password(password):
    suggestion = ''
    for letter in password:
        if letter == 'a':
            suggestion += '4'
        elif letter == 'e':
            suggestion += '3'
        elif letter == 'i':
            suggestion += '1'
        elif letter == 'o':
            suggestion += '0'
        elif letter == 's':
            suggestion += '5'
        elif letter == 't':
            suggestion += '7'
        else:
            suggestion += letter
    return suggestion


if __name__ == '__main__':
    print(better_password('password'))    # p455w0rd
    print(better_password('qwerty'))      # qw3r7y

    print(better_password('bcdfghjklmnpqruvwxyz'))                # bcdfghjklmnpqruvwxyz
    print(better_password('åäö'))                                 # åäö
    print(better_password('1234567890'))                          # 1234567890
    print(better_password('aeiost'))                              # 431057
    print(better_password('eastie'))                              # 345713
    print(better_password('oieast'))                              # 013457
    print(better_password('realisationsvinstbeskattning'))        # r34l154710n5v1n57b35k477n1ng
    print(better_password('specialistsjuksköterskeutbildning'))   # 5p3c14l1575juk5kö73r5k3u7b1ldn1ng
    print(better_password('underhållsuppföljningssystem'))        # und3rhåll5uppföljn1ng55y573m
