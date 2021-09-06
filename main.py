import cbpro
import time

# refer to passphrase.example for an example file
data = open('passphrase', 'r').read().splitlines()

public = data[0]
passphrase = data[1]
secret = data[2]
api_url = data[3]

auth_client = cbpro.AuthenticatedClient(public, secret, passphrase, api_url)

# print(auth_client)

# print(auth_client.get_accounts())

sell_price = 53000
sell_amount = 0.3

buy_price = 49000
buy_amount = 0.2

while True:
    price = float(auth_client.get_product_ticker(product_id='BTC-USD')['price'])
    if price <= buy_price:
        print(f'Buying {buy_amount} BTC\nCurrent Price: {price:,}\nBuying Price: {buy_price:,}\n')
        auth_client.buy(size=buy_amount, order_type='market', product_id='BTC-USD')
    elif price >= sell_price:
        print(f'Selling {sell_amount} BTC\nCurrent Price: {price:,}\nSelling Price: {buy_price:,}\n')
        auth_client.sell(size=sell_amount, order_type='market', product_id='BTC-USD')
    else:
        print((f"Doing nothing as price is {price:,}\n"))
    time.sleep(10)
