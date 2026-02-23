from random import choice 

words = "аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея индюк кит кобра коза козел койот корова кошка кролик крыса курица лама ласка лебедь лев лиса лосось лось лягушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь олень орел осел панда паук питон попугай пума семга скунс собака сова тигр тритон тюлень утка форель хорек черепаха ястреб ящерица".split()


def get_word(worda):
    return choice(words).upper()


# функция получения текущего состояния
def display_hangman(tries):
    stages = [
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
    ]
    return stages[tries]


def play(word):
    word_completion = ["_" for char in word]
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Давайте играть в угадайку слов!")
    print("Назовите букву или слово целиком.")
    while True:
        print(display_hangman(tries))
        if not tries:
            print("Вы проиграли. Слово:", word)
            return False
        print(f"У вас в запасе {tries} промахов")
        print(*word_completion)
        s = input().upper()
        while (not s.isalpha()) or s in guessed_letters or s in guessed_words:
            print("Некорректный ввод, повторите попытку")
            s = input().upper()
        if s == word:
            print("Поздравляем, вы выиграли!")
            return True
        elif len(s) > 1:
            guessed_words.append(s)
            tries -= 1
        elif s not in word:
            guessed_letters.append(s)
            tries -= 1
        else:
            for i in range(len(word)):
                if word[i] == s:
                    word_completion[i] = s
            guessed_letters.append(s)
            if "_" not in word_completion:
                print(*word_completion)
                print("Поздравляем, вы выиграли!")
                return True


def play_again(s):
    while True:
        if s in ("Д", "ДА"):
            return True
        elif s in ("Н", "НЕ", "НЕТ"):
            return False
        else:
            print("Некорректный ввод, повторите попытку")
            s = input().upper()


wins, losses = 0, 0
while True:
    if play(get_word(words)):
        wins += 1
    else:
        losses += 1
    print(f"Счёт: {wins}:{losses}. Хотите сыграть ещё? (Д/Н): ", end="")
    if not play_again(input().upper()):
        break
