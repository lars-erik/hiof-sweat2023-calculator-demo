from approvaltests import approvals

from AsciiReporter import AsciiReporter
from Operators import Addition, Subtraction
from calculator import CalculatorProgram
from ExpressionReader import ExpressionReader
from ExpressionParser import ExpressionParser

reporter = AsciiReporter()

def test_addition():
   parser = ExpressionParser(ExpressionReader(), Addition())
   report = CalculatorProgram(Addition(), parser, reporter).read_transform_calculate_format()
   approvals.verify(report)

def test_subtraction():
   parser = ExpressionParser(ExpressionReader(), Subtraction())
   report = CalculatorProgram(Subtraction(), parser, reporter).read_transform_calculate_format()
   approvals.verify(report)

