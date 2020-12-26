import unittest
from main_app import sumInts

class TestSum(unittest.TestCase):
   def test_sum(self):
      self.assertEqual(sumInts(1, 2, 3), 6);
      self.assertEqual(sumInts(1, 2), 3);

