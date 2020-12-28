class Node:
    
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
        
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
        
    def print_list(self):
        
        if self.head == None:
            return 0
        
        temp = self.head
        
        while temp:
            print(str(temp.data) + ' ', end='')
            temp = temp.next_node 
    
    
    def insert_to_list(self, data):
        
        if self.head == None:
            self.head = Node(data, None)
            return 0
        
        temp = self.head
        while temp.next_node:
            temp = temp.next_node
            
        temp.next_node = Node(data, None)
    
    
    def reverse_list(self, prev_node=None):
        
        current_node = self.head
        
        while current_node:
            
            next_node = current_node.next_node
            
            '''
            if prev_node == None:
                print('Prev node : None')
                print('Current node', current_node.data)
                print('Next node', next.data)
            elif next == None:
                print('Prev node', prev_node.data)
                print('Current node', current_node.data)
                print('Next node : None')
            else:
                print('Prev node', prev_node.data)
                print('Current node', current_node.data)
                print('Next node', next.data)
            '''
            
            current_node.next_node = prev_node
            prev_node = current_node
            current_node = next_node
            
        self.head = prev_node
        
    
obj = LinkedList()
obj.insert_to_list(5)
obj.insert_to_list(10)
obj.insert_to_list(15)
obj.insert_to_list(20)
obj.insert_to_list(25)


print('Linked List: ', end='')
obj.print_list()

obj.reverse_list()
print('\nReversed Linked List: ', end='')
obj.print_list()
