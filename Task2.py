# задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def code_RLE(text):
     new_string =''
     count = 1
     i = 0
     while i < len(text) - 1:
         if text[i] == text[i+1]: count+=1
         else: 
             new_string += str(count) + text[i]
             count = 1
         i+=1
     new_string += str(count) + text[len(text)-1]   
     return new_string      

def decode_RLE(text):
    words = ''
    rle_text = ''
    for alph in text:
         if alph.isdigit():
             words+=alph
         else:
             rle_text+=alph*int(words)  
             words = ''
    print(rle_text)
    return rle_text

a = input("Введите текст для кодировки: ")
print(f"Текст после кодировки: {code_RLE(a)}")
print(f"Текст после дешифровки: {decode_RLE(code_RLE(a))}")