from src.kata3_nth_letter import nth_letter


def test_basic():
    assert nth_letter(["yoda", "best", "has"]) == "yes"


def test_empty():
    assert nth_letter([]) == ""
