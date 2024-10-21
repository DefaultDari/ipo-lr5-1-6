file1 = open('D:\\profiles\\LutsenD_81\\Desktop\\text.txt', 'r') # Открываем исходный файл text.txt для чтения
file2 = open('D:\\profiles\\LutsenD_81\\Desktop\\output.txt', 'w')  # Открываем файл output.txt для записи, а если его нет, он будет создан
line_number = 1 # Инициализируем переменную для нумерации строк, начиная с 1
for line in file1: # Проходим по каждой строке в файле text.txt            
    number = f"{line_number}: {line}" # Создаем строку с номером строки и текстом строки            
    file2.write(number) # Записываем эту строку в файл output.txt
    line_number += 1 # Увеличиваем номер строки на 1 для следующей итерации
