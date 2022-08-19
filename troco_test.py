#coding:utf-8
import unittest
from troco import troco

class TestTroco(unittest.TestCase):
    def test_troco_1(self):
        self.assertEqual([1], troco(1))
        
unittest.main()
