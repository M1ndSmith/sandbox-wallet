import unittest
from sandbox_wallet.wallet import Wallet
from sandbox_wallet.microtransaction import MicroTransaction

class TestMicroTransaction(unittest.TestCase):
    def setUp(self):
        self.wallet_a = Wallet()
        self.wallet_b = Wallet()
        self.wallet_a.deposit(10000)
        self.micro_tx = MicroTransaction(self.wallet_a, self.wallet_b)

    def test_send_data_success(self):
        data_chunks = ["Chunk1", "Chunk2"]
        cost_per_chunk = 4000
        success = self.micro_tx.send_data(data_chunks, cost_per_chunk)
        self.assertTrue(success)
        self.assertEqual(self.wallet_a.balance, 2000)
        self.assertEqual(self.wallet_b.balance, 8000)

if __name__ == "__main__":
    unittest.main()
