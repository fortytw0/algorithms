from email import header


class Node(object) : 

    def __init__(self , head = None, next = None) -> None:
        self.head = head
        self.next = next

def reverse_linked_list(curr_node) : 


    if curr_node.next != None : 
        reverse_linked_list(curr_node.next)

    else : 
        curr_node.next = curr_node.head
        curr_node.head = curr_node.next

prev_node = None
next_node = None
head_node = None

for i in range(4) : 
    
    if prev_node == None : 
        node = Node(None, None)
        prev_node , head_node = node , node

    else : 
        node = Node(prev_node , None)
        prev_node.next = node
        prev_node = node


curr_node = head_node

while curr_node != None : 
    print(curr_node)
    curr_node = curr_node.next


reverse_linked_list(head_node)

curr_node = head_node
while curr_node != None : 
    print(curr_node)
    curr_node = curr_node.next