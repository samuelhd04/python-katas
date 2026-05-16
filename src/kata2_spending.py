def get_total(costs, items, tax):
    total = 0
    for item in items:
        if item in costs:
            total = total + costs[item]
    total_with_tax = total + total * tax
    return round(total_with_tax, 2)
