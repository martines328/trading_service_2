import time

api_key_real = "m3S7fP39dVm799Bm82JoZezWyK6pJcnTW0jT29KFzBwHTBlPtqnyTzxp4ruRcx1P"
api_secret_real = "bwZavuplh3C3XqU1pi4UrOZtsSC6jQiyYpKNye8tHZj1H6dsuQtLAnjKHrlapg8P"


BINANCE_API_KEY_testnet = "c918f6403af5360d974839e4d86c104014c12161753e1a5b5cf81e8fe42cef2d"
BINANCE_SECRET_KEY_testnet = "eff3ac725ff3f6b7007d42330b379be67abfd3129d14ab932c3f19cc99a7ee7a"


apikey_spot = '325u4zxwLBUBrShKFCBC8TJ37QBmSz6BogvuWROv6nE8iLIVCzSvjasJeiqFBUxN'
apisecret_spot = '6D01DR6MCI21ZeihNJZR3wgDYMkucHHgO4KRzEg2qtDKGcvaAQPb0IfDKngqI90m'

timestamp = int(time.time() * 1000)
recvWindow = 5000




# !!!!!!!!!! 2H MACD SuperTrendStrategy!!!!!!!!!!
ts_macd_symbol = "MATICUSDT"
ts_macd_interval = '2h'
ts_macd_interval_start_time = '15 day ago UTC'
ts_macd_pos_amount = 25
ts_macd_leverage = 7
ts_macd_delay_time = 3600  #300
ts_macd_position_delay_time = 5  #60
ts_macd_trailing_activation_percent = 2.5
ts_macd_callback_rate = 2.4

ts_macd_round = 4
round_amount = 0
round_price = 4




ts_macd_manage_pos_interval = '2h'
ts_macd_manage_start_time = '10 day ago UTC'
ts_macd_manage_delayt_time = 7200 #in sec for 1hours manage