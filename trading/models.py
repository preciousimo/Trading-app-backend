from django.db import models

class TradingAccount(models.Model):
    name = models.CharField(blank=True, max_length=50)
    server = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    investor_password = models.CharField(max_length=50)
    platform = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Equity(models.Model):
    account = models.ForeignKey(TradingAccount, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

class Balance(models.Model):
    account = models.ForeignKey(TradingAccount, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

class MarketWatchTime(models.Model):
    account = models.ForeignKey(TradingAccount, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=100)
    bid = models.DecimalField(max_digits=10, decimal_places=5)
    ask = models.DecimalField(max_digits=10, decimal_places=5)
    timestamp = models.DateTimeField(auto_now_add=True)

