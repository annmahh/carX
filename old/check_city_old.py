# for test

import geo

def check_city(line, file):
    with open(file, 'r', encoding='utf-8') as file:
        cities = file.readlines()
    cities = [city.strip() for city in cities]
    for city in cities:
        if city in line:
            return city
    if geo.get_geo(line):
        return "? " + geo.get_geo(line)
    elif "," in line:
        city = line.split(",")[0].strip()
        return "? " + city
    else:
        city = line.split(" ")[0].strip()
        return "? " + city
    return "Не найдено"

print(check_city("א. עפולה אייל  נייד: 053-9290444 קוד: *1142ניווט:https://waze.com/ul?ll=32.556806,35.392995&navigate=yes",
                 "../database/line5.txt"))