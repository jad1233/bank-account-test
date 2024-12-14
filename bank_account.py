class BankAccount:
    def __init__(self, accountNumber: str, balance: float = 0.0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.accountNumber = accountNumber
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def getBalance(self) -> float:
        return self.balance


import unittest

class TestBankAccount(unittest.TestCase):
    
    def test_create_account_with_valid_balance(self):
        account = BankAccount("123456", 100.0)
        self.assertEqual(account.getBalance(), 100.0)
    
    def test_create_account_with_invalid_balance(self):
        with self.assertRaises(ValueError):
            BankAccount("123456", -100.0)
    
    def test_deposit_valid_amount(self):
        account = BankAccount("123456", 100.0)
        account.deposit(50.0)
        self.assertEqual(account.getBalance(), 150.0)
    
    def test_deposit_invalid_amount(self):
        account = BankAccount("123456", 100.0)
        with self.assertRaises(ValueError):
            account.deposit(0)
        with self.assertRaises(ValueError):
            account.deposit(-50.0)
    
    def test_withdraw_valid_amount(self):
        account = BankAccount("123456", 100.0)
        account.withdraw(50.0)
        self.assertEqual(account.getBalance(), 50.0)
    
    def test_withdraw_insufficient_funds(self):
        account = BankAccount("123456", 100.0)
        with self.assertRaises(ValueError) as context:
            account.withdraw(150.0)
        self.assertEqual(str(context.exception), "Insufficient funds")
    
    def test_withdraw_invalid_amount(self):
        account = BankAccount("123456", 100.0)
        with self.assertRaises(ValueError):
            account.withdraw(0)
        with self.assertRaises(ValueError):
            account.withdraw(-50.0)
    
    def test_balance_after_multiple_operations(self):
        account = BankAccount("123456", 100.0)
        account.deposit(50.0)
        account.withdraw(30.0)
        self.assertEqual(account.getBalance(), 120.0)

if __name__ == '__main__':
    unittest.main()
