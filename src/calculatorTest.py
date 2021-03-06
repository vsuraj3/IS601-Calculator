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
        test_data = CsvReader('/src/csv_files/addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
          
     def test_subtraction(self):
         test_data = CsvReader('/src/csv_files/subtraction.csv').data
         for row in test_data:
             self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
             self.assertEqual(self.calculator.result, int(row['Result']))

     def test_multiply_method(self):
         test_data = CsvReader('/src/csv_files/multiplication.csv').data
         for row in test_data:
             self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
             self.assertEqual(self.calculator.result, int(row['Result']))
            
      def test_divide_method(self):
          test_data = CsvReader('/src/csv_files/division.csv').data
          for row in test_data:
              self.assertEqual(self.calculator.div(row['Value 1'], row['Value 2']), int(row['Result']))
              self.assertEqual(self.calculator.result, int(row['Result']))
                
      def test_square_method(self):
          test_data = CsvReader('/src/csv_files/square.csv').data
          for row in test_data:
              self.assertEqual(self.calculator.square(row['Value 1'], row['Value 2']), int(row['Result']))
              self.assertEqual(self.calculator.result, int(row['Result']))
       
   
      def test_squareRoot_method(self):
          test_data = CsvReader('/src/csv_files/squareRoot.csv').data
          for row in test_data:
              self.assertEqual(self.calculator.squareroot(row['Value 1'], row['Value 2']), int(row['Result']))
              self.assertEqual(self.calculator.result, int(row['Result']))
            
if __name__ == '__main__':
    unittest.main()
