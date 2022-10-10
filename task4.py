# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


def coding_text(text):
    result = ''
    count = 0
    old_element = ''
    for i in text:
        if old_element == '':
            old_element = i
            count += 1
            continue
        if i == old_element:
            count += 1
        else:
            result = result + str(count) + old_element
            old_element = i
            count = 1
    result = result + str(count) + old_element
    return result


with open('text_1.txt', 'r') as file:
    file_data_list1 = file.read()
    print(f'Данные с файла {file_data_list1}')
file.close()
print(coding_text(file_data_list1))
