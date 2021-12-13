import time
import krakenex
from pykrakenapi import KrakenAPI

api = krakenex.API()
k = KrakenAPI(api)

ticker = k.get_ticker_information('BTCGBP')
print(ticker.T)

#legend
#a = ask array(<price>, <whole lot volume>, <lot volume>)
#b = bid array(<price>, <whole lot volume>, <lot volume>)
#c = last trade closed array(<price>, <lot volume>)
#v = volume array(<today>, <last 24 hours>)
#p = volume weighted average price array(<today>, <last 24 hours>)
#t = number of trades array(<today>, <last 24 hours>)
#l = low array(<today>, <last 24 hours>)
#h = high array(<today>, <last 24 hours>)
#o = today’s opening price
