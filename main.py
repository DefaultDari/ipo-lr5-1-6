file1 = open("text.txt",'r', encoding="utf-8") # Открываем исходный файл text.txt для чтения
file2 = open("output.txt",'w', encoding="utf-8")  # Открываем файл output.txt для записи, а если его нет, он будет создан
line_number = 1 # Инициализируем переменную для нумерации строк, начиная с 1
for line in file1: # Проходим по каждой строке в файле text.txt            
    number = f"{line_number}: {line}" # Создаем строку с номером строки и текстом строки            
    file2.write(number) # Записываем эту строку в файл output.txt
    line_number += 1 # Увеличиваем номер строки на 1 для следующей итерации
#Закрытие файлов
file1.close()
file2.close()
