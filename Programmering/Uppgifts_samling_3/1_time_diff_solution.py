# Tiden för ett 5000-meterslopp på skridskor mäts i minuter, sekunder och
# hundradels sekunder. Vi kan representera tiden som en tupel bestående av
# tre heltal: minuter, sekunder och hundradels sekunder.

# Nils van der Poel: 6:08.84 (OS-guld 2022 Beijing)
# nils_22 = (6, 8, 84)
# Tomas Gustafsson: 7:12.28 (OS-guld 1984 Sarajevo)
# tomas_84 = (7, 12, 28)
# Tomas Gustafsson: 6:44.63 (OS-guld 1988 Calgary)
# tomas_88 = (6, 44, 63)

# Skriv en funktion som tar två tider i form av tupler enligt ovan och
# returnerar tidsskillnaden mellan dem på samma format. Vi kan anta att den
# första tiden alltid är kortare än den andra.

# Tips: Gör om tiderna till hundradels sekunder, subtrahera de två tiderna
# och gör om resultatet till minuter, sekunder och hundradelar igen.

def time_diff(t1, t2):
    t1_hundreds = t1[0] * 60 * 100 + t1[1] * 100 + t1[2]
    t2_hundreds = t2[0] * 60 * 100 + t2[1] * 100 + t2[2]
    t_diff = t2_hundreds - t1_hundreds
    minutes = t_diff // (60 * 100)
    seconds = t_diff // 100 - 60 * minutes
    hundreds = t_diff % 100
    return minutes, seconds, hundreds


if __name__ == '__main__':
    nils_22 = (6, 8, 84)
    tomas_84 = (7, 12, 28)
    tomas_88 = (6, 44, 63)
    print(time_diff(nils_22, tomas_88))       # (0, 35, 79)
    print(time_diff(tomas_88, tomas_84))      # (0, 27, 65)

    ta_1 = (7, 13, 22)
    ta_2 = (7, 13, 94)
    tb_1 = (9, 42, 17)
    tb_2 = (9, 42, 64)
    tc_1 = (11, 25, 14)
    tc_2 = (11, 25, 83)
    print(time_diff(ta_1, ta_2))     # (0, 0, 72)
    print(time_diff(tb_1, tb_2))     # (0, 0, 47)
    print(time_diff(tc_1, tc_2))     # (0, 0, 69)

    ta_1 = (7, 13, 20)
    ta_2 = (7, 16, 45)
    tb_1 = (9, 36, 77)
    tb_2 = (9, 41, 64)
    tc_1 = (11, 18, 78)
    tc_2 = (11, 25, 45)
    print(time_diff(ta_1, ta_2))     # (0, 3, 25)
    print(time_diff(tb_1, tb_2))     # (0, 4, 87)
    print(time_diff(tc_1, tc_2))     # (0, 6, 67)

    ta_1 = (7, 13, 22)
    ta_2 = (8, 56, 94)
    tb_1 = (3, 42, 52)
    tb_2 = (4, 12, 39)
    tc_1 = (11, 53, 67)
    tc_2 = (14, 14, 62)
    print(time_diff(ta_1, ta_2))     # (1, 43, 72)
    print(time_diff(tb_1, tb_2))     # (0, 29, 87)
    print(time_diff(tc_1, tc_2))     # (2, 20, 95)
