import pytest
from src.Operation import Operation


@pytest.mark.parametrize("description, from_, to_,"
                         "expected_str, "
                         "expected_repr", [
    ("Перевод организации", "Visa Gold 3589276410671603", "Счет 96292138399386853355",
     "12.07.2019 Перевод организации\nVisa Gold 3589 27** **** 1603 -> Счет **3355\n2631.44 руб.",
     "description=Перевод организации, from=Visa Gold 3589 27** **** 1603, to=Счет **3355)"
     ),
    ("Перевод с карты на карту", "Visa Gold 3589276410671603", "Visa Gold 2289276410671622",
     "12.07.2019 Перевод с карты на карту\nVisa Gold 3589 27** **** 1603 -> Visa Gold 2289 27** **** 1622\n2631.44 руб.",
     "description=Перевод с карты на карту, from=Visa Gold 3589 27** **** 1603, to=Visa Gold 2289 27** **** 1622)"
     ),
    ("Открытие вклада", "Счет 96292138399386853355", None,
     "12.07.2019 Открытие вклада\nСчет **3355\n2631.44 руб.",
     "description=Открытие вклада, from=None, to=Счет **3355)"
     )
])
def test_init(description, from_, to_, expected_str, expected_repr):
    data = {
        "id": 633268359,
        "state": "EXECUTED",
        "date": "2019-07-12T08:11:47.735774",
        "operationAmount": {
            "amount": "2631.44",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": description,
        "from": from_,
        "to": to_
    }
    expected_repr = (f"Operation(id=633268359, "
                     f"state=EXECUTED, "
                     f"date=2019-07-12 08:11:47.735774, "
                     f"operationAmount=2631.44 руб., {expected_repr}")

    operation = Operation(*data.values())
    assert operation.__str__() == expected_str
    assert operation.__repr__() == expected_repr


def test_init_card_to_bank_account():
    data = {
        "id": 633268359,
        "state": "EXECUTED",
        "date": "2019-07-12T08:11:47.735774",
        "operationAmount": {
            "amount": "2631.44",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Gold 3589276410671603",
        "to": "Счет 96292138399386853355"
        }
    expected_str = ("12.07.2019 Перевод организации\n"
                    "Visa Gold 3589 27** **** 1603 -> Счет **3355\n"
                    "2631.44 руб.")
    expected_repr = (f"Operation(id=633268359, "
                     f"state=EXECUTED, "
                     f"date=2019-07-12 08:11:47.735774, "
                     f"operationAmount=2631.44 руб.,"
                     f"description=Перевод организации,"
                     f"from=Visa Gold 3589 27** **** 1603,"
                     f"to=Счет **3355)")

    operation = Operation(*data.values())
    assert operation.__str__() == expected_str
    assert operation.__repr__() == expected_repr


def test_init_card_to_card():
    data = {
        "id": 633268359,
        "state": "EXECUTED",
        "date": "2019-07-12T08:11:47.735774",
        "operationAmount": {
            "amount": "2631.44",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Gold 3589276410671603",
        "to": "Visa Gold 2289276410671622"
    }
    expected_str = ("12.07.2019 Перевод с карты на карту\n"
                    "Visa Gold 3589 27** **** 1603 -> Visa Gold 2289 27** **** 1622\n"
                    "2631.44 руб.")
    expected_repr = (f"Operation(id=633268359, "
                     f"state=EXECUTED, "
                     f"date=2019-07-12 08:11:47.735774, "
                     f"operationAmount=2631.44 руб.,"
                     f"description=Перевод с карты на карту,"
                     f"from=Visa Gold 3589 27** **** 1603,"
                     f"to=Visa Gold 2289 27** **** 1622)")

    operation = Operation(*data.values())
    assert operation.__str__() == expected_str
    assert operation.__repr__() == expected_repr


def test_init_open_bank_account():
    data = {
        "id": 633268359,
        "state": "EXECUTED",
        "date": "2019-07-12T08:11:47.735774",
        "operationAmount": {
            "amount": "2631.44",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 96292138399386853355"
    }

    expected_str = ("12.07.2019 Открытие вклада\n"
                    "Счет **3355\n"
                    "2631.44 руб.")
    expected_repr = (f"Operation(id=633268359, "
                     f"state=EXECUTED, "
                     f"date=2019-07-12 08:11:47.735774, "
                     f"operationAmount=2631.44 руб.,"
                     f"description=Открытие вклада,"
                     f"from=None,"
                     f"to=Счет **3355)")

    operation = Operation(*data.values())
    assert operation.__str__() == expected_str
    assert operation.__repr__() == expected_repr
