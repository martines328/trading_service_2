import time
import logging
from binance import Client


class Client_Manager():

    def __init__(self, api_key, api_secret, testnet=False ):
        self.api_key = api_key
        self.api_secret = api_secret
        self.testnet = testnet



    def create_binance_client(self):
        try:
            binance_client = Client(self.api_key, self.api_secret, testnet=self.testnet)
            return binance_client
        except Exception as e:
            print(f"Can't create client - {e}")



