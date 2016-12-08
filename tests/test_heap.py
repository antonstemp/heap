import unittest
from heap import heap

SORTED_HEAP = [3, 2, 1]
MAX = 999
MIN = -999
BASIC_HEAP = [MIN, 2, MAX]


class TestHeapq(unittest.TestCase):
    def setUp(self):
        self.h = heap.heapq()
        self.h.heapify(BASIC_HEAP)
        self.n1 = heap.heap_node(MIN)
        self.n2 = heap.heap_node(MAX)

    def test_root(self):
        self.assertEqual(self.h.root.val, MAX)

    def test_heapify(self):
        self.assertEqual(len(BASIC_HEAP), len(self.h.nodes))
        for node in self.h.nodes:
            if node.parent:
                self.assertLess(node, node.parent)

            for child in node.children:
                self.assertGreater(node, child)

    def test_node(self):
        self.assertEqual(self.n1.val, MIN)

    def test_node_add_child(self):
        self.n2.add_child(self.n1)

        # Children set correctly
        self.assertIn(self.n1, self.n2.children)
        self.assertEqual(len(self.n2.children), 1)

        # Parent set correctly
        self.assertEqual(self.n1.parent, self.n2)

    def test_node_lt(self):
        self.assertLess(self.n1, self.n2)

    def test_node_gt(self):
        self.assertGreater(self.n2, self.n1)


if __name__ == '__main__':
    unittest.main()
