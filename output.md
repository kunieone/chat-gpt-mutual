import requests
import json
import time
import hmac
import hashlib
import base64

def get_sign(timestamp, method, request_path, secret_key):
    message = timestamp + method + request_path
    signature = hmac.new(bytes(secret_key, encoding='utf8'), bytes(message, encoding='utf-8'), hashlib.sha256).digest()
    return base64.urlsafe_b64encode(signature).decode()

def get_header(api_key, sign):
    return {
        'OK-ACCESS-KEY': api_key,
        'OK-ACCESS-SIGN': sign,
        'OK-ACCESS-TIMESTAMP': timestamp,
        'Content-Type': 'application/json'
    }

if __name__ == '__main__':
    api_key = 'your_api_key'
    secret_key = 'your_secret_key'
    timestamp = str(round(time.time()))
    method = 'GET'
    request_path = '/users/self/verify'
    sign = get_sign(timestamp, method, request_path, secret_key)
    header = get_header(api_key, sign)
    response = requests.get('https://www.okex.com' + request_path, headers=header)
    print(response.json())
##############################
I want to connect to the OKEx API and use the Python language to develop a quantitative trading script. The general logic of this script is as follows: every day at 0 o'clock in the morning, start monitoring all the "perpetual contract" digital currencies in the market, integrate the trading volume and amplitude, and "whether the unilateral growth/decline" to select, the relative volatility is the strongest, the trading volume and other data The currency is marked. After that, these currencies will be short or long respectively by the MACD cross strategy.

The specific process is as follows:

1. Get all the digital currency pairs of "perpetual contract" through the interface.

2. Get the real-time data of these digital currency pairs through the interface, including: last price, trading volume, etc.

3. According to the data volume and amplitude, etc. of these digital currency pairs, select the currency with the strongest relative volatility and the largest trading volume.

4. According to the MACD cross strategy, short or long these currencies respectively.
##############################</code>





A:

I want to connect to the OKEx API and use the Python language to develop a quantitative trading script. The general logic of this script is as follows: every day at 0 o'clock in the morning, start monitoring all the "perpetual contract" digital currencies in the market, integrate the trading volume and amplitude, and "whether the unilateral growth/decline" to select, the relative volatility is the strongest, the trading volume and other data The currency is marked. After that, these currencies will be short or long respectively by the MACD cross strategy.

api_key:??????API????????????????????????????????????????????????
passphrase:APIKey?????????
timestamp:Unix Epoch ????????????????????????
sign:???????????????????????????????????????
??????timestamp ??? method ???requestPath ?????????????????????????????????HMAC SHA256?????????????????????????????????SecretKey?????????????????????Base64??????
SecretKey:????????????APIKey????????????????????????????????????22582BD0CFF14C41EDBF1AB98506286D
?????? timestamp ??????:const timestamp = '' + Date.now() / 1,000
?????? sign ??????: sign=CryptoJS.enc.Base64.stringify(CryptoJS.HmacSHA256(timestamp +'GET'+ '/users/self/verify', secret))
method ?????? 'GET'
requestPath ?????? '/users/self/verify'
???????????????
WebSocket???HTML5???
##############################??????????????????????????????????????????????????????Websocket???????????????
##############################???

import websocket
import json

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        ws.send(json.dumps({'op':'login','args':[{'apiKey':'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx','passphrase':'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx','timestamp':'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx','sign':'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'}]}))
        ws.send(json.dumps({'op':'subscribe','args':['spot/ticker:BTC-USDT']}))
        time.sleep(1)
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://wsaws.okx.com:8443/ws/v5/private",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
##############################????????????????????????????????????????????????Websocket???????????????????????????????????????????????????????????????????????????API?????????
????????????
?????????????????????????????????????????????????????????24???????????????????????????
??????100ms???????????????????????????????????????????????????????????????????????????????????????????????????????????????
????????????
{
    "op": "subscribe",
    "args": [{
        "channel": "tickers",
        "instId": "LTC-USD-200327"
    }]
}
????????????

??????	??????	????????????	??????
op	String	???	?????????subscribe unsubscribe
args	Array	???	???????????????????????????
> channel	String	???	????????????tickers
> instId	String	???	??????ID
##############################I want to connect to the OKEx API and use the Python language to develop a quantitative trading script. The general logic of this script is as follows: every day at 0 o'clock in the morning, start monitoring all the "perpetual contract" digital currencies in the market, integrate the trading volume and amplitude, and "whether the unilateral growth/decline" to select, the relative volatility is the strongest, the trading volume and other data The currency is marked. After that, these currencies will be short or long respectively by the MACD cross strategy.
 
api_key:??????API???????????????????????????????????????????????? passphrase:APIKey????????? timestamp:Unix Epoch ???????????????????????? sign:???????????????????????????????????????
??????timestamp ??? method ???requestPath ?????????????????????????????????HMAC SHA256?????????????????????????????????SecretKey?????????????????????Base64??????
SecretKey:????????????APIKey????????????????????????????????????22582BD0CFF14C41EDBF1AB98506286D
?????? timestamp ??????:const timestamp = '' + Date.now() / 1,000
?????? sign ??????: sign=CryptoJS.enc.Base64.stringify(CryptoJS.HmacSHA256(timestamp +'GET'+ '/users/self/verify', secret))
method ?????? 'GET'
requestPath ?????? '/users/self/verify'
???????????????
WebSocket???HTML5??????????????????
##############################?????????????????????????????????????????????????????????????????????Websocket???????????????????????????????????????????????????????????????????????????API?????????
????????????
?????????????????????????????????????????????????????????24???????????????????????????
??????100ms???????????????????????????????????????????????????????????????????????????????????????????????????????????????
????????????
{    "op": "subscribe",    "args": [{        "channel": "tickers",        "instId": "LTC-USD-200327"    }]}????????????

??????	??????	????????????	??????
op	String	???	?????????subscribe unsubscribe
args	Array	???	???????????????????????????
> channel	String	???	????????????tickers
> instId	String	???	??????ID
##############################????????????

def get_price(currency):
    # ??????Websocket
    ws = create_connection("wss://wsaws.okx.com:8443/ws/v5/private")
    # ??????????????????
    subscribe_data = {
        "op": "subscribe",
        "args": [{
            "channel": "tickers",
            "instId": currency
        }]
    }
    ws.send(json.dumps(subscribe_data))
    # ????????????
    result =  ws.recv()
    # ??????Websocket??????
    ws.close()
    # ????????????
    data = json.loads(result)
    # ????????????
    return data
##############################??????????????????????????????

?????????Websocket????????????
????????????????????????Websocket??????
?????????????????????????????????????????????Websocket???????????????????????????????????????????????????????????????????????????API??????????????????????????????????????????????????????????????????????????????24?????????????????????????????????100ms???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????{    "op": "subscribe",    "args": [{        "channel": "tickers",        "instId": "LTC-USD-200327"    }]}??????????????????	??????	????????????	??????op	String	???	?????????subscribe unsubscribeargs	Array	???	???????????????????????????> channel	String	???	????????????tickers> instId	String	???	??????ID
##############################?????????

I want to connect to the OKEx API and use the Python language to develop a quantitative trading script. The general logic of this script is as follows: every day at 0 o'clock in the morning, start monitoring all the "perpetual contract" digital currencies in the market, integrate the trading volume and amplitude, and "whether the unilateral growth/decline" to select, the relative volatility is the strongest, the trading volume and other data The currency is marked. After that, these currencies will be short or long respectively by the MACD cross strategy. api_key:??????API???????????????????????????????????????????????? passphrase:APIKey????????? timestamp:Unix Epoch ???????????????????????? sign:?????????????????????????????????????????????timestamp ??? method ???requestPath ?????????????????????????????????HMAC SHA256?????????????????????????????????SecretKey?????????????????????Base64??????SecretKey:????????????APIKey????????????????????????????????????22582BD0CFF14C41EDBF1AB98506286D?????? timestamp ??????:const timestamp = '' + Date.now() / 1,000?????? sign ??????: sign=CryptoJS.enc.Base64.stringify(CryptoJS.HmacSHA256(timestamp +'GET'+ '/users/self/verify', secret))method ?????? 'GET'requestPath ?????? '/users/self/verify'???????????????WebSocket???HTML5??????
##############################
##############################
##############################
##############################