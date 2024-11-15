import httpx
import json
from pydantic import BaseModel, Field
from decimal import Decimal
from typing import List, Dict



API_BASE_URL = "https://economia.awesomeapi.com.br/json/last/USD-{currency}"

class USDRate(BaseModel):
    code: str = Field(default="USD")
    codein: str = Field(default="USD")
    name: str = Field(default="Dolar/Dolar")
    value: Decimal = Field(alias="high")

def get_rates(currencies: List[str]) -> Dict[str, USDRate]:
    """Gets current rate for USD vs Currency"""
    return_data = {}
    for currency in currencies:
        if currency == "USD":
            return_data[currency] = USDRate(high=1)
        else:
            response = httpx.get(API_BASE_URL.format(currency=currency))
            if response.status_code == 200:
                data = response.json()["USDBRL"]
                return_data[currency] = USDRate(**data)
            else:
                return_data[currency] = USDRate(name="api/error", high=0)

    return return_data


currencies = ["BRL", "USD"]

rates = get_rates(currencies)

# retorna o valor do dolar em reais
print(rates)
print(rates[currencies[0]].value)
