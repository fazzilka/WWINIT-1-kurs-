import math
import datetime

#вычисляем квадратный корень из числа
num = int(input("Введите число: "))
square_root = math.sqrt(num)
print(f"Квадратный корень из числа {num} = {square_root}")

# Получаем текущее время
current_time = datetime.datetime.now()
print(f"Текущее дата и время {current_time}")