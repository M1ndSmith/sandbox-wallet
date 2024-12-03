class FakeCoin:
    NAME = "SandboxCoin"
    SYMBOL = "SBC"
    DECIMALS = 2

    @staticmethod
    def format_amount(amount: int) -> str:
        return f"{amount / (10 ** FakeCoin.DECIMALS):.2f} {FakeCoin.SYMBOL}"
