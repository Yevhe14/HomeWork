#task 1
last_name = {'Іванов': 5,
             'Петров': 3,
             'Сідоров': 4,
             'Петренко': 5}
Good_grades = dict()
for i in last_name:
    if last_name[i] == 5 or last_name[i] == 4:
        Good_grades[i] = last_name[i]
print(Good_grades)

#task 2
city_weather = {'Київ': 10,
                'Харків': 12,
                'Львів': 8,
                'Одеса': 16}
count = 0
middle_digreez = 0
for i in city_weather.values():
    middle_digreez += i
    count += 1
middle_digreez = middle_digreez / count
print(middle_digreez)
