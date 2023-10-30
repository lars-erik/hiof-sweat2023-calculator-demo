from approvaltests import approvals

from calculator import CalculatorProgram
from ExpressionReader import ExpressionReader
from ExpressionParser import ExpressionParser

parser = ExpressionParser(ExpressionReader())

def test_addition():
   report = CalculatorProgram(lambda x, y: x + y, '+', parser).read_transform_calculate_format()
   approvals.verify(report)

def test_subtraction():
   report = CalculatorProgram(lambda x, y: x - y, '-', parser).read_transform_calculate_format()
   approvals.verify(report)

