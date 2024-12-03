import logging
import uuid
from .transaction import Transaction
from .coin import FakeCoin

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Wallet:
    def __init__(self):
        self.address = str(uuid.uuid4())
        self.balance = 0
        self.transactions = []

    def deposit(self, amount: int):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        self.balance += amount
        logging.info(f"Deposited {FakeCoin.format_amount(amount)} into wallet {self.address}.")

    def send(self, receiver_address: str, amount: int) -> Transaction:
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        transaction = Transaction(sender=self.address, receiver=receiver_address, amount=amount)
        self.balance -= amount
        self.transactions.append(transaction)
        logging.info(f"Sent {FakeCoin.format_amount(amount)} from {self.address} to {receiver_address}.")
        return transaction

    def receive(self, transaction: Transaction):
        if transaction.receiver != self.address:
            raise ValueError("Transaction receiver address mismatch.")
        self.balance += transaction.amount
        self.transactions.append(transaction)
        logging.info(f"Received {FakeCoin.format_amount(transaction.amount)} in wallet {self.address}.")

    def get_balance(self) -> str:
        return FakeCoin.format_amount(self.balance)

    def __repr__(self):
        return f"Wallet(address={self.address}, balance={self.get_balance()})"
