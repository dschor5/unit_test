#import unittest
from main_app import sumInts

class TestSum:
   def test_sum(self):
      assert sumInts(1, 2, 3) == 6
      assert sumInts(1, 2) == 3
