from approvaltests import approvals

from calculator import CalculatorProgram


def test_calculations():
   report = CalculatorProgram().read_transform_calculate_format()
   approvals.verify(report)

