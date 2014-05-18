import unittest
from stack import Stack, EmptyException

class StackTestCase(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def tearDown(self):
        self.stack = None

    def test_none_stack(self):
        self.assertIsNotNone(self.stack)

    def test_is_empty(self):
        # Check Stack is empty when initializing
        self.assertEqual(self.stack.size(), 0)
        # push one and get one
        self.stack.push(1)
        self.stack.pop()
        self.assertEqual(self.stack.size(), 0)

    def test_pop(self):
        # Throw EmptyException when size = 0
        with self.assertRaises(EmptyException):
            self.stack.pop()
        # check return correct value
        self.stack.push(1)
        self.assertEqual(self.stack.pop(),1)
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(),2)

    def test_push(self):
        self.stack.push(None)
        self.assertEqual(self.stack.size(), 1)
        self.assertEqual(self.stack.pop(), None)
        self.assertEqual(self.stack.size(), 0)

    def test_size(self):
        self.assertEqual(self.stack.size(), 0)
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.size(), 3)
        self.stack.pop()
        self.assertEqual(self.stack.size(), 2)
        self.stack.pop()
        self.stack.pop()
        self.assertEqual(self.stack.size(), 0)
