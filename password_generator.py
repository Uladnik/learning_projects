from random import choice 


def valid_ch(s):
    while True:
        if s[0] == "д":
            print("Включены")
            return True
        elif s[0] == "н":
            print("Исключены")
            return False
        else:
            s = input("Неверно, повторите попытку: ").lower()


def get_num(s, i):
    while True:
        if s.isdigit() and 0 < int(s) < i + 1:
            return int(s)
        else:
            s = input("Неверно, повторите попытку: ").lower()


def generate(ch, l, n):
    for _ in range(n):
        for _ in range(l):
            print(choice(ch), end="")
        print()


charset = []
print(
    f"""Это генератор паролей. Вы можете создать от 1 до 1000000 паролей, длиной от 1 до 255 символов каждый. Наборы символов вы также определяете, но обязательно выбрать хотя бы один. Ответьте на вопросы (Д/Н).""",
    end="\n\n",
)
while not charset:
    if valid_ch(input("Включать ли цифры 0123456789 ? ").lower()):
        charset += [str(i) for i in range(10)]
    if valid_ch(
        input("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ ? ").lower()
    ):
        charset += [chr(i) for i in range(65, 91)]
    if valid_ch(
        input("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz ? ").lower()
    ):
        charset += [chr(i) for i in range(97, 123)]
    if valid_ch(input("Включать ли символы !#$%&*+-=?@^_ ? ").lower()):
        charset += [i for i in "!#$%&*+-=?@^_"]
    if not charset:
        print("Нет символов для паролей. Начните заново.")
if valid_ch(input("Включать ли неоднозначные символы il1Lo0O ? ").lower()):
    for ch in "il1Lo0O":
        charset.remove(ch)
size = get_num(input("Укажите количество символов в пароле: ").lower(), 255)
iters = get_num(input("Укажите количество паролей: ").lower(), 10**6)
generate(charset, size, iters)
