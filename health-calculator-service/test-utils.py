import unittest
from health_utils import calculate_bmi, calculate_bmr

class TestUtils(unittest.TestCase):
  def test_calculate_bmi(self):
    self.assertAlmostEqual(calculate_bmi(1.75, 70), 22.86, places=2)
  def test_calculate_bmi_cm(self):
    self.assertEqual(calculate_bmi(175, 70), 0)
  def test_calculate_bmi_wrong(self):
    self.assertEqual(calculate_bmi(0, 70), 0)
  def test_calculate_bmr_f(self):
    self.assertEqual(calculate_bmr(175, 70, 30, 'F'), 1766.93)
  def test_calculate_bmr_m(self):
    self.assertEqual(calculate_bmr(175, 70, 30, 'M'), 2036.29)
  def test_calculate_bmr_wrong(self):
    self.assertEqual(calculate_bmr(175, 70, 30, 'X'), 0)

if __name__ == "__main__":
    unittest.main()