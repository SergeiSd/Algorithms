import math

def Dijkstra(graph, source, target):

    # dictionary for shortest distance between nodes
    shortest_distance = {}

    # list for shortest path between source and target node 
    way = [] 

    # the nodes which have not been visited yet
    unvisited_nodes = graph

    # list for predecessors of the nodes
    predecessor_nodes = {}
    
    for nodes in unvisited_nodes:
        # setting the shortest_distance of all the nodes as infinty
        shortest_distance[nodes] = math.inf
        
    # the distance of a point to itself is 0.
    shortest_distance[source] = 0
    
    # while all the nodes have been visited
    while(unvisited_nodes):
        
        min_Node = None
        
        for current_node in unvisited_nodes: 
            
            if min_Node is None:
                min_Node = current_node
                
            elif shortest_distance[min_Node] > shortest_distance[current_node]:
                min_Node = current_node
                
        # iterating through the connected nodes of current_node 
        for child_node, value in unvisited_nodes[min_Node].items():

            if value + shortest_distance[min_Node] < shortest_distance[child_node]:  
                # set the new value as the minimum distance of that connection
                shortest_distance[child_node] = value + shortest_distance[min_Node]
                # adding the current node as the predecessor of the child node
                predecessor_nodes[child_node] = min_Node
        
        unvisited_nodes.pop(min_Node)
        
    # set the current node as the target node 
    node = target
    
    while node != source:

        try:
            way.insert(0, node)
            node = predecessor_nodes[node]
        except Exception:
            print('\nPath not reachable.')
            break

    # including the source in the path
    way.insert(0,source)
    
    # if the node has been visited
    if shortest_distance[target] != math.inf:
        print('\nShortest distance = ' + str(shortest_distance[target]))
        print('\nThe path:')
        for point in way:
            if point == way[-1]:
                print(point)
            else:
                print(point + ' -> ', end='')


    print('\nThe shortest distance from source to every other node:\n')
    for key, value in shortest_distance.items(): 
        print('a ->', key, '=', value)

graph = {'a':{'b':5,'c':2},'b':{'c':1,'d':3},'c':{'b':3,'d':7},'d':{'e':7},'e':{'d':9}}

#Calling the function with source as 'a' and target as 'e'.
Dijkstra(graph, 'a', 'e')
# Our graph
#      B       7
#   5/ || \3 /--\
#  A  3||2  D    E
#   2\ || /7 \--/
#      C       9