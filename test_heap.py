import unittest
import heap

SORTED_HEAP = [3, 2, 1]
MAX = 999
MIN = -999
BASIC_HEAP = [MIN, 2, MAX]


class TestHeapq(unittest.TestCase):
    def setUp(self):
        self.h = heap.heapq()
        self.h.heapify(BASIC_HEAP)

    def test_root(self):
        self.assertEqual(self.h.root.val, MAX)

    def test_heapify(self):
        self.assertEqual(len(BASIC_HEAP), len(self.h.nodes))
        for node in self.h.nodes:
            if node.parent:
                self.assertLess(node, node.parent)

            for child in node.children:
                self.assertGreater(node, child)


if __name__ == '__main__':
    unittest.main()
