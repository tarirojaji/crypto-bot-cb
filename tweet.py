from nltk.util import pr
from numpy.lib.index_tricks import diag_indices_from
# from numpy import negative, positive
import requests
import auth
from datetime import datetime
import time
import schedule
import tweet_data
from tweet_data import positive, negative

buy_amount = 0.2
sell_amount = 0.3

diff, diff_n = 0, 0

# p, n = 30, 70

if positive > negative:
    diff = ((positive-negative)/((positive+negative)/2))*100
elif positive < negative:
    diff_n = (((negative-positive)/((negative+positive)/2))*100)*-1

print(diff, diff_n)

# if p > n:
#     diff = ((p-n)/((p+n)/2))*100
# elif p < n:
#     diff_n = (((n-p)/((n+p)/2))*100)*-1


def twt():
    if not diff_n:
        pass
    if int(diff) >= 30:
        print(f'Buying {buy_amount} Bitcoin')
        auth.auth_client.buy(product_id='BTC-US', size=buy_amount, order_type='market' )
    elif diff_n and int(diff_n) >= 30:
        print(f'Selling {sell_amount} Bitcoin')
        auth.auth_client.sell(product_id='BTC-US', size=sell_amount, order_type='market' )
    else:
        print('hodl')
    

schedule.every().day.at('05:51:00').do(twt)

while True:
    schedule.run_pending()
    time.sleep(1)

# while True:
#     twt()
#     time.sleep(10)