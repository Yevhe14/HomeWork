#калькулятор
def sum(a,b):        #Додавання
    return a + b

def averege(a,b):    #Віднімання
    return a - b

def mnozeny(a,b):    #Множення
    return a * b

def dilenny(a,b):    #Ділення
    return a / b

def doStepeny(a,b):  #Піднесеня до степеня
    return a ** b

def cheack_operator(operand_A, operand_B, operation):   #Перевірка яку дію виконати
    if operation not in ['+', '-', '*', '^']:
        print("Невідома операція")
    else:
        match operation:
            case '+':
                result = sum(operand_A, operand_B)
            case '-':
                result = averege(operand_A, operand_B)
            case '*':
                result = mnozeny(operand_A, operand_B)
            case '/':
                result = dilenny(operand_A, operand_B)
            case '^':
                result = doStepeny(operand_A, operand_B)
        print(f"{operand_A} {operation} {operand_B} = {result}")
a, operation, b = input().split()
cheack_operator(int(a), int(b), operation)


#Бронювання
last_name = "Сідоров"
last_name2 = "Петров"
count = 4

desk = {2: "столик на 2",
        4: "столик на 4",
        6: "столик на 6"}

def bron(last_name, count = 2):
    if count <= 4 and count > 2:
        print(f"{last_name} забронював {desk[4]}")
    if count <= 6 and count > 4:
        print(f"{last_name} забронював {desk[6]}")
    elif count <=2 and count < 3:
        print(f"{last_name} забронював {desk[2]}")
bron(last_name, count)
print()
bron(last_name2)
