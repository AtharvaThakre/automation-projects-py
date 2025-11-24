import requests

API_KEY = 'fca_live_loJQtzmxyaQo6v0u1Q6Paghalr9bzmDAGqmQoRZ7'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except Exception as e:
        print(e)
        return None
        
base = input("Enter the base currency (q for quit):").upper()

if base not in CURRENCIES:
    print("Entered BASE Currency is not in OUR API || invalid base")


data = convert_currency(base)
del data[base]

for ticker, value in data.items():
    print(f"{ticker} : {value}")