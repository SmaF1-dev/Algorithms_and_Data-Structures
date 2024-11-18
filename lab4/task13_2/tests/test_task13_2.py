from lab4.task13_2.src.main import Queue_Linked_List

import unittest

class TestQueueLinkList(unittest.TestCase):

    def test_should_empty(self):
        # given
        stack = Queue_Linked_List()
        expected_result = True

        # when
        result = stack.is_Empty()

        # then
        self.assertEqual(result, expected_result)

    def test_should_with_elem(self):
        # given
        expected_result = 10
        stack = Queue_Linked_List()
        stack.enqueue(10)
        stack.enqueue(20)
        stack.enqueue(30)

        # when
        result = stack.dequeue()

        # then
        self.assertEqual(result, expected_result)

    def test_should_not_empty(self):
        # given
        expected_result = False
        stack = Queue_Linked_List()
        stack.enqueue(10)
        stack.enqueue(20)
        stack.enqueue(30)

        # when
        result = stack.is_Empty()

        # then
        self.assertEqual(result, expected_result)
if __name__ == '__main__':
    unittest.main()