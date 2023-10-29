from approvaltests import approvals

from calculator import CalculatorProgram, SubtractionProgram


def test_addition():
   report = CalculatorProgram().read_transform_calculate_format()
   approvals.verify(report)

def test_subtraction():
   report = SubtractionProgram().read_transform_calculate_format()
   approvals.verify(report)

