class Amount:
    def __init__(self, value, name, code):
        self.value = value
        self.name = name
        self.code = code

    @classmethod
    def init_from_dict(cls, amount: dict):
        return cls(float(amount["amount"]), amount["currency"]["name"], amount["currency"]["code"])

    def __str__(self):
        return f"{self.value} {self.name}"

    def __repr__(self):
        return f"Amount(value={self.value}, name={self.name}, code={self.code})"
