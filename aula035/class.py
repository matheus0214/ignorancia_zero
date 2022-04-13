"""Class"""


def sum_values(*items, **kwargs):
    """Sum all values"""
    print(items, kwargs.get("name"))


sum_values(1, 2.3)
