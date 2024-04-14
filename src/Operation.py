from src.Payment import Payment
from src.Amount import Amount
from datetime import datetime


class Operation:
    def __init__(self, id, state, date, operationAmount, description, from_=None, to_=None):
        self.id = id
        self.state = state
        self.date = datetime.fromisoformat(date)
        self.operationAmount = Amount.init_from_dict(operationAmount)
        self.description = description
        self.from_ = Payment.init_from_str(from_) if to_ else None
        self.to_ = Payment.init_from_str(to_) if to_ else Payment.init_from_str(from_)

    def __str__(self):
        return (f"{self.date.strftime("%d.%m.%Y")} {self.description}\n"
                f"{self.from_ if self.from_ else ''}{' -> 'if self.from_ else ''}{self.to_}\n"
                f"{self.operationAmount}")

    def __repr__(self):
        return (f"Operation(id={self.id}, "
                f"state={self.state}, "
                f"date={self.date}, "
                f"operationAmount={self.operationAmount}, "
                f"description={self.description}, "
                f"from={self.from_}, "
                f"to={self.to_})")
