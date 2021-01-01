import unittest
from unit_test.main_app import sumInts

class TestSum(unittest.TestCase):
   """Test class for main file."""
   def test_sum(self):
      """Test sum function"""
      self.assertEqual(sumInts(1, 2, 3), 6);
      self.assertEqual(sumInts(1, 2), 3);

