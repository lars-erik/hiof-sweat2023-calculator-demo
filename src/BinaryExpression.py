class BinaryExpression:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def calculate(self):
        return self.operator.calculate(self.left, self.right)