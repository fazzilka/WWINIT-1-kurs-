# 1, 3 number
with open('example.txt', 'w', encoding='utf-8') as file:
    file.write("Это первая строка текста.\n")
    file.write("Это вторая строка текста.\n")
    file.write("Это третья строка текста.\n")
    file.write("Это четвертая строка текста.\n")

def read_file(filename, read_mode='all'):
    """
    Функция для чтения содержимого файла.

    :parametr filename: Имя файла для чтения.
    :parametr read_mode: Режим чтения ('all' для чтения всего файла, 'line' для построчного чтения).
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            if read_mode == 'all':
                content = file.read()
                print(content)
            elif read_mode == 'line':
                for line in file:
                    print(line.strip())
            else:
                print("Неверный режим чтения. Используйте 'all' или 'line'.")
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Пример использования функции
print("\nЧтение всего файла:\n")
read_file('exemple.txt', 'all')  # Чтение всего файла
print("\nПострочное чтение:\n")
read_file('exemple.txt', 'line')  # Построчное чтение

# 2 number
def write_to_file(filename, text, append=False):

    '''Записывает текст в файл. Если append=True, добавляет текст в конец файла,
    иначе перезаписывает файл.

    :parametr filename: Имя файла для записи.
    :parametr text: Текст для записи в файл.
    :parametr append: Флаг, указывающий, нужно ли добавлять текст в конец файла.'''

    mode = 'a' if append else 'w'  # Режим 'a' для добавления, 'w' для перезаписи
    with open(filename, mode, encoding='utf-8') as file:
        file.write(text + '\n')  # Записываем текст и добавляем перевод строки

def main():
    filename = 'user_input.txt'
    user_text = input("Введите текст, который вы хотите сохранить в файле: ")

    # Запрашиваем, хотим ли мы добавить текст в существующий файл
    append_mode = input("Хотите добавить текст в существующий файл? (да/нет): ").strip().lower()
    if append_mode == 'да':
        write_to_file(filename, user_text, append=True)
    else:
        write_to_file(filename, user_text, append=False)

    print(f"Текст успешно записан в файл {filename}.")


if __name__ == "__main__":
    main()