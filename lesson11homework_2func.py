import math
def square():
    storona = int(input("Введіть 1 сторону квадрата: "))
    plaza = storona * storona
    return plaza

def sircle():
    storona = int(input("Введіть радіус кола: "))
    plaza1 = math.pi * storona * storona
    return plaza1

def prym():
    storona = int(input("Введіть 1 сторону прямокутника: "))
    storona2 = int(input("Введіть 2 сторону прямокутника: "))
    plaza2 = storona * storona2
    return plaza2