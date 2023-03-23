from celery import shared_task
from .models import TradingAccount, Equity, Balance, MarketWatchTime
import MetaTrader5 as mt5

@shared_task
def fetch_data():
    # Connect to the MetaTrader 5 terminal
    mt5.initialize()

    # Define the list of accounts
    accounts = [
        {"server": "Deriv-Demo", "login": 22014542, "password": "duzftxd8", "platform": mt5.PLATFORM_TYPE_DESKTOP},
        {"server": "ICMarketsEU-Demo", "login": 51135132, "password": "yym2fmut", "platform": mt5.PLATFORM_TYPE_DESKTOP},
        {"server": "ICMarketsEU-Demo", "login": 51135134, "password": "u5qoleim", "platform": mt5.PLATFORM_TYPE_DESKTOP}
    ]

    # Loop through each account and fetch data
    for acc in accounts:
        # Connect to the account
        if not mt5.login(acc["login"], acc["password"], server=acc["server"], platform=acc["platform"]):
            print("Failed to connect to account ", acc["login"])
            continue

        # Fetch the account information
        account_info = mt5.account_info()
        account = TradingAccount.objects.create(
            name=account_info.name,
            login=account_info.login,
            server=account_info.server,
            currency=account_info.currency,
            leverage=account_info.leverage,
            balance=account_info.balance,
            equity=account_info.equity
        )

        # Fetch equity
        equity = mt5.account_info().equity
        Equity.objects.create(account=account, equity=equity)

        # Fetch balance
        balance = mt5.account_info().balance
        Balance.objects.create(account=account, balance=balance)

        # Fetch market watch time
        market_watch_time = mt5.market_watch_time()
        MarketWatchTime.objects.create(account=account, market_watch_time=market_watch_time)

        # Disconnect from the account
        mt5.shutdown()
