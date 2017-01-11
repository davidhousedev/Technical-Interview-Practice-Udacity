# Question 5
# Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. The function definition should look like question5(ll, m), where ll is the first node of a linked list and m is the "mth number from the end". You should copy/paste the Node class below to use as a representation of a node in the linked list. Return the value of the node at that position.

# class Node(object):
#   def __init__(self, data):
#     self.data = data
#     self.next = None

def question5(ll, m):
    cur = ll
    prev = None
    while cur:  # Advance cursor through complete ll
        cur.prev = prev  # For each node, add a pointer to the previous node
        prev = cur
        cur = cur.next
    for num in xrange(m - 1):
        prev = prev.prev  # Return through previous nodes until m is reached
    return prev.data

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None


if __name__ == '__main__':
    # Build a linked list for testing
    # Size: 5 nodes, find the 3rd node from the end
    root = Node(1)
    current_node = root
    for num in xrange(4):
        new_node = Node(num + 2)
        current_node.next = new_node
        current_node = new_node
    print 'Created LL'
    question5(root, 3)

# Notes
#
# This algorithm returns the data at a linked list node that is mth number
# from the end. It achieves this by iterating through every item of a
# linked list, and inserting pointers to the previous items of the list
# until it reaches the end, effectively transforming a singly-linked list to
# a doubly-linked list. From the final node, it traverses back through the
# list until it finds the desired node.
#
# This algorithm runs with a worst case time complexity of O(2n), in the case
# where the user's prompt returns data from the linked list's root node.
# However, this worst case is aproximated to O(n) where n is the number of
# items in the linked list. Notably, this algorithm achieves O(n) without
# implementing any additional data structures, achiving space complexity in
# constant time O(1).