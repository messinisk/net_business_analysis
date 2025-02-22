import pytest
# import sys
# import os

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from net_analysis.setting.return_func_error import validate_numerical_inputs


class DummyClass:
    @validate_numerical_inputs
    def divide(self, a, b):
        return a / b


@pytest.fixture
def dummy():
    return DummyClass()


def test_valid_flow(dummy):
    """Έλεγχος σωστής ροής με κανονικούς αριθμούς"""
    result = dummy.divide(10, 2)
    assert result == 5


def test_string_conversion_flow(dummy):
    """Έλεγχος αν μετατρέπονται σωστά οι αριθμητικές συμβολοσειρές"""
    result = dummy.divide("10", "2")
    assert result == 5


def test_invalid_string_flow(dummy, capsys):
    """Έλεγχος αν η μη αριθμητική συμβολοσειρά προκαλεί προειδοποίηση"""
    result = dummy.divide("abc", 2)
    captured = capsys.readouterr()
    assert result == 0.0
    assert "δεν είναι αριθμός" in captured.out


def test_non_numeric_flow(dummy, capsys):
    """Έλεγχος αν απορρίπτονται μη αριθμητικά αντικείμενα"""
    result = dummy.divide([10], 2)
    captured = capsys.readouterr()
    assert result == 0.0
    assert "Πρέπει να είναι αριθμός" in captured.out


def test_zero_division_flow(dummy, capsys):
    """Έλεγχος αν η διαίρεση με το μηδέν επιστρέφει άπειρο"""
    result = dummy.divide(10, 0)
    captured = capsys.readouterr()
    assert result == float("inf")
    assert "Δεν μπορεί να γίνει διαίρεση με μηδέν" in captured.out
