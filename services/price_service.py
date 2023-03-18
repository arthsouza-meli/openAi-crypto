import requests

class echo "# openAi-crypto" >> README.md

    def __init__(self):
        self.base_url = "https://api.coingecko.com/api/v3"

    def fetch_crypto_price(self, cryptocurrency):
        url = f"{self.base_url}/simple/price?ids={cryptocurrency}&vs_currencies=usd"
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception(f"CoinGecko API request failed with status code {response.status_code}")

        response_json = response.json()
        price = response_json[cryptocurrency]["usd"]

        return price

