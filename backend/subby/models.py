from django.db import models
from datetime import timedelta
from dateutil.relativedelta import relativedelta

# Create your models here.

class Subscription(models.Model):

    BILLING_PERIOD = [
        ("weekly", "Weekly"),
        ("monthly", "Monthly"),
        ("yearly", "Yearly")
    ]

    #user ДОБАВЬ АВТОРИЗАЦИЮ И ВСЕ ОСТАЛЬНОЕ ОТ АУТЕНТИФИКАЦИИ ТЫ СМОЖЕШ БРО И Т.Д.
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    billing = models.CharField(max_length=10, choices=BILLING_PERIOD, default="monthly")
    start_date = models.DateField()
    next_payment_date = models.DateField()


    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def calculate_next_payment(self):
        if self.billing == "weekly":
            self.next_payment_date += timedelta(days=7)
        elif self.billing == "monthly":
            self.next_payment_date += relativedelta(months=1)
        else:
            self.next_payment_date += relativedelta(years=1)

