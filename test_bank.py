import unittest
from bank import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Alice", 100)

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 100)

    def test_deposit_positive_amount(self):
        result = self.account.deposit(50)
        self.assertTrue(result)
        self.assertEqual(self.account.balance, 150)

    def test_deposit_negative_amount(self):
        result = self.account.deposit(-20)
        self.assertFalse(result)
        self.assertEqual(self.account.balance, 100)

    def test_withdraw_valid_amount(self):
        result = self.account.withdraw(70)
        self.assertTrue(result)
        self.assertEqual(self.account.balance, 30)

    def test_withdraw_overdraft(self):
        result = self.account.withdraw(200)
        self.assertFalse(result)
        self.assertEqual(self.account.balance, 100)

if __name__ == '__main__':
    unittest.main()
    
Method	What it checks for
assertEqual(a, b)	a == b
assertNotEqual(a, b)	a != b
assertTrue(x)	bool(x) is True
assertFalse(x)	bool(x) is False
assertIs(a, b)	a is b
assertIsNone(x)	x is None
assertIn(a, b)	a in b
assertRaises(Exception)	Exception is raised