class ExpressionParser():
    def __init__(self, reader):
        self.reader = reader

    def parse_operations(self):
        data = self.reader.read_data()
        lines = map(lambda l: l.split(','), data.split('\n'))
        operations = []
        for line in filter(lambda l: not l[0] == 'X', lines):
            operations.append({'x': (int(line[0])), 'y': (int(line[1]))})
        return operations
