#task 1
name = str(input("Введіть прізвище студента: "))
point = int(input("Введіть кількість балів яку набрав студент: "))
rating = ""

if point <= 60:
    rating = "незадовільно"
elif point <= 74 and point > 60:
    rating = "задовільно"
elif point <= 94 and point >= 75:
    rating = "добре"
elif point <= 100 and point >= 95:
    rating = "відмінно"

print(f'Студент {name} набрав {point} балів і отриав оцінку "{rating}"!')

#task 2
FirstTwoL = str(input("Введіть перші дві літери номеру транспортного засобу: "))
oblast = ""

match FirstTwoL:
    case 'АА', 'АК':
        oblast = "Місто Київ"
    case 'АВ':
        oblast = "Вінницька область"
    case 'АЕ':
        oblast = "Дніпропетровська область"
    case 'АН':
        oblast = "Донецька область"
    case _:
        oblast = "Інша область "
print(oblast)