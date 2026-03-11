mistakes = 0
right = 0
import random
while mistakes<3:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = input(f"{a} + {b}  = ")
    if c == a+b:
        right = right + 1
        print("Правильно!")
    else:
        mistakes = mistakes + 1
        print("Ответ неверный")
print("Игра окончена. Правильных ответов:", right)