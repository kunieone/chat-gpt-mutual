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

api_key:调用API的唯一标识。需要用户手动设置一个
passphrase:APIKey的密码
timestamp:Unix Epoch 时间戳，单位为秒
sign:签名字符串，签名算法如下：
先将timestamp 、 method 、requestPath 进行字符串拼接，再使用HMAC SHA256方法将拼接后的字符串和SecretKey加密，然后进行Base64编码
SecretKey:用户申请APIKey时所生成的安全密钥，如：22582BD0CFF14C41EDBF1AB98506286D
其中 timestamp 示例:const timestamp = '' + Date.now() / 1,000
其中 sign 示例: sign=CryptoJS.enc.Base64.stringify(CryptoJS.HmacSHA256(timestamp +'GET'+ '/users/self/verify', secret))
method 总是 'GET'
requestPath 总是 '/users/self/verify'
继续：概述
WebSocket是HTML5一
##############################，但是我不知道如何订阅，请问如何订阅Websocket私有频道？
##############################：

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
##############################，请设计一个函数，使用刚才打开的Websocket通道，获取每秒钟市场上所有币种的数据，下面是相关的API文档：
行情频道
获取产品的最新成交价、买一价、卖一价和24小时交易量等信息。
最快100ms推送一次，没有触发事件时不推送，触发推送的事件有：成交、买一卖一发生变动。
请求示例
{
    "op": "subscribe",
    "args": [{
        "channel": "tickers",
        "instId": "LTC-USD-200327"
    }]
}
请求参数

参数	类型	是否必须	描述
op	String	是	操作，subscribe unsubscribe
args	Array	是	请求订阅的频道列表
> channel	String	是	频道名，tickers
> instId	String	是	产品ID
##############################I want to connect to the OKEx API and use the Python language to develop a quantitative trading script. The general logic of this script is as follows: every day at 0 o'clock in the morning, start monitoring all the "perpetual contract" digital currencies in the market, integrate the trading volume and amplitude, and "whether the unilateral growth/decline" to select, the relative volatility is the strongest, the trading volume and other data The currency is marked. After that, these currencies will be short or long respectively by the MACD cross strategy.
 
api_key:调用API的唯一标识。需要用户手动设置一个 passphrase:APIKey的密码 timestamp:Unix Epoch 时间戳，单位为秒 sign:签名字符串，签名算法如下：
先将timestamp 、 method 、requestPath 进行字符串拼接，再使用HMAC SHA256方法将拼接后的字符串和SecretKey加密，然后进行Base64编码
SecretKey:用户申请APIKey时所生成的安全密钥，如：22582BD0CFF14C41EDBF1AB98506286D
其中 timestamp 示例:const timestamp = '' + Date.now() / 1,000
其中 sign 示例: sign=CryptoJS.enc.Base64.stringify(CryptoJS.HmacSHA256(timestamp +'GET'+ '/users/self/verify', secret))
method 总是 'GET'
requestPath 总是 '/users/self/verify'
继续：概述
WebSocket是HTML5一种新的协议
##############################正如你前面写的，请设计一个函数，使用刚才打开的Websocket通道，获取每秒钟市场上所有币种的数据，下面是相关的API文档：
行情频道
获取产品的最新成交价、买一价、卖一价和24小时交易量等信息。
最快100ms推送一次，没有触发事件时不推送，触发推送的事件有：成交、买一卖一发生变动。
请求示例
{    "op": "subscribe",    "args": [{        "channel": "tickers",        "instId": "LTC-USD-200327"    }]}请求参数

参数	类型	是否必须	描述
op	String	是	操作，subscribe unsubscribe
args	Array	是	请求订阅的频道列表
> channel	String	是	频道名，tickers
> instId	String	是	产品ID
##############################。写代码

def get_price(currency):
    # 连接Websocket
    ws = create_connection("wss://wsaws.okx.com:8443/ws/v5/private")
    # 订阅行情频道
    subscribe_data = {
        "op": "subscribe",
        "args": [{
            "channel": "tickers",
            "instId": currency
        }]
    }
    ws.send(json.dumps(subscribe_data))
    # 获取数据
    result =  ws.recv()
    # 关闭Websocket连接
    ws.close()
    # 解析数据
    data = json.loads(result)
    # 返回数据
    return data
##############################时，请注意以下几点：

请使用Websocket私有频道
请使用刚才打开的Websocket通道
请设计一个函数，使用刚才打开的Websocket通道，获取每秒钟市场上所有币种的数据，下面是相关的API文档：行情频道获取产品的最新成交价、买一价、卖一价和24小时交易量等信息。最快100ms推送一次，没有触发事件时不推送，触发推送的事件有：成交、买一卖一发生变动。请求示例{    "op": "subscribe",    "args": [{        "channel": "tickers",        "instId": "LTC-USD-200327"    }]}请求参数参数	类型	是否必须	描述op	String	是	操作，subscribe unsubscribeargs	Array	是	请求订阅的频道列表> channel	String	是	频道名，tickers> instId	String	是	产品ID
##############################写代码

I want to connect to the OKEx API and use the Python language to develop a quantitative trading script. The general logic of this script is as follows: every day at 0 o'clock in the morning, start monitoring all the "perpetual contract" digital currencies in the market, integrate the trading volume and amplitude, and "whether the unilateral growth/decline" to select, the relative volatility is the strongest, the trading volume and other data The currency is marked. After that, these currencies will be short or long respectively by the MACD cross strategy. api_key:调用API的唯一标识。需要用户手动设置一个 passphrase:APIKey的密码 timestamp:Unix Epoch 时间戳，单位为秒 sign:签名字符串，签名算法如下：先将timestamp 、 method 、requestPath 进行字符串拼接，再使用HMAC SHA256方法将拼接后的字符串和SecretKey加密，然后进行Base64编码SecretKey:用户申请APIKey时所生成的安全密钥，如：22582BD0CFF14C41EDBF1AB98506286D其中 timestamp 示例:const timestamp = '' + Date.now() / 1,000其中 sign 示例: sign=CryptoJS.enc.Base64.stringify(CryptoJS.HmacSHA256(timestamp +'GET'+ '/users/self/verify', secret))method 总是 'GET'requestPath 总是 '/users/self/verify'继续：概述WebSocket是HTML5一种
##############################
##############################
##############################
##############################