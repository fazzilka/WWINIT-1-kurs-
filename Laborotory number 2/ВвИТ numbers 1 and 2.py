#Number 1
def greet(name, msg):
    print("Привет,", name + '. ' + msg)

greet(input('Напиши имя: '), "Добро пожаловать в МТУСИ")

def square(number):
    number = number**2
    return number

num = int(input('Напиши число: '))
print('Квадрат числа', num, '=', square(num))


def max_of_two(x, y):
    if x > y:
        return x
    return y

x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
print('Большее число:', max_of_two(x, y))


#Number 2
def describe_person(name, age=30):
    print("Имя ->", name + ".", age)

describe_person(input('Напиши имя: '))

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 2):
        if number % i == 0:
            return False
        return True

num = int(input())
print(is_prime(num))