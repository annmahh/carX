# by for cycle

text = file.read()
lines = text.split('\n')
line_iterator = iter(lines)

for line in line_iterator:
    print('LINE: ', line)
    if 'מ"ק' in line:
        date_match = re.search(r'\d{1,2}\.\d{1,2}\.\d{4}', line)
        if date_match:
            date = date_match.group()
            # print(f"Дата: {date}")

            line2 = next(line_iterator, None)
            if line2 is not None:
                number_match = re.search(r'מ"ר:(\d+)', line2)
                if number_match:
                    number = number_match.group(1)
                    # print(f"Номер: {number}")

                    line3 = next(line_iterator, None)
                    if line3 is not None:
                        model = line3
                        # print(f"Модель: {model}")

                        line4 = next(line_iterator, None)
                        if line4 is not None:
                            locationA = check_city(line4, database4)
                            if locationA == 'בית חולים העמק':
                                locationA = 'עפולה'
                            elif locationA == 'סוכנויות ומרכזי שירות דור':
                                locationA = 'נצרת'
                            locationA_flag = False
                            if '?' not in locationA:
                                locationA_flag = True
                            # print(f"Локация 1: {locationA}")

                            line5 = next(line_iterator, None)
                            locationB_flag = False
                            if line5 is not None:
                                locationB = check_city(line5, database5)
                                while not locationB_flag:
                                    if '?' not in locationB:
                                        locationB_flag = True
                                        if locationA_flag == False:
                                            if geo.get_geo(line5):
                                                locationA = geo.get_geo(line5)
                                            else:
                                                locationA = '?'
                                    else:
                                        line5 = line5
                                        print('line5: ', line5)
                                        line5_next = next(line_iterator, None)
                                        print('line5_next: ', line5_next)
                                        if 'מ"ק' in line5_next:
                                            line = line5
                                            print('LINE (): ', line)
                                            break
                                        locationB = check_city(line5, database5)

                                if locationB == 'בית חולים העמק':
                                    locationB = 'עפולה'
                                elif locationB == 'סוכנויות ומרכזי שירות דור':
                                    locationB = 'נצרת'
                                if '?' in locationB:
                                    locationB = '?'

                                if locationA_flag == False:
                                    if geo.get_geo(line5):
                                        locationA = geo.get_geo(line5)
                                    else:
                                        locationA = '?'
                                # print(f"Локация 2: {locationB}", '\n', line5, '\n')
                                # print(date, number, model, locationA, locationB, row)
                                update_excel(date, number, model, locationA, locationB, row)
                                row = row + 1