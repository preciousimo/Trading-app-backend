import datetime
import time
import psycopg2
from decouple import config
import MetaTrader5 as mt5
from .models import TradingAccount, TradingData

# Connect to PostgreSQL database
conn = psycopg2.connect(
    database=config('DB_NAME'),
    user=config('DB_USER'),
    password=config('DB_PASSWORD'),
    host=config('DB_HOST'),
    port=config('DB_PORT')
)

# Set the database cursor
cur = conn.cursor()

# Login to each trading account
logins = [
    {"login": 22014542, "investor_password": "duzftxd8", "platform": "Deriv-Demo"},
    {"login": 51135132, "investor_password": "yym2fmut", "platform": "ICMarketsEU-Demo"},
    {"login": 51135134, "investor_password": "u5qoleim", "platform": "ICMarketsEU-Demo"},
]

for login_data in logins:
    login = login_data["login"]
    platform = login_data["platform"]
    investor_password = login_data["investor_password"]

    mt5.initialize()
    authorized = mt5.login(login=login, password=investor_password)
    if not authorized:
        print(f"Failed to connect to account {login}")
        continue

    # Create or update the TradingAccount model for this login
    account, created = TradingAccount.objects.get_or_create(
        login=login,
        defaults={
            "investor_password": investor_password,
            "platform": platform,
        }
    )

    # Fetch the equity, balance, and market watch time data
    account_info = mt5.account_info()
    equity = mt5.account_info().equity
    balance = mt5.account_info().balance
    market_watch_time = mt5.market_watch_time()
    timestamp = datetime.datetime.now()

    # Create the TradingData model for this login
    trading_data  = TradingData(
        account=account,
        equity=equity,
        balance=balance,
        market_watch_time=market_watch_time,
        timestamp=timestamp,
    )
    trading_data.save()

    # Insert the data into the PostgreSQL database
    cur.execute(
        f"INSERT INTO trading_data (login, equity, balance, market_watch_time, timestamp) VALUES ({login}, {equity}, {balance}, '{market_watch_time}', '{timestamp}')"
    )

    # Commit the transaction
    conn.commit()

    # Logout from the account
    mt5.shutdown()

# Close the database connection
conn.close()

# Wait for 1 minute before fetching data again
time.sleep(60)
