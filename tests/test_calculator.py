from cautious_computing_machine import calculator


def test_can_add_two_numbers():
    assert calculator.add_number(2, 2) == 4
    assert calculator.add_number(13, 11) == 24
