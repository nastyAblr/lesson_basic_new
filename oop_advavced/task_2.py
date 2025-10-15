"""
Создайте класс BankAccount с приватными атрибутами __balance и __interest_rate,
а также публичными методами deposit(amount) и withdraw(amount),
которые изменяют баланс счета.
Также создайте метод add_interest(), который увеличивает баланс
на процентную ставку. Затем создайте объект этого класса и проведите
несколько операций депозита, снятия и начисления процентов.
"""



class BankAccount:
    def __init__(self, balance=0, interest_rate=0):
        self.__balance = balance
        self.__interest_rate = interest_rate

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'Депозит: {amount}, Новый баланс: {self.__balance}')
        else:
            print('Сумма для внесения должна быть положительной')

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f'Сумма изьятия: {amount}, Новый баланс: {self.__balance}')
        else:
            print('Недостаточный баланс или неверная сумма')

    def add_interest(self):
        interest = self.__balance * self.__interest_rate / 100
        self.__balance += interest
        print(f'Добавленная ставка: {interest:.2f}, '
              f'Новый баланс: {self.__balance:.2f}')  # .2f - значат, что число в формате float, после запятой 2 знака


account1 = BankAccount(balance=1000, interest_rate=5)
account1.deposit(500)
account1.withdraw(200)
account1.add_interest()
