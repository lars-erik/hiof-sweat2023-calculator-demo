import sys


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
            report += f"{op['x']} {self.format_operator()} {op['y']} = {op['subtotal']}\n"
        report += 'Total: ' + str(total)
        return report

    def format_operator(self): return '+'

    def calculate(self, operations):
        total = 0
        for op in operations:
            subtotal = self.calculate_operation(op['x'], op['y'])
            op['subtotal'] = subtotal
            total = self.calculate_operation(total, subtotal)
        return total

    def calculate_operation(self, x, y):
        return x + y

class SubtractionProgram(CalculatorProgram):
    def calculate_operation(self, x, y):
        return x - y

    def format_operator(self): return '-'


if __name__ == "__main__":
    program = (
        SubtractionProgram() if len(sys.argv) > 1 and sys.argv[1] == 'sub'
        else
        CalculatorProgram()
    )

    print(program.read_transform_calculate_format())




