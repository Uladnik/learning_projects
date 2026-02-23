def switch_opt(s): 
    while True:
        if s[0] == "2":
            return True
        elif s[0] == "1":
            return False
        else:
            s = input("Неверно, повторите попытку: ").lower()


def get_key(s):
    while True:
        if s.isdigit() and int(s) > 0:
            return int(s)
        else:
            s = input("Неверно, повторите попытку: ").lower()


upcase, lowcase, alphabet = ord("Я"), ord("я"), 32
print("Это (де)шифратор Цезаря. Выберите параметры и введите текст.", end="\n\n")
if switch_opt(input("Язык (русский - 1, английский - 2): ")):
    upcase, lowcase, alphabet = ord("Z"), ord("z"), 26
k = get_key(input("Сдвиг вправо (натуральное число): ")) % alphabet
if switch_opt(input("Шифрование (1) или дешифрование (2): ")):
    k = alphabet - k

for ch in input("Ваш текст: "):
    if ch.isupper():
        i = ord(ch) + k
        print(chr(i - alphabet) if i > upcase else chr(i), end="")
    elif ch.islower():
        i = ord(ch) + k
        print(chr(i - alphabet) if i > lowcase else chr(i), end="")
    else:
        print(ch, end="")
