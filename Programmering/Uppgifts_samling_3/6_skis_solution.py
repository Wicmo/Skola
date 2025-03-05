# Vuxna längdskidåkare bör ha skidor som är 20-30 cm längre än kroppslängden.
# Skidor finns i alla jämna 5 cm-längder (190 cm, 195 cm, 200 cm, 205 cm, ...).
# För att hitta rätt längd på skidor för en åkare adderar vi 25 cm till
# kroppslängden och avrundar till närmaste 5 cm.

# Ex:
# kroppslängd 167 cm + 25 cm = 192 cm -> 190 cm skidlängd
# kroppslängd 154 cm + 25 cm = 178 cm -> 180 cm skidlängd

# I skiduthyrningen förbereder man sig inför en hektisk dag genom att i förväg
# plocka fram rätt antal skidor av de olika längderna. Varje kund har i sin
# bokning angett sitt namn och sin längd. Alla bokningar har sedan samlats i en
# dict där varje nyckel är ett namn och värdet är personens längd.
# Skriv en funktion som tar denna dict och returnerar en ny dict där varje nyckel
# är en skidlängd och värdet är en lista med namn på de personer som ska ha skidor
# av den längden. Endast skidlängder som bokats av minst en person ska finnas
# med som nycklar i dict:en.

# Notera att det inte finns någon övre gräns för hur långa personerna kan vara.

# Tips: Vi kan avrunda till jämna 5 cm genom att först dividera med 5, sedan
# avrunda till närmsta heltal och slutligen multiplicera resultatet med 5.

def skis(booking):
    res = {}
    for name, length in booking.items():
        ski = round((length + 25) / 5) * 5
        if ski in res:
            res[ski].append(name)
        else:
            res[ski] = [name]
    return res


if __name__ == '__main__':
    adams = {'Al': 167, 'Bob': 154, 'Cat': 169, 'Don': 164}
    print(skis(adams))    # {190: ['Al', 'Don'], 180: ['Bob'], 195: ['Cat']}

    customers = {'Astrid': 167, 'Birgitta': 154, 'Carola': 169, 'Dagny': 164}
    print(skis(customers))   # {190: ['Astrid', 'Dagny'], 180: ['Birgitta'], 195: ['Carola']}

    for height in range(145, 201):
        ski_length = round((height + 25) / 5) * 5
        # print(height, ski_length)

    names = ['Alfred', 'Bertil', 'Claes', 'Dan', 'Evalott', 'Freja', 'Gunborg', 'Hilda']
    import random
    lengths = random.sample(range(145, 201), 8)
    random.shuffle(names)
    people = dict(zip(names, lengths))
    print(people)

    order2 = {'Freja': 179, 'Alfred': 178, 'Claes': 200, 'Dan': 186,
              'Bertil': 167, 'Hilda': 155, 'Evalott': 157, 'Gunborg': 168}
    skis2 = {205: ['Freja', 'Alfred'], 225: ['Claes'], 210: ['Dan'],
             190: ['Bertil'], 180: ['Hilda', 'Evalott'], 195: ['Gunborg']}
    res2 = skis(order2)
    customer_names = set()
    for client_list in res2.values():
        customer_names.update(client_list)
    assert set(order2.keys()) == customer_names
    print(set(order2.keys()))
    print(customer_names)

    random.seed(835)
    ppl = list('abcdefghijklmnopqrstuvwxyz')
    random.shuffle(ppl)
    lens = random.sample(range(150, 350), len(ppl))
    order3 = dict(zip(ppl, lens))
    print(order3)
    res3 = skis(order3)
    customer_names3 = set()
    for client_list in res3.values():
        customer_names3.update(client_list)
    assert set(order3.keys()) == customer_names3
    print(res3)
