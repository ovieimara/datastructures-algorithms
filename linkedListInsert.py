"""
Given the pointer to the head node of a linked list
of naija artists and an artist to insert at a
certain position, insert this node at the
desired position and return the head node.

Algorithm:
1. iterate through the node from the head,
   keeping track of current position.
2. If current position equals zero, create new node
   assign the next pointer of the new node to the head
   and the head to the new node. Then exit
3. If the desired position is the current position - 1,
   create new node, assign the next pointer of new node
   to the next node not at position, and assign the current
   Node next pointer to the new Node. Take note of the
   order of the assignment, so as not to cut the next node.
   Therefore, new node assignment must come first. Then exit.

4. return head
"""

class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

    def __str__(self):
        artists = []
        while self:
            artists.append(f'{self.name} ---->')
            self = self.next
        artists.append('None')

        return ''.join(artists)

asake = Node('ASAKE')
burna_boy = Node('BURNA BOY')
wizkid = Node('WIZKID')
davido = Node('DAVIDO')
fireboy = Node('FIRE BOY')

asake.next = burna_boy
burna_boy.next = wizkid
wizkid.next = davido
davido.next = fireboy

print(f'LINKED LIST: {asake}')

def insertNode(head, data, position):
    currentNode = head
    currentPosition = 0
    newNode = Node(data)

    while currentNode:
        nextNode = currentNode.next

        if position == 0:
            newNode.next = head
            head = newNode
            break

        if currentPosition == position - 1:
            newNode.next = nextNode
            currentNode.next = newNode
            break

        currentNode = nextNode
        currentPosition += 1

    return head

head = insertNode(asake, 'AYRA STARR', 1)
print(head)
