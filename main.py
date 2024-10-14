with open('C:\\Users\\agjjj\Desktop\\text.txt', 'r') as text_txt: # Открываем исходный файл text.txt для чтения
    with open('C:\\Users\\agjjj\Desktop\\output.txt', 'w') as output_txt: # Открываем файл output.txt для записи, а если его нет, он будет создан
        line_number = 1 # Инициализируем переменную для нумерации строк, начиная с 1
        for line in text_txt: # Проходим по каждой строке в файле text.txt            
            number = f"{line_number}: {line}" # Создаем строку с номером строки и текстом строки            
            output_txt.write(number) # Записываем эту строку в файл output.txt
            line_number += 1 # Увеличиваем номер строки на 1 для следующей итерации