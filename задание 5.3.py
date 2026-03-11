word = ''
while True:
    word = input("Введите слово: ")
    letters = list(word)
    if "ф" in letters:
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")