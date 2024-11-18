from lab4.task13_1.src.main import Stack_Linked_List

import unittest

class TestStackLinkList(unittest.TestCase):

    def test_should_empty(self):
        # given
        stack = Stack_Linked_List()
        expected_result = True

        # when
        result = stack.is_Empty()

        # then
        self.assertEqual(result, expected_result)

    def test_should_with_elem(self):
        # given
        expected_result =  30
        stack = Stack_Linked_List()
        stack.push(10)
        stack.push(20)
        stack.push(30)

        # when
        result = stack.pop()

        # then
        self.assertEqual(result, expected_result)

    def test_should_not_empty(self):
        # given
        expected_result = False
        stack = Stack_Linked_List()
        stack.push(10)
        stack.push(20)
        stack.push(30)

        # when
        result = stack.is_Empty()

        # then
        self.assertEqual(result, expected_result)
if __name__ == '__main__':
    unittest.main()