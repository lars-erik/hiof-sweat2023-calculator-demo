from approvaltests import approvals

from Operators import Addition, Subtraction
from calculator import CalculatorProgram
from ExpressionReader import ExpressionReader
from ExpressionParser import ExpressionParser


def test_addition():
   parser = ExpressionParser(ExpressionReader(), Addition())
   report = CalculatorProgram(Addition(), parser).read_transform_calculate_format()
   approvals.verify(report)

def test_subtraction():
   parser = ExpressionParser(ExpressionReader(), Subtraction())
   report = CalculatorProgram(Subtraction(), parser).read_transform_calculate_format()
   approvals.verify(report)

