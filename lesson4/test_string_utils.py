import pytest
from stringutils import StringUtils

su = StringUtils()

def test_positive_and_negative_capitilize():
    #Positive
    assert su.capitilize("skypro") == "Skypro"
    assert su.capitilize("surgut") == "Surgut"
    assert su.capitilize("moscow") == "Moscow"

    #Negative
    assert su.capitilize("") == ""
    assert su.capitilize(" ") == " "
    assert su.capitilize("123test") == "123test"

def test_positive_and_negative_trim():
      #Positive
    assert su.trim("    Skypro")== "Skypro"
    assert su.trim("  Snegovik")== "Snegovik"
      #Negative
    assert su.trim("")== ""

def to_list(self, string: str, delimeter=",") -> list[str]:
    if self.is_empty(string):
            return []
    return string.split(delimeter)

def contains(self, string: str, symbol: str) -> bool:
        res = False
        try:
            res = string.index(symbol) > -1
        except ValueError:
            pass
        return res

def delete_symbol(self, string: str, symbol: str) -> str:
        if self.contains(string, symbol):
            string = string.replace(symbol, "")
        return string

def starts_with(self, string: str, symbol: str) -> bool:
     return string.startswith(symbol)

def end_with(self, string: str, symbol: str) -> bool:
     return string.endswith(symbol)

def test_is_empty():
    assert su.is_empty("") == True
    assert su.is_empty(" ")== True
    assert su.is_empty("skypro")== False
    assert su.is_empty("/n")== False

def list_to_string(self, lst: list, joiner=", ") -> str:
        string = ""
        length = len(lst)
        if length == 0:
            return string

        for i in range(0, length - 1):
            string += str(lst[i]) + joiner

        return string + str(lst[-1])