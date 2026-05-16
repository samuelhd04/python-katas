from src.kata1_dictionary import Dictionary


def test_entry_found():
    d = Dictionary()
    d.newentry("Apple", "A fruit that grows on trees")
    assert d.look("Apple") == "A fruit that grows on trees"


def test_entry_not_found():
    d = Dictionary()
    assert d.look("Banana") == "Can't find entry for Banana"
