from django.db import models

class Business(models.Model):
    name = models.CharField(max_length=100)
    year_established = models.IntegerField()
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    preAssessment = models.IntegerField(default=20)

class BalanceSheet(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    year = models.IntegerField()
    month = models.IntegerField()
    profit_or_loss = models.DecimalField(max_digits=10, decimal_places=2)
    assets_value = models.DecimalField(max_digits=10, decimal_places=2)
