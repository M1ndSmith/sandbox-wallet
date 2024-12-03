# Sandbox Wallet

**Sandbox Wallet** is a Python package that simulates a cryptocurrency wallet system for a fake coin called **SandboxCoin (SBC)**. This project is designed to demonstrate wallet functionality, including transactions, microtransactions, and logging.

The wallet supports basic features like creating accounts, depositing funds, transferring funds, and handling microtransactions tied to data chunks. It also includes a robust logging mechanism for detailed tracking of all operations.

## Features

- **Wallet Management**: Create wallets with unique addresses and manage balances.
- **Fund Transfers**: Send and receive transactions securely between wallets.
- **Microtransactions**: Perform transactions for individual data chunks, ensuring sender wallets have sufficient funds.
- **Error Handling**: Automatically cancel transactions if the sender's balance is insufficient.
- **Logging**: Track all transactions and wallet operations with detailed logs.
- **Extensibility**: Modular design allows for easy expansion of features.

## Project Structure

sandbox_wallet/
├── sandbox_wallet/
│   ├── __init__.py # Package initializer
│   ├── wallet.py # Wallet class for managing balances
│   ├── transaction.py # Transaction class for transfers
│   ├── microtransaction.py # MicroTransaction class for chunked data transfers
│   └── coin.py # Coin details and formatting
├── tests/
│   ├── test_wallet.py # Unit tests for Wallet functionality
│   └── test_microtransaction.py # Unit tests for MicroTransaction
├── setup.py # Package installation setup
├── README.md # Project documentation
└── requirements.txt # Required dependencies

## Installation

Install the package locally using `pip`:

```bash
git clone https://github.com/your-username/sandbox-wallet.git
cd sandbox-wallet
pip install .


##Usage
Basic Wallet Operations

from sandbox_wallet import Wallet

# Create wallets
wallet_a = Wallet()
wallet_b = Wallet()

# Deposit funds
wallet_a.deposit(10000)  # 100 SBC

# Transfer funds
transaction = wallet_a.send(wallet_b.address, 5000)  # 50 SBC
wallet_b.receive(transaction)

# Check balances
print(wallet_a.get_balance())  # 50 SBC remaining


##Microtransactions with Data Chunks

from sandbox_wallet import MicroTransaction

# Define data chunks and cost per chunk
data_chunks = ["Chunk1", "Chunk2", "Chunk3"]
cost_per_chunk = 2000  # 20 SBC per chunk

# Perform microtransactions
micro_tx = MicroTransaction(wallet_a, wallet_b)
success = micro_tx.send_data(data_chunks, cost_per_chunk)
if success:
    print("All data chunks sent successfully!")
else:
    print("Transaction failed due to insufficient funds.")


##Testing
Run unit tests to ensure everything is functioning as expected:

python -m unittest discover tests

##Contributing
Contributions are welcome! Please feel free to fork the repository and submit pull requests.
print(wallet_b.get_balance())  # 50 SBC received