import os
from web3 import Web3
from dotenv import load_dotenv
load_dotenv()


# Сделал .env, чтобы хранить переменные
token_address = os.getenv("TOKEN_ADDRESS")
POLYGON_RPC = os.getenv("POLYGON_RPC")
ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API")
ETHERSCAN_URL = os.getenv("ETHERSCAN_URL")


print("TOKEN_ADDRESS from .env:", token_address)
print("POLYGON_RPC from .env:", POLYGON_RPC)

if not token_address or not POLYGON_RPC:
    raise ValueError("TOKEN_ADDRESS или POLYGON_RPC не заданы в .env")


TOKEN_ADDRESS = Web3.to_checksum_address(token_address)


w3 = Web3(Web3.HTTPProvider(POLYGON_RPC))
print("Connected:", w3.is_connected())



# Нашел в документации Ethereum.org  https://ethereum.org/sn/developers/docs/standards/tokens/erc-20/ + добавил то что нужно
simplified_abi = [
    {
        'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}],
        'name': 'balanceOf',
        'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
        'stateMutability': 'view', 'type': 'function', 'constant': True
    },
    {
        'inputs': [],
        'name': 'decimals',
        'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}],
        'stateMutability': 'view', 'type': 'function', 'constant': True
    },
    {
    'inputs': [],
    'name': 'name',
    'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}],
    'stateMutability': 'view',
    'type': 'function',
    'constant': True
    },
    {
        'inputs': [],
        'name': 'symbol',
        'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}],
        'stateMutability': 'view', 'type': 'function', 'constant': True
    },
    {
        'inputs': [],
        'name': 'totalSupply',
        'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
        'stateMutability': 'view', 'type': 'function', 'constant': True
    },
    {
        "anonymous": False,
        "inputs": [
            {"indexed": True, "name": "from", "type": "address"},
            {"indexed": True, "name": "to", "type": "address"},
            {"indexed": False, "name": "value", "type": "uint256"}
        ],
        "name": "Transfer",
        "type": "event"
    }
]

token_contract = w3.eth.contract(w3.to_checksum_address(TOKEN_ADDRESS), abi=simplified_abi)
