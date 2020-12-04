import pytest
from banking import Account


class TestAccount:

    def setup_class(self):
        self.account1 = Account(1)
        self.account2 = Account(2)

    def teardown_class(self):
        pass

    def test_check_balance(self):
        assert self.account1.check_balance() == 0
        assert self.account2.check_balance() == 0

    def test_deposit(self):
        self.account1.deposit(200)
        assert self.account1.check_balance() == 200

    def test_withdraw(self):
        self.account1.withdraw(150)
        assert self.account1.check_balance() == 50

    def test_withdraw_limit(self):
        assert self.account1.withdraw(250) == False

    def test_transfer(self):
        self.account1.deposit(150)
        self.account1.transfer(self.account2, 50)
        assert self.account2.check_balance() == 50
