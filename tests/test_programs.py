import importlib.util
import unittest
from pathlib import Path

PROGRAMS = Path(__file__).resolve().parents[1] / "programs"

def load(name):
    spec = importlib.util.spec_from_file_location(name, PROGRAMS / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

class PracticeTests(unittest.TestCase):
    def test_leap_years(self):
        fn = load("leap_year_checker").is_leap_year
        self.assertTrue(fn(2000))
        self.assertFalse(fn(1900))
        self.assertTrue(fn(2024))
        self.assertFalse(fn(2025))

    def test_quadratic(self):
        fn = load("quadratic_equation_solver").solve_quadratic
        self.assertEqual(fn(1, -3, 2)[1], (2.0, 1.0))
        self.assertEqual(fn(1, 2, 1)[1], (-1.0, -1.0))
        self.assertEqual(fn(1, 0, 1)[1], (1j, -1j))
        with self.assertRaises(ValueError):
            fn(0, 1, 1)

    def test_loan_boundaries(self):
        fn = load("loan_eligibility_checker").assess_loan
        self.assertIn("Gold", fn(21, 20000, 750))
        self.assertIn("Silver", fn(60, 20000, 650))
        self.assertIn("Not eligible", fn(20, 30000, 800))

    def test_scholarship_tiers(self):
        fn = load("scholarship_eligibility").scholarship_result
        self.assertIn("Full", fn(90, 200000))
        self.assertIn("75%", fn(80, 300000))
        self.assertIn("50%", fn(70, 400000))
        self.assertIn("Merit", fn(60, 500000))
        self.assertIn("Not eligible", fn(59, 0))

if __name__ == "__main__":
    unittest.main()
