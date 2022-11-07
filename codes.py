'''
Our goal is to reverse a linked list with the names of Naija Artists
'''

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


def reverseLinkedList(head):
    current_node = head
    previous_node = None

    while current_node:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node

    return previous_node

new_head = reverseLinkedList(asake)
print(f'REVERSED LINKED LIST: {new_head}')




