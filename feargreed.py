import requests
import auth
# from datetime import datetime
import time
import schedule


resp = requests.get('https://api.alternative.me/fng/').json()
value = resp['data'][0]['value']


# print(auth.auth_client.get_accounts())

# current_time = datetime.now().strftime('%H:%M:%S')
# print(current_time)

buy_amount = 0.2
sell_amount = 0.3


def fng():
    if int(value) <= 30:
        print(f'Buying {buy_amount} Bitcoin')
        auth.auth_client.buy(product_id='BTC-US', size=buy_amount, order_type='market' )
    elif int(value) >= 70:
        print(f'Selling {sell_amount} Bitcoin')
        auth.auth_client.sell(product_id='BTC-US', size=sell_amount, order_type='market' )
    else:
        print('hodl')

schedule.every().day.at('21:37:00').do(fng)

while True:
    schedule.run_pending()
    time.sleep(1)



