import sys

from ExpressionParser import ExpressionParser
from ExpressionReader import ExpressionReader
from Operators import Subtraction, Addition


class CalculatorProgram():

    def __init__(self, operator, parser):
        self.parser = parser
        self.operator = operator

    def read_transform_calculate_format(self):
        operations = self.parser.parse_operations()
        total = self.calculate(operations)
        report = self.format_report(operations, total)
        return report

    def format_report(self, operations, total):
        report = ''
        for op in operations:
            report += f"{op.left} {str(op.operator)} {op.right} = {op.calculate()}\n"
        report += 'Total: ' + str(total)
        return report

    def calculate(self, operations):
        total = 0
        for op in operations:
            subtotal = op.calculate()
            total = self.operator.calculate(total, subtotal)
        return total



if __name__ == "__main__":
    operator = (
        Subtraction() if len(sys.argv) > 1 and sys.argv[1] == 'sub'
        else
        Addition()
    )
    parser = ExpressionParser(ExpressionReader(), operator)
    program = CalculatorProgram(operator, parser)

    print(program.read_transform_calculate_format())
