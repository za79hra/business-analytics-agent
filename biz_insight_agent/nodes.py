from .utils import calculate_profit, calculate_cac, calculate_percentage_change


def input_node(state):
    return {
        "input_data": state["input_data"]
    }


def processing_node(state):
    data = state["input_data"]
    today = data['today']
    yesterday = data['yesterday']

    profit = calculate_profit(today['revenue'], today['cost'])

    cac = calculate_cac(today['cost'], today['customers'])
    prev_cac = calculate_cac(yesterday['cost'], yesterday['customers'])

    revenue_change = calculate_percentage_change(today['revenue'], yesterday['revenue'])
    cost_change = calculate_percentage_change(today['cost'], yesterday['cost'])
    cac_change = calculate_percentage_change(cac, prev_cac)

    metrics = {
        'profit': profit,
        'cac': cac,
        'cac_change': cac_change,
        'revenue_change': revenue_change,
        'cost_change': cost_change
    }

    return {
        "metrics": metrics
    }


def recommendation_node(state):
    metrics = state["metrics"]
    recommendations = []

    if metrics['profit'] < 0:
        recommendations.append("Reduce costs if profit is negative.")
    if metrics['cac_change'] > 20:
        recommendations.append("Review marketing campaigns, CAC increased.")
    if metrics['revenue_change'] > 0:
        recommendations.append("Consider increasing advertising budget.")

    return {
        "recommendations": {
            'profit': metrics['profit'],
            'cac': metrics['cac'],
            'alerts': recommendations
        }
    }
