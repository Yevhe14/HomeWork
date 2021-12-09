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