from src.dto import get_operations_data
from src.utils import create_operations, sorted_operations_from_date


def main():
    data = get_operations_data()
    operations = create_operations(data)
    operations = sorted_operations_from_date(operations)
    display_executed = 5
    for operation in operations:
        if display_executed <= 0:
            break
        if operation.state == "EXECUTED":
            print(operation, '\n')
            display_executed -= 1


if __name__ == "__main__":
    main()
