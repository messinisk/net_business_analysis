from functools import wraps


def is_numeric_string(value: str) -> bool:
    """Επιστρέφει True αν η συμβολοσειρά περιέχει μόνο αριθμούς"""
    try:
        float(value)  # Αν πετύχει η μετατροπή, είναι αριθμός
        return True
    except ValueError:
        return False


def validate_numerical_inputs(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        new_args = []

        for arg in args:
            # Έλεγχος αν είναι string και αν μπορεί να μετατραπεί σε float
            if isinstance(arg, str):
                if is_numeric_string(arg):
                    arg = float(arg)
                else:
                    print(
                        f"⚠ Προειδοποίηση: Το '{arg}'\
                            δεν είναι αριθμός και αγνοείται."
                    )
                    return 0.0  # Αντί για None, επιστρέφουμε 0.0

            # Έλεγχος αν είναι αριθμός
            if not isinstance(arg, (int, float)):
                print(
                    f"⚠ Προειδοποίηση: Μη έγκυρη παράμετρος: {arg}.\
                        Πρέπει να είναι αριθμός."
                )
                return 0.0  # Αντί για None

            new_args.append(abs(arg))  # Μετατροπή σε θετικό

        # Έλεγχος διαίρεσης με το μηδέν
        if any(a == 0 for a in new_args):
            print("⚠ Προειδοποίηση: Δεν μπορεί να γίνει διαίρεση με μηδέν.")
            return float("inf")  # Αντί για None, επιστρέφουμε άπειρο ή 0.0

        return func(self, *new_args, **kwargs)

    return wrapper
