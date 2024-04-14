import pytest
from src.Payment import Payment


@pytest.mark.parametrize("name, number, expected", [
    ("Счет", "75106830613657916952", "**6952"),
    ("Visa Classic", "6831982476737658", "6831 98** **** 7658")
])
def test_init(name, number, expected):
    payment = Payment(name, number)
    assert payment.name == name
    assert payment.number == expected


@pytest.mark.parametrize("string, expected_name, expected_number", [
    ("Счет 75106830613657916952", "Счет", "**6952"),
    ("Visa Classic 6831982476737658", "Visa Classic", "6831 98** **** 7658")
])
def test_init_from_str(string, expected_name, expected_number):
    payment = Payment.init_from_str(string)
    assert payment.name == expected_name
    assert payment.number == expected_number
