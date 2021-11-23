#task 1 рішення 1
last_name = input("Введіть текст: ")
a = 0
for i in last_name:
    max = a
    a = last_name.count(i)
    if max < a:
        max = a
        leter = i
    else:
        a = 0
print(f"Буква \"{leter}\" зустрічаэться {max} разів")



#task 1 рішення 2
text1 = input("Введіть ваше текст: ")
a1 = 0
flag = False
for i1 in text1:
    max1 = a1
    a1 = text1.count(i1)
    if max1 < a1:
        max1 = a1
        leter1 = i1
        max2 = a1
    if max1 == max2 and max1 > 1:
        flag = True
        leter2 = i1
    else:
        a1 = 0
if flag == False:
    print(f"Буква \"{leter1}\" зустрічаэться {max1} разів")
elif flag == True:
    print(f"Буква \"{leter1}\" і буква \"{leter2}\" зустрічаються однакову кількість разів {max1} рази")


#task 2
num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
text = input("Введите текст: ")
counter = 0
txt = ""
for x in text:
    if x == num[counter]:
        txt = text.replace(num[counter], "")
    counter =+ 1
print(txt)

#task 3
numPhones = ["+380670125456", "+380680213784", "+380970123329", "+380440784920", "+380660145326", "+38660345451", "+3809702154", "380970121314"]
errorPhone = [""]
for numPhone in numPhones:
    if len(numPhone) == 13 or numPhone[3:6] == "067" or numPhone[3:6] == "069" or numPhone[3:6] == "097" or numPhone[3:6] == "044" and numPhone[:3] == "+38":
       pass
    else:   
       errorPhone.append(numPhone)
for z in errorPhone:
    print(z, end= " ")