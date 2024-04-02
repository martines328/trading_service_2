import threading
import logging
from Strategy.macd_sprtrnd_strategy_2h import Macd_sprtrnd_strategy_2h


def main():


    ts_macd_strategy = Macd_sprtrnd_strategy_2h()
    thread3 = threading.Thread(target=ts_macd_strategy.trade_strategy())
    thread3.start()
    logging.info("Start strategy thread")

if __name__ == "__main__":
    main()