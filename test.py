'''
test of the linked list for LL
'''

from linked_list import Node, LinkedList

node_a = Node(1)
node_b = Node(2)
node_c = Node(3)
node_d = Node(4)


ll = LinkedList()
print(ll)

ll.insert_at_end(node_a)
ll.insert_at_end(node_b)
ll.insert_at_end(node_c)
ll.insert_at_end(node_d)
print(ll) 

# test reverse() method
ll.reverse()
print(ll)
