import datetime
import threading

import alpaca_trade_api as tradeapi
import time
from alpaca_trade_api.rest import TimeFrame
import pandas as pd
API_KEY = "PKAXF2MD47AXI6VUE6FQ"
API_SECRET = "HmZJ8wUIAXYjcqu1gCNQ4UT7gJrDzVVdHbd3tzvU"
APCA_API_BASE_URL = "https://paper-api.alpaca.markets"

print("Hello World")