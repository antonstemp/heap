import math

BASE = 2


class heap_node(object):
    MAX_CHILDREN = 2

    val = None
    parent = None
    children = None

    def __init__(self, val, parent=None):
        self.val = val
        self.parent = parent
        self.children = []

    def __gt__(self, other):
        return self.val > other.val

    def __lt__(self, other):
        return self.val < other.val

    def __str__(self):
        return 'V:{} P:{} C:{} '.format(
            self.val,
            None if not self.parent else self.parent.val,
            [child.val for child in self.children]
        )

    def add_child(self, child):
        if len(self.children) > self.MAX_CHILDREN:
            raise Exception('TooManyChildrenError')

        self.children.append(child)
        child.parent = self


class heapq(object):
    """
    Max heap
    """

    nodes = []

    @property
    def root(self):
        return self.nodes[0] if self.nodes else None

    def heap_print(self):
        """
        Prints the entire heap
        """
        cur = 0
        for i, node in enumerate(self.nodes):
            level = int(math.floor(math.log(i + 1, BASE)))
            if level > cur:
                cur = level
                print ''
            print '{} '.format(node),
        print '\n'

    def heappush(self, item):
        """
        Adds an element to the heap
        Olog(n)
        """

        new_node = heap_node(item)
        # Update the total list of nodes
        self.nodes.append(new_node)

        if self.root:
            # Locate the first node without 2 children
            node = self._find_empty()
            node.add_child(new_node)

            self._sift_down(new_node)

        return new_node

    def heappop(self):
        """
        Removes the largest element from the heap
        Olog(n)
        """
        top_val = self.root.val

        last_node = self._find_last()
        self._remove(last_node)

        self.root.val = last_node.val
        self._sift_up(self.root)

        return top_val

    def heapify(self, items):
        """
        Given a list of elements creates a heap
        Onlog(n)
        """

        # Create a list of nodes
        nodes = [heap_node(item) for item in items]
        self.nodes = nodes

        """
        Assigns parent-child relationship based on index number
        Ignore root node
        Index    | Parent index
        1        | none
        2 3      | 1
        4 5 6 7  | 2
        """
        for i, node in enumerate(nodes[1:], start=2):
            parent = self._calc_parent(i)
            parent.add_child(node)

        # Sort all the node_values
        non_leaf_nodes = len(self.nodes) // 2
        for node in reversed(self.nodes[:non_leaf_nodes]):
            self._sift_up(node)

    def heapdelete(self, node):
        self._swap(node, self.root)
        result = self.heappop()

        self._sift_up(node)
        self._sift_down(node)

        return result

    def size(self):
        return len(self.nodes)

    def _calc_parent(self, node_number):
        parent_index = (node_number // 2) - 1
        return self.nodes[parent_index]

    def _find_empty(self):
        """
        Finds the first node that has 0 or 1 children
        """

        index = len(self.nodes)
        return self._calc_parent(index)

    def _find_last(self):
        """
        Return the last node from the lowest level of the tree
        """

        return self.nodes[-1]

    def _swap(self, node1, node2):
        """
        Swaps the the values of two nodes
        """

        node1.val, node2.val = node2.val, node1.val

    def _sift_up(self, node):
        """
        For every non leaf node check that its children are not greater
        If they are swap parent with the largest child and continue until
        lowest level
        """

        while node.children:
            largest_child = max(node.children)
            if not largest_child > node:
                return

            # Swap values
            self._swap(node, largest_child)

            node = largest_child

    def _sift_down(self, node):
        while node.parent:
            if not node > node.parent:
                return

            self._swap(node, node.parent)
            node = node.parent

    def _remove(self, node):
        if node.children:
            raise Exception('cannot remove node with children')

        node.parent.children.remove(node)

        # Ensure O(1) when removing last node
        if node is self.nodes[-1]:
            self.nodes.heappop()
        else:
            # O(n) operation
            self.nodes.remove(node)


if __name__ == '__main__':
    h = heapq()
    h.heapify([1, 8, 7, 6, 5, 4, 3, 2, 1])
    h.heap_print()
    print 'heappushing'
    h.heappush(10)
    h.heap_print()
