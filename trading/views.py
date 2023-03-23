from rest_framework import generics
from .models import TradingAccount, Equity, Balance, MarketWatchTime
from .serializers import TradingAccountSerializer, EquitySerializer, BalanceSerializer, MarketWatchTimeSerializer

class TradingAccountList(generics.ListCreateAPIView):
    queryset = TradingAccount.objects.all()
    serializer_class = TradingAccountSerializer

class TradingAccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TradingAccount.objects.all()
    serializer_class = TradingAccountSerializer

class EquityList(generics.ListCreateAPIView):
    queryset = Equity.objects.all()
    serializer_class = EquitySerializer

class EquityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equity.objects.all()
    serializer_class = EquitySerializer

class BalanceList(generics.ListCreateAPIView):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer

class BalanceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer

class MarketWatchTimeList(generics.ListCreateAPIView):
    queryset = MarketWatchTime.objects.all()
    serializer_class = MarketWatchTimeSerializer

class MarketWatchTimeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MarketWatchTime.objects.all()
    serializer_class = MarketWatchTimeSerializer
