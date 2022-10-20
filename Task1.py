# задача 1. Создайте программу для игры с конфетами человек против человека.
from random import randint

def candy_num(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите количество конфет от 1 до 28: "))
    return x


def game(name, k, count, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {count}. Осталось на столе {value} конфет.")

gamer1 = input("Введите имя первого игрока: ")
gamer2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
round = randint(0,2)
if round:
    print(f"Первый ходит {gamer1}")
else:
    print(f"Первый ходит {gamer2}")

count1 = 0 
count2 = 0

while value > 28:
    if round:
        k = candy_num(gamer1)
        count1 += k
        value -= k
        round = False
        game(gamer1, k, count1, value)
    else:
        k = candy_num(gamer2)
        count2 += k
        value -= k
        round = True
        game(gamer2, k, count2, value)

if round:
    print(f"Выиграл {gamer1}")
else:
    print(f"Выиграл {gamer2}")