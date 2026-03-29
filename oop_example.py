# Создаёт объект банковской карты класса ATM
# При вводе правильного пин-кода позволяет совершать операции


class ATM:
    def __init__(self, balance=1000, pin="1234"):
        self.balance = balance
        self.pin = pin

    def check_balance(self, guess):
        print(f"Баланс: {self.balance}" if guess == self.pin else "Неверный пин-код!")
        return self.balance if guess == self.pin else None

    def withdraw(self, guess, amount):
        if guess == self.pin:
            self.balance -= amount
            print(f"Снято {amount}. Остаток: {self.balance}")
            return self.balance
        else:
            print("Неверный пин-код!")
            return None

    def deposit(self, guess, amount):
        if guess == self.pin:
            self.balance += amount
            print(f"Внесено {amount}. Баланс: {self.balance}")
            return self.balance
        else:
            print("Неверный пин-код!")
            return None


my_atm = ATM()
my_atm.check_balance("0000")    # Неверный пин-код!
my_atm.check_balance("1234")    # Баланс: 1000
my_atm.withdraw("1234", 500)    # Снято 500. Остаток: 500
my_atm.deposit("1234", 200)     # Внесено 200. Баланс: 700
