from string_utils import StringUtils

su = StringUtils()


def test_positive_and_negative_capitilize():

    # Positive
    assert su.capitilize("skypro") == "Skypro"
    assert su.capitilize("surgut") == "Surgut"
    assert su.capitilize("moscow") == "Moscow"

    # Negative
    assert su.capitilize("") == ""
    assert su.capitilize(" ") == " "
    assert su.capitilize("123test") == "123test"


def test_positive_and_negative_trim():

    # Positive
    assert su.trim("    Skypro") == "Skypro"
    assert su.trim("  Snegovik") == "Snegovik"

    # Negative
    assert su.trim("") == ""


def test_to_list():

    # Positive
    assert su.to_list("Moscow,Surgut,Dagestan") == ["Moscow", "Surgut", "Dagestan"]
    assert su.to_list("Moscow-Surgut-Dagestan", "-") == ["Moscow", "Surgut", "Dagestan"]

    # Negative
    assert su.to_list("1-2-3", "-") == ["1", "2", "3"]
    assert su.to_list("") == []


def test_contains():

    # Positive
    assert su.contains("SkyPro", "S") == True
    assert su.contains("Surgut", "S") == True
    assert su.contains("Hi", "H") == True

    # Negative
    assert su.contains("SkyPro", "H") == False
    assert su.contains("", "") == True


def test_delete_symbol():

    # Positive
    assert su.delete_symbol("Surgut", "g") == "Surut"
    assert su.delete_symbol("666metis", "6") == "metis"

    # Negative
    assert su.delete_symbol("Surgut", "a") == "Surgut"
    assert su.delete_symbol("12345", "6") == "12345"
    assert su.delete_symbol("", "g") == ""


def test_starts_with():

    # Positive
    assert su.starts_with("666metis", "6") == True
    assert su.starts_with("Hello", "H") == True
    assert su.starts_with("flash", "f") == True

    # Negative
    assert su.starts_with("666metis", "m") == False
    assert su.starts_with("Flash", "f") == False


def test_end_with():

    # Positive
    assert su.end_with("666metis", "s") == True
    assert su.end_with("Sergut", "t") == True
    assert su.end_with("metis666", "6") == True

    # Negative
    assert su.end_with("666metis", "6") == False
    assert su.end_with("Surgut", "S") == False


def test_is_empty():
    assert su.is_empty("") == True
    assert su.is_empty(" ") == True
    assert su.is_empty("skypro") == False
    assert su.is_empty("/n") == False


def test_list_to_string():

    # Positive
    assert su.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    assert su.list_to_string(["Sur", "Gut"], "-") == "Sur-Gut"
