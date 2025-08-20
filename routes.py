from fastapi import APIRouter, Query, status
import requests
from pydantic import BaseModel
from web3 import Web3
from typing import List
from dependecies import token_contract, TOKEN_ADDRESS, ETHERSCAN_API_KEY, ETHERSCAN_URL, token_address, w3, simplified_abi




router = APIRouter(tags=['Tokens'])

# ПУНКТ А
@router.get("/balance", status_code=status.HTTP_200_OK, description="Получить баланс конкретного кошелька. УРОВЕНЬ А")
async def get_balance(wallet_address: str = Query(..., description="Адрес пользователя в сети Polygon")):
    try:
        check_sum_adress = Web3.to_checksum_address(wallet_address)
        symbol = token_contract.functions.symbol().call()
        decimals = token_contract.functions.decimals().call()
        raw_balance = token_contract.functions.balanceOf(check_sum_adress).call()

        balance = raw_balance / (10**decimals)

        return {
            "address": wallet_address,
            "token": symbol,
            "balance": balance
        }
    
    except Exception as e:
        return {"ERROR" : str(e)}



# ПУНКТ Б
class AddressBatch(BaseModel):
    wallet_addresses: list[str]

@router.post("/balance_batch", status_code=status.HTTP_200_OK, description="Получить баланс каждого кошелька из списка. УРОВЕНЬ Б")
async def get_severeal_balances(batch: AddressBatch):
    result = []
    symbol = token_contract.functions.symbol().call()
    decimals = token_contract.functions.decimals().call()
    for wallet_address in batch.wallet_addresses:
        try:
            check_sum_adress = Web3.to_checksum_address(wallet_address)
            raw_balance = token_contract.functions.balanceOf(check_sum_adress).call()
            balance = raw_balance / (10**decimals)

# Вывод как в примере
            result.append(balance)
            
# Вывод покрасивее
            """result.append({
                "symbol":symbol,
                "balance":balance
            })"""

# Расширенный вывод
            """result.append({
                "address":wallet_address,
                "symbol":symbol,
                "decimals": decimals,
                "balance": balance
                })"""
        except Exception as e:
            result.append({"address": wallet_address, "error": str(e)})
    
    return {"balances": result}


# ПУНКТ С
"""Ковырялся, не отрабатывало. В итоге увидел, что этот запрос доступен только для подписчиков Pro версии API 

{
  "status": "0",
  "message": "NOTOK",
  "result": "Sorry, it looks like you are trying to access an API Pro endpoint. Contact us to upgrade to API Pro."
}

"""

"""@router.get("/top_holders")
async def get_top_holders(n: int = Query(..., description="Количество топ адресов")):
    params = {
        "module": "token",
        "action": "tokenholderlist",
        "contractaddress": TOKEN_ADDRESS,
        "page": 1,
        "offset": 1,
        "chainid": 137,
        "apikey": ETHERSCAN_API_KEY
    }

    try:
        response = requests.get(ETHERSCAN_URL, params=params)
        response.raise_for_status()
        data = response.json()

        if data["status"] != "1":
            return {"error": data.get("message", "Unknown error")}

        top_n = [(item["HolderAddress"], int(item["TokenHolderQuantity"])) for item in data["result"]]


        return {"top_holders": top_n}
    except Exception as e:
        return {"error": str(e)}"""

# Пункт E 
@router.get("/get_token_info/{token_address}", status_code=status.HTTP_200_OK, description="Получить информацию. УРОВЕНЬ Е")
async def get_token_info(token_address: str):
    try:
        
        checksum_address = Web3.to_checksum_address(token_address)
        # Создаём контракт именно для этого токена
        contract = w3.eth.contract(address=checksum_address, abi=simplified_abi)


        name = contract.functions.name().call()
        symbol = contract.functions.symbol().call()
        decimals = contract.functions.decimals().call()
        total_supply = contract.functions.totalSupply().call()

        result = {
            "name": name,
            "symbol": symbol,
            "decimals": decimals,
            "totalSupply": total_supply / (10 ** decimals)
        }

        return result

    except Exception as e:
        return {"error": str(e)}
