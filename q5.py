# Question 5
# Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. The function definition should look like question5(ll, m), where ll is the first node of a linked list and m is the "mth number from the end". You should copy/paste the Node class below to use as a representation of a node in the linked list. Return the value of the node at that position.

# class Node(object):
#   def __init__(self, data):
#     self.data = data
#     self.next = None

def question5(ll, m):
    end_pointer = ll
    mid_pointer = ll
    for num in xrange(m):
        end_pointer = end_pointer.next  # Advance ll end tracker
    while end_pointer:  # Advance end pointer through complete ll
        end_pointer = end_pointer.next
        mid_pointer = mid_pointer.next
    return mid_pointer.data

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
    print 'Created LL with the vals 1=>2=>3=>4=>5'
    print 'TEST 1: Looking for 3rd value from end'
    print 'Result should be 3'
    print question5(root, 3)
    print 'TEST 2: Looking for 1st value from end'
    print 'Result should be 5'
    print question5(root, 1)
    print 'TEST 3: Looking for 5rd value from end'
    print 'Result should be 1'
    print question5(root, 5)

# Notes
#
# This second iteration of a linked list traversal algorithm
# utilizes two pointers to systematically advance through a
# linked list, such that the previous pointer will always
# come to rest at the mth node from the end.
#
# The algorithm starts by advancing a ll end tracker to node
# m-1 of the list. At this point, the distance between the end
# pointer and the mid pointer--which still resides at the root
# node-- is equivilant to the distance between the mth node
# and the end of the list, plus one. Both pointers then advance
# through the list until the end pointer is set to None (or,
# the end node plus one). The distance between the two pointers
# has been maintained, so the mid pointer is now residing at
# the mth node from the end of the list. Finally, the mid
# pointer's data is returned.
#
# This algorithm achieves time complexity of O(n), because it will
# always have to iterate through every element of the linked list
# in order to find the end. Notably, it achieves space complexity
# in constant time O(1) because only two variables are declared
# regardless of the size of the linked list.