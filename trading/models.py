from django.db import models

class TradingAccount(models.Model):
    server = models.CharField(max_length=100)
    login = models.CharField(max_length=100)
    investor_password = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.platform} Account {self.login}"
    
class TradingData(models.Model):
    account = models.ForeignKey(TradingAccount, on_delete=models.CASCADE)
    equity = models.DecimalField(max_digits=15, decimal_places=2)
    balance = models.DecimalField(max_digits=15, decimal_places=2)
    market_watch_time = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.account} - {self.timestamp}"