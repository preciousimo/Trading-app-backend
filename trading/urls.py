from django.urls import path
from .views import TradingAccountList, TradingAccountDetail, EquityList, EquityDetail, BalanceList, BalanceDetail, MarketWatchTimeList, MarketWatchTimeDetail

urlpatterns = [
    path('accounts/', TradingAccountList.as_view()),
    path('accounts/<int:pk>/', TradingAccountDetail.as_view()),
    path('equities/', EquityList.as_view()),
    path('equities/<int:pk>/', EquityDetail.as_view()),
    path('balances/', BalanceList.as_view()),
    path('balances/<int:pk>/', BalanceDetail.as_view()),
    path('marketwatchtimes/', MarketWatchTimeList.as_view()),
    path('marketwatchtimes/<int:pk>/', MarketWatchTimeDetail.as_view()),
]
