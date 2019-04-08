from unittest import TestCase
from test import test1

class TestTest1(TestCase):
    def test_sum_new(self):
        t=test1(5,6)
        print(t.sum_new())
        return
        self.fail()
