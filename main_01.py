def check(number):
    return number % 2 == 0 #2 проверка четности

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError ('На ноль делить нельзя!')
    # raise - это слово для генерации исключений
    return a / b

def divide_rest(a,b):
    if b == 0:
        raise ValueError ('На ноль делить нельзя!')
    return a % b
