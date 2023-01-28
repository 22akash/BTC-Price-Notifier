
import requests
import time
# global variables
api_key = '4fb54833-eaaf-4920-ba3a-6ddf99e35f20'
bot_token = '1868999599:AAFLRlvZUsCpRBIB1ucSWt_QzHdUsoIZlYo'
chat_id = '1543567877'

#Set threshold time limit for notifications

threshold = 40000
time_interval = 1 * 15

def get_btc_price():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    headers = {'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key }

    # make a request to the coinmarketcap api
    response = requests.get(url, headers=headers)
    response_json = response.json()
    
# extract the bitcoin price from the json data
    btc_price = response_json['data'][0]
    return btc_price['quote']['USD']['price']

# fn to send_message through telegram
def send_message1(chat_id, msg):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={msg}"
    
# send the msg
    requests.get(url)

# main fn
def main():
    price_list = []

# infinite loop
    while True:
        price = get_btc_price()
        price_list.append(price)

# if the price falls below threshold, send an immediate msg
        if price < threshold:
            send_message(chat_id = chat_id, msg=f'BTC Price Drop Alert: {price}')

# send last 6 btc price
        if len(price_list) >= 6:
            send_message(chat_id=chat_id, msg=price_list)
      
            # empty the price_list
            price_list= []

# fetch the price for every dash minutes
        time.sleep(time_interval)
  
  
# The Main() function
if __name__ == '__main__':
    main()
