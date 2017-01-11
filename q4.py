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

    tree = TreelessBST(matrix_tree, root)
    ancestor = tree.find_ancestor(child1, child2)
    return ancestor


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreelessBST(object):
    def __init__(self, matrix, root):
        self.root = root
        self.matrix = matrix

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

    def search(self, value):
        traversal = []
        return self._search_node(self.root, value, traversal)

    def _search_node(self, node_idx, value, traversal):
        traversal += [node_idx]
        print traversal
        if node_idx == value:
            return traversal
        if value < node_idx:
            left = self._get_left_path(self.matrix[node_idx])
            print 'continuing search with left index: {}'.format(left)
            if type(left) == int:  # Ensure index exists
                return self._search_node(left, value, traversal)
        if value > node_idx:
            right = self._get_right_path(self.matrix[node_idx])
            print 'continuing search with right index: {}'.format(right)
            if type(right) == int:  # Ensure index exists
                return self._search_node(right, value, traversal)

    def _get_left_path(self, node):
        ''' Get the index of the first 1 in node, searching from the left '''
        # Utilize try/except to avoid value error if no 1 is found
        try:
            idx = node.index(1)
            return idx
        except:
            return None

    def _get_right_path(self, node):
        ''' Get the index of the first 1 in node, searching from the right '''
        # Utilize try/except to avoid value error if no 1 is found
        try:
            idx = (len(node) - 1) - node[::-1].index(1)
            return idx
        except:
            return None


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
# This algorithm reads a matrix representation of a binary search
# tree (BST) to determine the lowest common ancestor (LST) of two
# points. The logic relies on a recursive depth first search method
# which returns the traversal path between root and the specified
# value. Once the traversal paths of both query values have been found,
# values from both traversals are extracted until the first common
# value is found, which will be the LST.
#
# This algorithm achieves low time complexity and space complexity
# by reading the BST matrix in-place. Time complexity is limited by
# the utilization of depth first search, which evaluates to
# O(n log n). Space complexity is kept low, with an average of
# O(n), where n is