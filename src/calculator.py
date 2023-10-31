import sys

from Aggregation import Aggregation
from AsciiReporter import AsciiReporter
from ExpressionParser import ExpressionParser
from ExpressionReader import ExpressionReader
from Operators import Subtraction, Addition


class CalculatorProgram():

    def __init__(self, operator, parser, reporter):
        self.parser = parser
        self.operator = operator
        self.reporter = reporter

    def execute(self):
        operations = self.parser.parse_operations()
        aggregation = Aggregation(operations, self.operator)
        aggregation.calculate()
        report = self.reporter.format_report(aggregation)
        return report


if __name__ == "__main__":
    operator = (
        Subtraction() if len(sys.argv) > 1 and sys.argv[1] == 'sub'
        else
        Addition()
    )
    parser = ExpressionParser(ExpressionReader(), operator)
    program = CalculatorProgram(operator, parser, AsciiReporter())

    print(program.execute())
