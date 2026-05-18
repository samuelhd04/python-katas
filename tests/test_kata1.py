from src.kata1_dictionary import Dictionary
from unittest.mock import MagicMock


def test_entry_found():
    d = Dictionary()
    d.collection = MagicMock()
    d.collection.find_one.return_value = {"definition": "A fruit that grows on trees"}
    assert d.look("Apple") == "A fruit that grows on trees"


def test_entry_not_found():
    d = Dictionary()
    d.collection = MagicMock()
    d.collection.find_one.return_value = None
    assert d.look("Banana") == "Can't find entry for Banana"
