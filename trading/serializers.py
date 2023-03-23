from rest_framework import serializers
from .models import TradingAccount, Equity, Balance, MarketWatchTime

class TradingAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradingAccount
        fields = '__all__'

class EquitySerializer(serializers.ModelSerializer):
    account = TradingAccountSerializer(read_only=True)
    class Meta:
        model = Equity
        fields = '__all__'

class BalanceSerializer(serializers.ModelSerializer):
    account = TradingAccountSerializer(read_only=True)
    class Meta:
        model = Balance
        fields = '__all__'

class MarketWatchTimeSerializer(serializers.ModelSerializer):
    account = TradingAccountSerializer(read_only=True)
    class Meta:
        model = MarketWatchTime
        fields = '__all__'
