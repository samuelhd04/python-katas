from src.kata2_spending import get_total


def test_basic_total():
    costs = {"socks": 5, "shoes": 60, "sweater": 30}
    assert get_total(costs, ["socks", "shoes"], 0.09) == 70.85


def test_item_not_in_costs():
    costs = {"socks": 5}
    assert get_total(costs, ["socks", "hat"], 0.0) == 5.0
