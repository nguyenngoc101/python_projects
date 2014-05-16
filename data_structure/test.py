import unittest
from stack import Stack

class StackTestCase(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def tearDown(self):
        print "dang chay ham tearDown"
        self.stack = None

    def test_none_stack(self):

    def test_is_empty(self):
        pass

    def test_pop(self):
        pass

    def test_push(self):
        pass

    def test_size(self):
        pass
