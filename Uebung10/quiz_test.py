from cityquiz import check_guess


def test_check_guess():
    assert check_guess("Ljubljana", "Slovenia", {"Slovenia": "Ljubljana"}) == True
    return "test_check_guess() passed successfully."


print test_check_guess()
