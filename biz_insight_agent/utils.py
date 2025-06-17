
def calculate_profit(revenue, cost):
    try:
        return revenue - cost
    except Exception:
        return 0


def calculate_cac(cost, customers):
    if not isinstance(customers, (int, float)) or customers <= 0:
        return 0.0
    return cost / customers


def calculate_percentage_change(today, yesterday):
    if not isinstance(today, (int, float)) or not isinstance(yesterday, (int, float)):
        return 0
    if yesterday == 0:
        return 0
    return ((today - yesterday) / yesterday) * 100
