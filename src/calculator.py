import sys

from ExpressionParser import ExpressionParser
from ExpressionReader import ExpressionReader


class CalculatorProgram():

    def __init__(self, calculate_operation, operator, parser):
        self.parser = parser
        self.calculate_operation = calculate_operation
        self.operator = operator

    def read_transform_calculate_format(self):
        operations = self.parser.parse_operations()
        total = self.calculate(operations)
        report = self.format_report(operations, total)
        return report

    def format_report(self, operations, total):
        report = ''
        for op in operations:
            report += f"{op['x']} {self.operator} {op['y']} = {op['subtotal']}\n"
        report += 'Total: ' + str(total)
        return report

    def calculate(self, operations):
        total = 0
        for op in operations:
            subtotal = self.calculate_operation(op['x'], op['y'])
            op['subtotal'] = subtotal
            total = self.calculate_operation(total, subtotal)
        return total



if __name__ == "__main__":
    parser = ExpressionParser(ExpressionReader())
    program = (
        CalculatorProgram(lambda x, y: x - y, '-', parser) if len(sys.argv) > 1 and sys.argv[1] == 'sub'
        else
        CalculatorProgram(lambda x, y: x + y, '+', parser)
    )

    print(program.read_transform_calculate_format())
