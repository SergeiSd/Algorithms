class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


head = Node(10, Node(20, Node(30, Node(40))))


def print_list(head, end='\n'):
    while head:
        print(head.data, end=' -> ' if head.next else '')
        head = head.next
    print(end=end)

print('LinkedList: ', end='')
print_list(head)


def reverse_list(head, tail=None):
    while head:
        head.next, tail, head = tail, head, head.next
    return tail

print('Reversed LinkedList: ', end='')
print_list(reverse_list(head))