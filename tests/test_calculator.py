from approvaltests import approvals

from AsciiReporter import AsciiReporter
from Operators import Addition, Subtraction
from calculator import CalculatorProgram
from ExpressionReader import ExpressionReader
from ExpressionParser import ExpressionParser

reporter = AsciiReporter()

def test_addition():
   parser = ExpressionParser(ExpressionReader(), Addition())
   report = CalculatorProgram(Addition(), parser, reporter).execute()
   approvals.verify(report)

def test_subtraction():
   parser = ExpressionParser(ExpressionReader(), Subtraction())
   report = CalculatorProgram(Subtraction(), parser, reporter).execute()
   approvals.verify(report)

