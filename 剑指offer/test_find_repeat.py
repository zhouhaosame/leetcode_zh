from unittest import TestCase
from find_repeat_char_3 import find_repeat

class TestFind_repeat(TestCase):
    def test_find_first_unique_char(self):
        test=find_repeat([1, 1, 1, 2, 2, 3, 4, 4, 5, 6, 7])
        result1_1=test.find_arbitrary_repeat_char()
        result1_2=test.find_first_unique_char()
        print(result1_1)
        print(result1_2)
        test=find_repeat([])
        result1_1=test.find_arbitrary_repeat_char()
        result1_2=test.find_first_unique_char()
        print(result1_1)
        print(result1_2)
        test=find_repeat([0,1,2,3,4,5,6])
        result1_1=test.find_arbitrary_repeat_char()
        result1_2=test.find_first_unique_char()
        print(result1_1)
        print(result1_2)
        test=find_repeat([1,2,3,4,5,5,6])
        result1_1=test.find_arbitrary_repeat_char_without_modifing()
        print(result1_1)
        test=find_repeat([1,2,3,4,5,5,6,6,6,6])
        result1_1=test.find_arbitrary_repeat_char_without_modifing()
        print(result1_1)
        test=find_repeat([1,2,2,3,4,5,6,7])
        result1_1=test.find_arbitrary_repeat_char_without_modifing()
        print(result1_1)
        return
        self.fail()

