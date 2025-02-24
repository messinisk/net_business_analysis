def doc_decorator(attr_name):
    def wrapper(func):
        doc = getattr(MetaArgs, attr_name, "")
        func.__doc__ = doc
        return func
    return wrapper

class MetaArgs:
    """Documentation args"""
    
    cost_of_goods_sold = """
[Documentation cost_of_goods_sold]
[A key factor affecting the mixed results for the year is the cost of inventory sold. ]
[Cost of sales includes the difference between turnover and gross operating results]"""

    average_stock = """
[Documentation average_stock]\n[The average inventory is half of the maximum inventory ( [production per day - demand per day] x production period in days).          ]
"""

@doc_decorator("cost_of_goods_sold")
@doc_decorator("average_stock")
class FunCost:
    pass

# Έλεγχος του docstring
print(FunCost.__doc__)
