#task 1
print("Завдання 1")
print()
num1 = int(input("Введіть 1 число: "))
num2 = int(input("Введіть 2 число: "))
sum = 0
for i in range(num1, num2 + 1):
    a = i * i
    sum += a
print(sum)


#task 2
print("Завдання 2")
print()
text = str(input("Введіть довільний текст: "))
sim = str(input("Введіт символ який ви хочет порахувати: "))
count = 0
for i in text:
    if i == sim:
        count += 1
print(count)

#task 3
print("Завдання 3")
print()
city1 = "Стамбул"
city2 = "Львів"
city3 = "Будапешт"
city4 = "Копенгаген"
city5 = "Одеса"
count = 0
EnterCity = str(input("Введіть місто до якого хочете поїхати: "))
for x in city1, city2, city3, city4, city5:
    if(EnterCity == x):
        print(f"Ви вже були в місті {EnterCity}")
        break
    if(EnterCity != x):
        count += 1
    if(count == 5):
        print(f"Ти ще не був в місті {EnterCity}")
