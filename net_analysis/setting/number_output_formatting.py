import locale
from functools import wraps

locale.setlocale(locale.LC_ALL, '')

def display_locale(gui_mode=False):
    """ 
    Αν ο χρήστης γράψει `@display_locale` χωρίς παρένθεση
    """
    if callable(gui_mode):
        func = gui_mode
        gui_mode = False  # Προεπιλογή
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, (int, float)):
                formatted_result = locale.format_string("%.2f", result, grouping=True)
                print(formatted_result)  # Για CLI, εμφανίζει αυτόματα
                return result  # Κρατάει την αριθμητική τιμή για επεξεργασία
            return result
        return wrapper

    # Αν ο χρήστης γράψει `@display_locale(gui_mode=True)`
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, (int, float)):
                formatted_result = locale.format_string("%.2f", result, grouping=True)
                if gui_mode:
                    return formatted_result  # Για GUI, επιστρέφει string
                print(formatted_result)  # Για CLI, εμφανίζει αυτόματα
            return result  # Αν δεν είναι αριθμός, επιστρέφει κανονικά την τιμή
        return wrapper
    return decorator