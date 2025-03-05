# Ett läsår är uppdelat i fyra perioder: hösttermin, jullov, vårtermin och sommarlov.
# Datumen för de olika perioderna ges av
# hösttermin: 18 augusti - 22 december
# jullov: 23 december - 10 januari
# vårtermin: 11 januari - 10 juni
# sommarlov: 11 juni - 17 augusti
# Vi representerar ett datum med två heltal m och d. Såväl månader som dagar numreras med start
# på 1. Maj representeras av 5 och den sjuttonde maj av 5, 17.
# Komplettera följande funktion så att den returnerar den period som svarar mot ett givet datum.
# Perioden representeras av en av strängarna "hösttermin", "jullov", "vårtermin", "sommarlov".
def period(month, day):
    if (month == 8 and day >= 18) or (9 <= month <= 11) or (month == 12 and day <= 23):
        return 'hösttermin'
    elif (month == 12 and day >= 23) or (month == 1 and day <= 10):
        return 'jullov'
    elif (month == 1 and day >= 11) or (2 <= month <= 5) or (month == 6 and day <= 10):
        return 'vårtermin'
    elif (month == 6 and day >= 11) or (month == 7) or (month == 8 and day <= 17):
        return 'sommarlov'


if __name__ == '__main__':
    print(period(5, 25))   # 25 maj -> vårtermin
    print(period(7, 4))   # 4 juli -> sommarlov
    print(period(11, 14))   # 14 november -> hösttermin
    print(period(1, 1))   # 1 januari -> jullov
