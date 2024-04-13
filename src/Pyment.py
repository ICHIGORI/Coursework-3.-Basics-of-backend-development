class Payment:
    def __init__(self, name: str, number: str):
        self.name = name
        self.number = self.get_apply_hiding(number)

    @classmethod
    def init_from_str(cls, payment: str):
        *name, number = payment.split()
        return cls(' '.join(name), number)

    def __str__(self):
        return f"{self.name} {self.number}"

    def __repr__(self):
        return f"Payment(name={self.name}, number={self.number})"

    def get_apply_hiding(self, number):
        if self.name == "Счет":
            return f"**{number[-4:]}"
        else:
            return f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
