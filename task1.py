# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with open('file.txt', 'r', encoding='utf-8') as file:
    file_data_list = file.read()
    print(f'Данные с файла {file_data_list}')
file.close()

my_list = file_data_list.split(" ")
result = []
for word in my_list:
    if "абв" not in word:
        result.append(word)

print(" ".join(result))
