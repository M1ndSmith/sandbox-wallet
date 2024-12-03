import logging
from .transaction import Transaction
from .coin import FakeCoin

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MicroTransaction:
    def __init__(self, sender_wallet, receiver_wallet):
        self.sender_wallet = sender_wallet
        self.receiver_wallet = receiver_wallet
        self.data_sent = 0

    def send_data(self, data_chunks, cost_per_chunk):
        for i, chunk in enumerate(data_chunks):
            if self.sender_wallet.balance < cost_per_chunk:
                logging.error("Insufficient funds. Transaction canceled.")
                return False

            transaction = self.sender_wallet.send(self.receiver_wallet.address, cost_per_chunk)
            self.receiver_wallet.receive(transaction)
            self.data_sent += 1
            logging.info(f"Chunk {i + 1} sent. {FakeCoin.format_amount(cost_per_chunk)} transferred.")

        logging.info(f"All chunks sent. Total sent: {self.data_sent}.")
        return True
