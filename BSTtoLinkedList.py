# Node class for representing a tree node
class Node:
    
    # Constructor 
    def __init__(self, data): 
        self.data = data 
        self.left_node = None
        self.right_node = None


# Function to make current node right of the last node in the list 
def FlattenBinaryTree(root): 
  
    # A variable for the last node that was added to the linked list 
    global last_node 

    if(root == None): 
        return
      
    left_node = root.left_node 
    right_node = root.right_node 
  
    # Avoid first iteration where root is the only node in the list 
    if(root != last_node): 
        last_node.right_node = root 
        last_node.left_node = None
        last_node = root 

    FlattenBinaryTree(left_node) 
    FlattenBinaryTree(right_node) 
    
    if(left_node == None and right_node == None): 
        last_node = root 

# A function to print the inorder traversal of the tree 
def PrintInorderBST(root):
    
    if(root == None): 
        return
    
    PrintInorderBST(root.left_node) 
    print(str(root.data), end = " ") 
    PrintInorderBST(root.right_node) 

# Build the our tree 
'''
          1
        /   \
       2     5
      / \   / \
     3   4 6   7

'''
root = Node(1) 
root.left_node = Node(2) 
root.left_node.left_node = Node(3) 
root.left_node.right_node = Node(4) 
root.right_node = Node(5)
root.right_node.left_node = Node(6)
root.right_node.right_node = Node(7) 
  
# Print the inorder traversal of the original tree 
print("Original inorder traversal = ", end = '') 
PrintInorderBST(root) 
print('') 
  
# A variable for the last node that was added to the linked list 
last_node = root 
  
# Flatten the binary tree, at the beginning root node is the only node in the list 
FlattenBinaryTree(root) 
  
# Print the inorder traversal of the flattened binary tree 
print("Flattened inorder traversal = ", end = '') 
PrintInorderBST(root) 
