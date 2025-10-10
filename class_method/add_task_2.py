"""
Создайте класс BankAccount с приватным атрибутом _balance (баланс).
В init установите self._balance = 0.

Добавьте метод-геттер def get_balance(self):, который возвращает self._balance.
Добавьте метод-сеттер def set_balance(self, amount):,
который добавляет amount к self._balance,
но только если amount > 0
(иначе выведите "Сумма должна быть положительной!" и не добавляйте).

Создайте account = BankAccount(), вызовите account.set_balance(100)
(баланс станет 100), затем account.set_balance(-50) (должна быть ошибка).
Выведите print(account.get_balance()).

"""
class BancAccount:
    def __init__(self):
        self._balance = 0

    def get_balance(self):
        return self._balance
    def set_balance(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print('Сумма должна быть положительной')

account = BancAccount()
account.set_balance(100)
account.set_balance(-50)
print(account.get_balance())
