from decimal import Decimal

def monthly_avg(queryset):
    avg = Decimal("0")

    for sub in queryset:
        if sub.billing == "weekly":
            avg += sub.price * Decimal("52") / Decimal("12")
        elif sub.billing == "monthly":
            avg += sub.price
        else:
            avg += sub.price / Decimal("12")

    return avg