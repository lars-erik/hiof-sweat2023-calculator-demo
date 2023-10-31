import sys

from Aggregation import Aggregation
from ExpressionParser import ExpressionParser
from ExpressionReader import ExpressionReader
from Operators import Subtraction, Addition


class CalculatorProgram():

    def __init__(self, operator, parser):
        self.parser = parser
        self.operator = operator

    def read_transform_calculate_format(self):
        operations = self.parser.parse_operations()
        aggregation = Aggregation(operations, self.operator)
        aggregation.calculate()
        report = self.format_report(aggregation)
        return report

    def format_report(self, aggregation):
        report = ''
        for op in aggregation.operations:
            report += f"{op.left} {str(op.operator)} {op.right} = {op.calculate()}\n"
        report += 'Total: ' + str(aggregation.total)
        return report


if __name__ == "__main__":
    operator = (
        Subtraction() if len(sys.argv) > 1 and sys.argv[1] == 'sub'
        else
        Addition()
    )
    parser = ExpressionParser(ExpressionReader(), operator)
    program = CalculatorProgram(operator, parser)

    print(program.read_transform_calculate_format())
