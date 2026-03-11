words = ''
while True:
    words = words + ' ' + input("Введите слово: ")
    if "stop" in words:
        break
print(words)