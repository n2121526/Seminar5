# задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв". Функции FIND и COUNT юзать нельзя.
text = input('Введите текст:').split()
delete_text = 'абв'
new_text = list(filter(lambda item: delete_text not in item, text))
print(new_text)


