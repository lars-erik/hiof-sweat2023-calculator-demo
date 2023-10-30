from BinaryExpression import BinaryExpression


class ExpressionParser():
    def __init__(self, reader, operator):
        self.reader = reader
        self.operator = operator

    def parse_operations(self):
        data = self.reader.read_data()
        lines = map(lambda l: l.split(','), data.split('\n'))
        operations = []
        for line in filter(lambda l: not l[0] == 'X', lines):
            operations.append(
                BinaryExpression(int(line[0]), self.operator, int(line[1]))
            )
        return operations
