from approvaltests import approvals

from calculator import CalculatorProgram, ExpressionParser


def test_addition():
   report = CalculatorProgram(lambda x, y: x + y, '+', ExpressionParser()).read_transform_calculate_format()
   approvals.verify(report)

def test_subtraction():
   report = CalculatorProgram(lambda x, y: x - y, '-', ExpressionParser()).read_transform_calculate_format()
   approvals.verify(report)

