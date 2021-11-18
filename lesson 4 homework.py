'''
products = []
products_sold = list()

print('Постачання продуктів')

while True:
    product = input('Введіть назву продукту або 0 для виходу: ')

    if product == '0' :
        break
    else:
        products.append(product)
for i in products:
    print(i, end=' ')
'''

west = ['Євразія', 'Африка', 'Австралія']
east = ['Північна Америка', 'Південна Америка']
all = []
for i in west:
    west.append(east)
for x in west:
    print(x, end= '')
'''
#task 2
goods = [

    ['телефон', 'samsung', 7800],

    ['ноутбук', 'dell', 28000],

    ['ноутбук', 'hp', 35000],

    ['телефон', 'iphone', 27800],

]

print("Категорії товарів \n 1) телефон\n 2) ноутбук")
categori = str(input("Введіть категорію: "))
price = int(input("Введіть максимальну ціну: "))
count = 0
for i in goods:
    if goods[count][0] == categori:
        if goods[count][2] <= price:
            print(f"{categori} {goods[count][1]} ви можете купити за {goods[count][2]}")
        else:
            print(f'По ціні {price} ви нічого не зможете купити!')
    else:
        print(f'Категорії "{categori}" не має!')
        break
    count += 1
'''