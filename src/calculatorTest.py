import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator=Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method(self):
        self.assertEqual(self.calculator.add(2,2),4)
        self.assertEqual(self.calculator.result,4)

    def test_subtract_method(self):
        test_data = CsvReader('/src/csv_files/subtraction.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

if __name__ == '__main__':
    unittest.main()