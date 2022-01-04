import math
from lesson11homework_2func import square
from lesson11homework_2func import sircle
from lesson11homework_2func import prym

x = 0
x1 = 0
figures = input("Введіть назву фігури \n Квадрат, коло, прямокутник: ")

if figures == "квадрат":
    x = square()
elif figures == "коло":
    x = sircle()
elif figures == "прямокутник":
    x = prym()
else:
    print(0)

print()

print(f"Площа {figures} {x}см^2")

print()
figures1 = input("Введіть назву фігури \n Квадрат, коло, прямокутник: ")

if figures1 == "квадрат":
    x1 = square()
elif figures1 == "коло":
    x1 = sircle()
elif figures1 == "прямокутник":
    x1 = prym()
else:
    print(0)

print()

print(f"Площа {figures1} {x1}см^2")

print()

print(f"Зрівняти площі фігур {figures} {x}см^2 і {figures1} {x1}см^2")
if x > x1:
    print(f"площа {figures} більше ніж площа {figures1}")
elif x < x1:
    print(f"Площа {figures1} більше ніж площа {figures}")
elif x == x1:
    print(f"Площа {figures} = площі {figures1}")
else:
    print("Error")