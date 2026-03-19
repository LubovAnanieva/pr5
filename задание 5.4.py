import random
mistakes = 0
right = 0
while mistakes<3:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = int(input(f"{a} + {b} = "))
    if c == a + b:
        right += 1
        print("Правильно!")
    else:
        mistakes += 1
        print("Ответ неверный")
print(f"Игра окончена. Правильных ответов: {right}")
