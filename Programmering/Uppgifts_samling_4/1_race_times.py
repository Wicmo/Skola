# Löpare pratar ofta om tempo (i minuter och sekunder per km) istället för hastighet
# (i km/h). Vi vill nu räkna ut tiden det tar att springa en given sträcka i km givet
# ett visst tempo. Funktionen ska returnera en tupel bestående av tre heltal som
# motsvarar timmar, minuter och sekunder. Avrunda till närmsta heltal vid behov.
def race_time(distance, minutes, seconds):
    seconds_per_km = minutes * 60 + seconds
    total_seconds = round(distance * seconds_per_km)
    h = total_seconds // 3600
    m = (total_seconds % 3600) // 60
    s = total_seconds % 60
    return h, m, s


if __name__ == '__main__':
    # 10 km i tempot 6 min 0 s per km
    print(race_time(10, 6, 0))          # (1, 0, 0)
    # marathon 42.195 km i tempot 5 min 35 s per km
    print(race_time(42.195, 5, 35))     # (3, 55, 35)

    # Test integer race lengths, less than 1h:
    print(race_time(5, 6, 0))           # (0, 30, 0)
    print(race_time(6, 5, 57))          # (0, 35, 42)
    print(race_time(7, 5, 21))          # (0, 37, 27)
    print(race_time(15, 3, 42))         # (0, 55, 30)
    print(race_time(20, 2, 55))         # (0, 58, 20)

    # Test integer race lengths, more than 1h:
    print(race_time(12, 6, 30))         # (1, 18, 0)
    print(race_time(15, 5, 57))         # (1, 29, 15)
    print(race_time(27, 5, 18))         # (2, 23, 6)
    print(race_time(50, 4, 26))         # (3, 41, 40)
    print(race_time(64, 6, 13))         # (6, 37, 52)

    # Test use cases:
    print(race_time(21.0975, 5, 41))    # (1, 59, 54)
    print(race_time(42.195, 2, 50))     # (1, 59, 33)
    print(race_time(42.195, 5, 35))     # (3, 5, 35)
    print(race_time(16.0934, 5, 15))    # (1, 24, 29)
    print(race_time(8.04672, 6, 43))    # (0, 54, 3)
