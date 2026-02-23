from random import randint 

x = randint(1, 100)
n = int(input("Угадайте число от 1 до 100: "))
while True:
    if n == x:
        print("Вы угадали, поздравляем!")
        break
    print(
        "Слишком много, попробуйте еще раз"
        if n > x
        else "Слишком мало, попробуйте еще раз"
    )
    n = int(input())