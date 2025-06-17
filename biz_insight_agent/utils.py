def calculate_profit(revenue, cost):
    return revenue - cost


def calculate_cac(cost, customers):
    if customers == 0:
        return float('inf')
    return cost / customers


def calculate_percentage_change(today, yesterday):
    if yesterday == 0:
        return 0
    return ((today - yesterday) / yesterday) * 100
