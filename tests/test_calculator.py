from approvaltests import approvals

from calculator import read_transform_calculate_format


def test_calculations():
   report = read_transform_calculate_format()
   approvals.verify(report)

