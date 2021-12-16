def func(x, y):
      return x + y

func_alias = func
result = func_alias(2, 3)
print(result)

#-----------------------------------
def sum_func(x, y):
    return x + y

def subtraction_func(x, y):
    return x - y

def tricky_func(x, y, func):
    return func(x, y)

sum_result = tricky_func(2, 3, sum_func)
min_result = tricky_func(2, 3, subtraction_func)

print(sum_result)  # 5
print(min_result)  #-1


#-----------------------------------
def sum_func(x, y):
    return x + y

def subtraction_func(x, y):
    return x - y

def get_operator(operator):
    if operator == '+':
        return sum_func
    elif operator == '-':
        return subtraction_func
    else:
        print('Unknown operator')

sum_action_function = get_operator("+")
print(sum_action_function(2, 3))    # 5

sub_action_function = get_operator("-")
print(sub_action_function(2, 3))    # -1


#-----------------------------------
user_A = {
    'phone': '+380001234567',
    'notification': 'SMS'
}

user_B = {
    'email': 'petrov@ggg.com', 
    'notification': 'email'
}

user_C = {
    'app_id': 'dasdskcs7y774ysbfh', 
    'notification': 'push'
}

def send_sms(user_info, message):
    print('Send SMS to {} with text {}'.format(user_info['phone'], message))
    

def send_push(user_info, message):
    print('Send message {} to queue with app id {}'.format(message, user_info['app_id']))
    

def send_email(user_info, message):
    print('Send email to {} with text {}'.format(user_info['email'], message))
    
    
def check_notification_type(type):
    if type == 'SMS':
        return send_sms
    elif type == 'push':
        return send_push
    else:
        return send_email


for user in [user_A, user_B, user_C]:
    send_method = check_notification_type(user['notification'])
    send_method(user, '18.09.2001 надходження: зарплата - 30 000 грн. Баланс: 100 444 грн.')


#-----------------------------------
#Каррирование
def sum_func(x, y):
    return x + y


def sub_func(x, y):
    return x - y


OPERATIONS = {
    '-': sub_func,
    '+': sum_func
}


def get_handler(operator):
    return OPERATIONS[operator]


handler = get_handler('-')
handler(2, 3)           # -1

get_handler('+')(2, 3)  # 5


#-----------------------------------
#Лямбда-функции 
sum_lambda = lambda x, y: x + y
sum_lambda(10, 12)


#-----------------------------------

#map
numbers = [1, 2, 3, 4, 5]

for i in map(lambda x: x ** 2, numbers):
    print(i)



#-----------------------------------
#filter
for i in filter(lambda x: x % 2, range(1, 10)):
    print(i)



#-----------------------------------
#Вивести країни з населенням більше 300 мільйонів.

countries = [
    ['China', 1394015977],
    ['United States', 329877505],
    ['India', 1326093247],
    ['Indonesia', 267026366],
    ['Bangladesh', 162650853],
    ['Pakistan', 233500636],
    ['Nigeria', 214028302],
    ['Brazil', 21171597],
    ['Russia', 141722205],
    ['Mexico', 128649565]
]

populated = filter(lambda c: c[1] > 300000000, countries)

print(list(populated))


#-----------------------------------
employers = [
    {'name': 'Ivanova', 
     'gender': 'female',
    }, 
    {'name': 'Ivanov', 
     'gender': 'male',
    }, 
    {'name': 'Petrova', 
     'gender': 'female',
    }, 
    {'name': 'Sidorova', 
     'gender': 'female',
    }, 
]

def check_female(user):
    return user['gender'] == 'female'

womans = filter(check_female, employers)
for worker in womans:
    print(worker['name'])

for worker in filter(check_female, employers):
    print(worker['name'])