class CalculatorProgram:
    def read_transform_calculate_format(self):
        data = self.read_data()
        operations = self.parse_operations(data)
        total = self.calculate(operations)
        report = self.format_report(operations, total)
        return report


    def read_data(self):
        data = open('./../data/calculations.csv').read()
        return data


    def parse_operations(self, data):
        lines = map(lambda l: l.split(','), data.split('\n'))
        operations = []
        for line in filter(lambda l: not l[0] == 'X', lines):
            operations.append({'x': (int(line[0])), 'y': (int(line[1]))})
        return operations


    def format_report(self, operations, total):
        report = ''
        for op in operations:
            report += f"{op['x']} + {op['y']} = {op['subtotal']}\n"
        report += 'Total: ' + str(total)
        return report


    def calculate(self, operations):
        total = 0
        for op in operations:
            subtotal = op['x'] + op['y']
            op['subtotal'] = subtotal
            total += subtotal
        return total


if __name__ == "__main__":
    print(CalculatorProgram().read_transform_calculate_format())




