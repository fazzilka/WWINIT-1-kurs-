from my_package import math_operation, string_opperation

a = int(input("Введите число а: "))
b = int(input("Введите число b: "))
product = math_operation.umnog(a, b)
print(f"Произведение a на b равно: {product}")

rez_string = string_opperation.string("Hello", "MTUCI")
print(f"Результат конкатенации равен: {rez_string}")