
# Linked List Node 
class Node: 

    # Class constructor
    def __init__(self, data): 
        self.data = data 
        self.next_node = None
  
  
# Create and handle list operations 
class LinkedList: 

    # Class constructor
    def __init__(self): 
        self.head_node = None
  
    # Method to display the list 
    def printList(self): 

        temp = self.head_node 
        
        while temp: 
            print(temp.data, end=" ") 
            temp = temp.next_node
  
    # Method to add element to list 
    def addToList(self, newData): 

        new_Node = Node(newData) 
        if self.head_node is None: 
            self.head_node = new_Node 
            return
  
        last = self.head_node 
        while last.next_node: 
            last = last.next_node
  
        last.next_node = new_Node 
  
  

def mergeTwoLists(firstHead, secondHead): 
    '''
    Function to merge the lists 
    Takes two lists which are sorted joins them to get a single sorted list 
    '''

    # A dummy node to store the result 
    dummy_node = Node(0) 
  
    # Tail stores the last node 
    tail_node = dummy_node 

    while True: 
  
        # If any of the list gets completely empty directly join all the elements of the other list 
        if firstHead is None: 
            tail_node.next_node = secondHead 
            break

        if secondHead is None: 
            tail_node.next_node = firstHead 
            break
  
        # Compare the data of the lists and whichever is smaller is appended to the last of the merged list and the head is changed 
        if firstHead.data <= secondHead.data: 
            tail_node.next_node = firstHead 
            firstHead = firstHead.next_node

        else: 
            tail_node.next_node = secondHead 
            secondHead = secondHead.next_node
  
        # Advance the tail 
        tail_node = tail_node.next_node
  
    # Returns the head of the merged list 
    return dummy_node.next_node
  
  
# Create 2 lists 
firstList = LinkedList() 
secondList = LinkedList() 
  
# Add elements to the list in sorted order in first and second list
firstList.addToList(5) 
firstList.addToList(8) 
firstList.addToList(17) 
firstList.addToList(35)

secondList.addToList(1) 
secondList.addToList(12) 
secondList.addToList(20) 
secondList.addToList(26)

# Call the merge function 
firstList.head_node = mergeTwoLists(firstList.head_node, secondList.head_node) 
  
# Display merged list 
print("Merged Linked List = ", end='') 
secondList.printList() 