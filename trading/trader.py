import datetime
import time
import psycopg2
import MetaTrader5 as mt5

# Connect to PostgreSQL database
conn = psycopg2.connect(
    database="database_name",
    user="postgres",
    password="your_password",
    host="localhost",
    port="5432"
)

# Set the database cursor
cur = conn.cursor()

# Login to each trading account
logins = [22014542, 51135132, 51135134]
for login in logins:
    mt5.initialize()
    authorized = mt5.login(login=login, password="investor_password")
    if not authorized:
        print(f"Failed to connect to account {login}")
        continue

    # Fetch the equity, balance, and market watch time data
    equity = mt5.account_info().equity
    balance = mt5.account_info().balance
    market_watch_time = mt5.market_watch_time()
    timestamp = datetime.datetime.now()

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
