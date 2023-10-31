class Aggregation:
    def __init__(self, operations, operator):
        self.operations = operations
        self.operator = operator
        self.total = None

    def calculate(self):
        self.total = 0
        for op in self.operations:
            subtotal = op.calculate()
            self.total = self.operator.calculate(self.total, subtotal)
        return self.total