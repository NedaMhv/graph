# We need to create a dictionary for the illustrated graph.
graph = {
  '0' : ['1','2'],
  '1' : ['2', '4'],
  '2' : ['3'],
  '3' : ['4'],
  '4' : [],
}
# Then we create an empty List to save the visited nodes and track the visited nodes.

visited = []

# Creating an empty list for Keeping track of the current nodes in the queue

queue = []  

# function for BFS( The arguments for this function are: the graph, visited nodes and the starting node.
   
def bfs(visited, graph, node): 
  visited.append(node)
  queue.append(node)
# Creating loop to visit each node
  while queue:          
    m = queue.pop(0)
    print (m, end = " ")

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print("The Breadth-First Search is as follow")
bfs(visited, graph, '0')    # function calling


