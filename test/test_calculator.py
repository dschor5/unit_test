import unittest
from source.calculator import Calculator

class TestSum(unittest.TestCase):
   """Test class for main file."""

   @classmethod
   def setUpClass(cls):
      cls.__calc = Calculator()

   def test_addition(self):
      """Test addition function"""
      self.assertEqual(self.__calc.addition(1, 2), 3)
      self.assertAlmostEqual(self.__calc.addition(1.5, 0.5), 2.0)
      self.assertRaises(ValueError, self.__calc.addition, "a", "b")
      

   def test_subtraction(self):
      """Test subtraction function"""
      self.assertEqual(self.__calc.subtraction(1, 2), -1)
      self.assertEqual(self.__calc.subtraction(2, 1), 1)
      self.assertRaises(TypeError, self.__calc.subtraction, "a", "b")

      
   @classmethod
   def tearDownClass(cls):
      cls.__calc = None
      
     
