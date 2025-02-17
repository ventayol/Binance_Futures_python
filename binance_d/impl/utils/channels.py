import json
from binance_d.impl.utils.timeservice import get_current_timestamp
from binance_d.model import DepthStep


def aggregate_trade_channel(symbol):
    channel = dict()
    channel["params"] = list()
    channel["params"].append(symbol + "@aggTrade")
    channel["id"] = get_current_timestamp()
    channel["method"] = "SUBSCRIBE"
    return json.dumps(channel)

def index_price_channel(pair):
    channel = dict()
    channel["params"] = list()
    channel["params"].append(pair + "@indexPrice")
    channel["id"] = get_current_timestamp()
    channel["method"] = "SUBSCRIBE"
    return json.dumps(channel)

def mark_price_channel(symbol):
    channel = dict()
    channel["params"] = list()
    channel["params"].append(symbol + "@markPrice@1s")
    channel["id"] = get_current_timestamp()
    channel["method"] = "SUBSCRIBE"
    print(channel)
    return json.dumps(channel)

def continuous_kline_channel(pair, contract_type, interval):
    channel = dict()
    channel["params"] = list()
    channel["params"].append(pair + '_' + contract_type + "@continuousKline_" + interval)
    channel["id"] = get_current_timestamp()
    channel["method"] = "SUBSCRIBE"
    return json.dumps(channel)

def kline_channel(symbol, interval):
    channel = dict()
    channel["params"] = list()
    channel["params"].append(symbol + "@kline_" + interval)
    channel["id"] = get_current_timestamp()
    channel["method"] = "SUBSCRIBE"
    return json.dumps(channel)

def mark_price_kline_channel(symbol, interval):
    channel = dict()
    channel["params"] = list()
    channel["params"].append(symbol + "@markPriceKline_" + interval)
    channel["id"] = get_current_timestamp()
    channel["method"] = "SUBSCRIBE"
    return json.dumps(channel)

def index_kline_channel(pair, interval):
    channel = dict()
    channel["params"] = list()
    channel["params"].append(pair + "@indexPriceKline_" + interval)
    channel["id"] = get_current_timestamp()
    channel["method"] = "SUBSCRIBE"
    return json.dumps(channel)

def trade_channel(symbol):
    channel = dict()
    channel["params"] = list()
    channel["params"].append(symbol + "@trade")
    channel["id"] = get_current_timestamp()
    channel["method"] = "SUBSCRIBE"
    return json.dumps(channel)

def symbol_miniticker_channel(symbol):
    channel = dict()
    channel["params"] = list()
    channel["params"].append(symbol + "@miniTicker")
    channel["id"] = get_current_timestamp()
    channel["method"] = "SUBSCRIBE"
    return json.dumps(channel)

def all_miniticker_channel():
    channel = dict()
    channel["params"] = list()
    channel["params"].append("!miniTicker@arr")
    channel["id"] = get_current_timestamp()
    channel["method"] = "SUBSCRIBE"
    return json.dumps(channel)

def symbol_ticker_channel(symbol):
    channel = dict()
    channel["params"] = list()
    channel["params"].append(symbol + "@ticker")
    channel["id"] = get_current_timestamp()
    channel["method"] = "SUBSCRIBE"
    return json.dumps(channel)

def all_ticker_channel():
    channel = dict()
    channel["params"] = list()
    channel["params"].append("!ticker@arr")
    channel["id"] = get_current_timestamp()
    channel["method"] = "SUBSCRIBE"
    return json.dumps(channel)

def symbol_bookticker_channel(symbol):
    channel = dict()
    channel["params"] = list()
    channel["params"].append(symbol + "@bookTicker")
    channel["id"] = get_current_timestamp()
    channel["method"] = "SUBSCRIBE"
    return json.dumps(channel)

def all_bookticker_channel():
    channel = dict()
    channel["params"] = list()
    channel["params"].append("!bookTicker")
    channel["id"] = get_current_timestamp()
    channel["method"] = "SUBSCRIBE"
    return json.dumps(channel)

def symbol_liquidation_channel(symbol):
    channel = dict()
    channel["params"] = list()
    channel["params"].append(symbol + "@forceOrder")
    channel["id"] = get_current_timestamp()
    channel["method"] = "SUBSCRIBE"
    return json.dumps(channel)

def all_liquidation_channel(symbol):
    channel = dict()
    channel["params"] = list()
    channel["params"].append("!forceOrder@arr")
    channel["id"] = get_current_timestamp()
    channel["method"] = "SUBSCRIBE"
    return json.dumps(channel)

def book_depth_channel(symbol, limit, update_time):
    channel = dict()
    channel["params"] = list()
    channel["params"].append(symbol + "@depth" + str(limit) + str(update_time))
    channel["id"] = get_current_timestamp()
    channel["method"] = "SUBSCRIBE"
    return json.dumps(channel)

def diff_depth_channel(symbol, update_time):
    channel = dict()
    channel["params"] = list()
    channel["params"].append(symbol + "@depth" + update_time)
    channel["id"] = get_current_timestamp()
    channel["method"] = "SUBSCRIBE"
    return json.dumps(channel)
    
def user_data_channel(listenKey):
    channel = dict()
    channel["params"] = list()
    channel["params"].append(listenKey)
    channel["id"] = get_current_timestamp()
    channel["method"] = "SUBSCRIBE"
    return json.dumps(channel)
