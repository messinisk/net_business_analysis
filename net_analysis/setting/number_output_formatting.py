import locale
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
locale.setlocale(locale.LC_ALL, "")


def display_locale(value):
    """
    Αντικαθιστά το round() και μορφοποιεί το αποτέλεσμα σύμφωνα με το locale.
    """

    if isinstance(value, (int, float)):
        value = abs(value)
        formatted_value = locale.format_string("%.2f", value, grouping=True)
        return formatted_value
    else:
        return value  # Αν δεν είναι αριθμός, επιστρέφει το αρχικό δεδομένο


def is_valid_number(value) -> float | str:
    if isinstance(value, (int, float)):
        if value == 0:
            return "The value must not be zero."
        else:
            return abs(value)  # Επιστρέφουμε την απόλυτη τιμή

    if isinstance(value, str):
        if value.lstrip("-").isdigit():  # Αν είναι αριθμός
            value = value.lstrip("-").replace("-", "")
            return abs(float(value))  # Επιστρέφουμε την απόλυτη τιμή
    return f"this -> ({value}) Not number"  # Αν δεν είναι αριθμός
