from coinapi_v1 import CoinAPIv1
import datetime

test_key = '81531D7E-B89D-485D-A00F-C403B163FFB1'

api = CoinAPIv1(test_key)
exchanges = api.metadata_list_exchanges()

symbols = api.metadata_list_symbols()
print('Symbols')
for symbol in symbols:
   #if(symbol['exchange_id']=="BITFINEX"): <= 例 BITFINEX を指定した場合
   if(symbol['exchange_id']=="BITFINEX"):
       print('Symbol ID: %s' % symbol['symbol_id'])
    
