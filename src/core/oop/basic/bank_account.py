import datetime as dt

class BankAccount:
    def __init__(self, account_holder):
        """初始化 BankAccount 实例
        Args:
            account_holder (str): 账户持有人
        """
        self._balance = 0
        self._name = account_holder
        with open(self._name + '_ledger.txt', 'w', encoding='utf-8') as ledger_file:
            ledger_file.write(f'{dt.datetime.now()} 开户余额：0\n')
            ledger_file.write('-' * 20 + '\n')

    def deposit(self, amount):
        """存款
        Args:
            amount (int): 存款金额
        """
        if amount < 0: return
        self._balance += amount
        with open(self._name + '_ledger.txt', 'a', encoding='utf-8') as ledger_file:
            ledger_file.write(f'{dt.datetime.now()} 存款：{amount}\n')
            ledger_file.write(f' 账户余额：{self._balance}\n')
            ledger_file.write('-' * 20 + '\n')

    def withdraw(self, amount):
        """取款
        Args:
            amount (int): 取款金额
        """
        if amount < 0 or amount > self._balance: return
        self._balance -= amount
        with open(self._name + '_ledger.txt', 'a', encoding='utf-8') as ledger_file:
            ledger_file.write(f'{dt.datetime.now()} 取款：{amount}\n')
            ledger_file.write(f'账户余额：{self._balance}\n')
            ledger_file.write('-' * 20 + '\n')


if __name__ == '__main__':
    pkmer = BankAccount('pkmer')
