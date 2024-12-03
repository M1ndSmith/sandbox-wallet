# Sandbox Wallet

## Overview

**Sandbox Wallet** is a Python package that simulates a cryptocurrency wallet system for a fictional cryptocurrency called **SandboxCoin (SBC)**. The project demonstrates comprehensive wallet functionality, including secure transactions, microtransactions, and detailed logging mechanisms.

## Key Features

- **Wallet Management**: 
  * Create wallets with unique addresses 
  * Manage and track wallet balances

- **Fund Transfers**: 
  * Securely send and receive transactions between wallets
  * Robust error handling for insufficient funds

- **Microtransactions**: 
  * Perform transactions for individual data chunks
  * Verify sender wallet has sufficient funds before processing

- **Comprehensive Logging**: 
  * Detailed tracking of all wallet and transaction operations
  * Supports thorough audit and verification processes

- **Extensible Design**: 
  * Modular architecture allows easy feature expansion
  * Flexible implementation for future enhancements

## Project Structure

```
sandbox_wallet/
├── sandbox_wallet/
│   ├── __init__.py       # Package initializer
│   ├── wallet.py         # Wallet class for managing balances
│   ├── transaction.py    # Transaction class for transfers
│   ├── microtransaction.py  # MicroTransaction class for chunked data transfers
│   └── coin.py           # Coin details and formatting
├── tests/
│   ├── test_wallet.py    # Unit tests for Wallet functionality
│   └── test_microtransaction.py  # Unit tests for MicroTransaction
├── setup.py              # Package installation setup
├── README.md             # Project documentation
└── requirements.txt      # Required dependencies
```

## Installation

Clone the repository and install using pip:

```bash
git clone https://github.com/M1ndSmith/sandbox-wallet.git
cd sandbox-wallet
pip install .
Alternatively
Install the package using the setup.py file
python setup.py install

```
## Install Dependencies

Install the required Python libraries using pip:

```bash
pip install -r requirements.txt
```

## Usage Examples

### Basic Wallet Operations

```python
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
```

### Microtransactions with Data Chunks

```python
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
```

## Testing

Run unit tests to ensure package functionality:

```bash
python -m unittest discover tests
```

## Contributing

Contributions are welcome! Feel free to fork the repository, make your changes, and submit a pull request.
