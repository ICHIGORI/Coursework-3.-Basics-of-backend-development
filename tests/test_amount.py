import pytest
from src.Amount import Amount


@pytest.mark.parametrize("value, name, code, expected_str, expected_repr", [
    ("45849.53", "USD", "USD", "45849.53 USD", "Amount(value=45849.53, name=USD, code=USD)"),
    ("26311.40", "руб.", "RUB", "26311.40 руб.", "Amount(value=26311.40, name=руб., code=RUB)"),
])
def test_init(value, name, code, expected_str, expected_repr):
    amount = Amount(value, name, code)
    assert amount.__str__() == expected_str
    assert amount.__repr__() == expected_repr


def test_init_from_dict():
    data_init = {
        "amount": "2631.44",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }}
    amount = Amount.init_from_dict(data_init)
    assert amount.__str__() == "2631.44 руб."
    assert amount.__repr__() == "Amount(value=2631.44, name=руб., code=RUB)"
