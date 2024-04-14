import json
import os
from pathlib import Path
from datetime import datetime
from src.utils import sorted_operations_from_date, create_operations


def test_sorted_operations_from_date():
    class __Operation:
        def __init__(self, date):
            self.date = datetime.fromisoformat(date)

        def __str__(self):
            return f"{self.date}"

    data = [__Operation("2019-12-03 04:27:03.427014"),
            __Operation("2019-11-19 09:22:25.899614"),
            __Operation("2019-12-08 22:46:21.935582"),
            __Operation("2019-12-07 06:17:14.634890")]
    expected = ["2019-12-08 22:46:21.935582",
                "2019-12-07 06:17:14.634890",
                "2019-12-03 04:27:03.427014",
                "2019-11-19 09:22:25.899614"]
    for i in range(len(expected)):
        assert sorted_operations_from_date(data)[i].__str__() == expected[i]


def test_create_operations():
    path_data = os.path.join(Path(__file__).parent.parent, f"tests/utils_data.json")
    path_expected = os.path.join(Path(__file__).parent.parent, f"tests/utils_data_expected.txt")

    with open(path_data, encoding="utf-8") as file:
        data = json.load(file)
    with open(path_expected, encoding="utf-8") as file:
        expected = file.readlines()

    operations = create_operations(data)
    for i, expected_line in enumerate(expected):
        assert operations[i].__repr__() == expected_line.rstrip()
