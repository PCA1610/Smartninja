from rechner import addition_funktion


def testing_addition_funktion():
    assert addition_funktion(value1=2, value2=3) == 5
    return "testing_addition_funktion() passed successfully"


print testing_addition_funktion()
