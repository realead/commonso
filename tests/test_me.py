import unittest

import commonso.setter as setter
import commonso.getter as getter

class SetGetTester(unittest.TestCase): 

   def test_setget_same(self):
      setter.set_value(42)
      val = setter.get_value()
      self.assertEqual(val, 42)

   def test_setget_different(self):
      setter.set_value(42)
      val = getter.get_value()
      self.assertEqual(val, 42)

