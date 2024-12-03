import unittest
from sandbox_wallet.wallet import Wallet
from sandbox_wallet.transaction import Transaction

class TestWallet(unittest.TestCase):
    def setUp(self):
        self.wallet_a = Wallet()
        self.wallet_b = Wallet()

    def test_deposit_positive_amount(self):
        self.wallet_a.deposit(5000)
        self.assertEqual(self.wallet_a.balance, 5000)

    def test_send_funds(self):
        self.wallet_a.deposit(5000)
        transaction = self.wallet_a.send(self.wallet_b.address, 3000)
        self.wallet_b.receive(transaction)
        self.assertEqual(self.wallet_a.balance, 2000)
        self.assertEqual(self.wallet_b.balance, 3000)

if __name__ == "__main__":
    unittest.main()
