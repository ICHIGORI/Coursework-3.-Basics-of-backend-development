from src.dto import get_operations_data
from src.Operation import Operation
from datetime import datetime


def create_operations(operations_data: list[dict]) -> list[Operation]:
    """Создаёт список объектов Operation из данных json файла"""
    operations_obj = []
    operations = operations_data
    for operation in operations:
        if not operation:
            continue
        operations_obj.append(Operation(*operation.values()))
    return operations_obj


def sorted_operations_from_date(operations: list) -> list:
    """Сортирует объекты по дате"""
    return sorted(operations, key=lambda x: datetime.strftime(x.date, "%Y-%m-%d %H:%M:%S"), reverse=True)


if __name__ == "__main__":
    print(*sorted_operations_from_date(create_operations(get_operations_data()))[:5], sep='\n\n')
