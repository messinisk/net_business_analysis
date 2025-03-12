import pytest
import locale

# Εισαγωγή των συναρτήσεων που θα δοκιμαστούν
from net_analysis.setting.number_output_formatting import (
    display_locale,
    is_valid_number,
)


# Ρύθμιση του locale για τις δοκιμές
locale.setlocale(locale.LC_ALL, "Greek_Greece.1253")


def test_display_locale_with_integer():
    assert display_locale(1234) == "1.234,00"


def test_display_locale_with_float():
    assert display_locale(1234.56) == "1.234,56"


def test_display_locale_with_non_numeric():
    assert display_locale("test") == "test"


def test_is_valid_number_with_positive_int():
    assert is_valid_number(10) == 10


def test_is_valid_number_with_negative_int():
    assert is_valid_number(-10) == 10


def test_is_valid_number_with_zero():
    assert is_valid_number(0) == "The value must not be zero."


def test_is_valid_number_with_numeric_string():
    assert is_valid_number("10") == 10.0


def test_is_valid_number_with_negative_numeric_string():
    assert is_valid_number("-10") == 10.0


def test_is_valid_number_with_non_numeric_string():
    assert is_valid_number("abc") == "this -> (abc) Not number"
