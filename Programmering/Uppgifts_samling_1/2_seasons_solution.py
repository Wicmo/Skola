# I en kalender baserad på astronomiska händelser (vinter- och sommarsolstånd,
# vår- och höstdagjämning) definieras årstiderna enligt följande:
# vår: 20 mars - 20 juni
# sommar: 21 juni - 21 september
# höst: 22 september - 20 december
# vinter: 21 december - 19 mars
# Vi representerar ett datum med två heltal m och d. Såväl månader som dagar numreras med start
# på 1. Maj representeras av 5 och den sjuttonde maj av 5, 17.
# Komplettera följande funktion så att den returnerar den årstid som svarar mot ett givet datum.
# Årstiden representeras av en av strängarna "summer", "autumn", "winter", "spring".
def season(month, day):
    if (month == 3 and day >= 20) or (4 <= month <= 5) or (month == 6 and day <= 20):
        return 'spring'
    elif (month == 6 and day >= 21) or (7 <= month <= 8) or (month == 9 and day <= 21):
        return 'summer'
    elif (month == 9 and day >= 22) or (10 <= month <= 11) or (month == 12 and day <= 20):
        return 'autumn'
    elif (month == 12 and day >= 21) or (1 <= month <= 2) or (month == 3 and day <= 19):
        return 'winter'


if __name__ == '__main__':
    print(season(5, 25))   # 25 maj -> spring
    print(season(8, 13))   # 13 augusti -> summer
    print(season(12, 21))   # 21 december -> winter
    print(season(12, 20))   # 20 december -> autumn
