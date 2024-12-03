class Transaction:
    def __init__(self, sender: str, receiver: str, amount: int):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def __repr__(self):
        return f"Transaction(sender={self.sender}, receiver={self.receiver}, amount={self.amount})"
