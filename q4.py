# Question 4
# Find the least common ancestor between two nodes on a binary search tree. The least common ancestor is the farthest node from the root that is an ancestor of both nodes. For example, the root is a common ancestor of all nodes on the tree, but if both nodes are descendents of the root's left child, then that left child might be the lowest common ancestor. You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties. The function definition should look like question4(T, r, n1, n2), where T is the tree represented as a matrix, where the index of the list is equal to the integer stored in that node and a 1 represents a child node, r is a non-negative integer representing the root, and n1 and n2 are non-negative integers representing the two nodes in no particular order. For example, one test case might be

# question4([[0, 1, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [1, 0, 0, 0, 1],
#            [0, 0, 0, 0, 0]],
#           3,
#           1,
#           4)
# and the answer would be 3.

def question4(matrix_tree, root, child1, child2):


    tree = BinaryTree(matrix_tree, root)
    # print tree.print_tree()
    # print tree.search(child1)
    # print tree.search(child2)
    ancestor = tree.find_ancestor(child1, child2)
    # print 'Found common ancestor: {}'.format(ancestor)
    return ancestor


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, matrix, root):
        self.root = self._add_node(matrix, root)

    def _add_node(self, matrix, idx):
        new_node = Node(idx)
        for chi_idx, child in enumerate(matrix[idx]):
            if child:  # True if child is 1
                if chi_idx < idx:
                    new_node.left = self._add_node(matrix, chi_idx)
                else:
                    new_node.right = self._add_node(matrix, chi_idx)
        return new_node

    def find_ancestor(self, num1, num2):
        ''' Finds search paths for both search nums and returns their
            common ancestor '''
        path1 = self.search(num1)
        path2 = self.search(num2)
        ancestor = None
        while path1 and path2:
            cur1 = path1.pop(0)
            cur2 = path2.pop(0)
            if cur1 == cur2:
                ancestor = cur1
        return ancestor



    def search(self, find_val):
        ''' Searches for param:num and returns traversal path as a string '''
        return self._search_node(self.root, find_val, [])

    def _search_node(self, node, val, traversal):
        traversal += [node.value]
        if node.value == val:
            return traversal
        if not node.left and not node.right:
            return None
        if val < node.value and node.left:
            return self._search_node(node.left, val, traversal)
        if val > node.value and node.right:
            return self._search_node(node.right, val, traversal)
        return None

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return self.preorder_print(self.root)

    def preorder_print(self, start):
        """Helper method - use this to create a
        recursive print solution."""
        printed = str(start.value)
        if not start.left and not start.right:
            printed = '({})'.format(start.value)
        if start.left:
            printed += '-' + self.preorder_print(start.left)
        if start.right:
            printed += '-' + self.preorder_print(start.right)
        return printed


if __name__ == '__main__':
    print 'Test 1: Testing BST with root as the least common ancestor (LST)'
    print 'Result should be 3'
    print question4([[0, 1, 0, 0, 0],
                     [0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0],
                     [1, 0, 0, 0, 1],
                     [0, 0, 0, 0, 0]],
                    3,
                    1,
                    4)
    print 'Test 2: Testing BST with LST to the right of root'
    print 'Result should be 5'
    print question4([[0, 1, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [1, 0, 0, 0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 1, 0, 1, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0]],
                    3,
                    4,
                    6)
    print 'Test 3: Testing BST with LST to the left of root'
    print 'Result should be 1'
    print question4([[0, 0, 0, 0, 0, 0, 0, 0],
                     [1, 0, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 1, 0, 0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 1, 0, 1, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0]],
                    3,
                    0,
                    1)

# Notes
#
# This algorithm translates a matrix representation of a binary tree
# to a binary tree, then uses depth-first searching to find two
# values within the tree. Should those values be found, internal
# methods read the DFS traversal paths until it finds the least
# common ancestor of both values.
#
# There are multiple operations that occur for each node in the
# binary tree (n), such as building the binary tree, and recursive
# DFS in the worst case. However, because worst case is aproximately
# O(3n), the aproximate time complexity is O(n).