""""
Given the head node of a doubly linked list of naija artists,
reverse the order of the nodes in place.
Algorithm:
switch the next and prev pointers of the nodes so
that the direction of the list is reversed.
Return a reference to the head node of the reversed list.
"""

class Node:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.prev = None

    def __str__(self):
        artists = []
        while self:
            artists.append(f'{self.name} <---->')
            self = self.next

        artists.append('None')
        return ''.join(artists)

asake = Node('ASAKE')
burna_boy = Node('BURNA BOY')
wizkid = Node('WIZKID')
davido = Node('DAVIDO')
fireboy = Node('FIRE BOY')

asake.next = burna_boy
burna_boy.prev = asake
burna_boy.next = wizkid
wizkid.prev = burna_boy
wizkid.next = davido
davido.prev = wizkid
davido.next = fireboy
fireboy.prev = davido

print(f'LINKED LIST: {asake}')


def reverseDoublyLinkedList(head):
    previousNode = None
    currentNode = head

    while currentNode:
        nextNode = currentNode.next
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = nextNode

    return previousNode

head = reverseDoublyLinkedList(asake)
print(head)
