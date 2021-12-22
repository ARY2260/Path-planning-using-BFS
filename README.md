# Path-planning-using-BFS

### What is the Application?

Our application for the project is a path planning algorithm. 
The path planning problem is one of the most interesting and researched topics.
Path planning is a non-deterministic polynomial-time ("NP") hard problem with the task of finding a continuous path that connects the system from the first to the last goal. The complexity of the problem increases with increasing degrees of system freedom. The path to be followed will be de determined based on obstacles and situations, for example, consider the shortest route between the final points, or a short time to travel without a collision, etc.
These algorithms are commonly used in applications, such as Google Maps and other traffic routing systems. A more advanced version of this algorithm is getting used in autonomous driving vehicles. 
In our project, we will implement a path planning algorithm on a grid cell. And will find the shortest path for our object to move from S to E without any collisions.

### What is a Possible Solution?

One possible solution to the pathfinding problem is to use the Breadth-First-Search or in short BFS algorithm to find the shortest possible path. The way to use is to create a grid in the area which contains the start the end and all the obstacles. Apply the BFS algorithm on the cells of this grid starting from the cell which contains the start point and then moving progressively toward the cell that contains the endpoint. The BFS algorithm is used here to select which cell to move and to finally visualize a path This created area is called GRAPH in computational terms. BFS is a method of traversing trees (another type of data structure) which can also be applied to graphs as they are similar to graphs with the only difference that we can have level order connections in graphs. 
<br>
<br>
BFS Algorithm-
<br>
Breadth-first search (BFS) is an algorithm that is used to graph data or search tree or traverse structures. Let us understand the working of the algorithm with an example
In the various levels of the data, you can mark any node as the starting or initial node to begin traversing. The BFS will visit the node and mark it as visited and places it in the queue. Now the BFS will visit the nearest and un-visited nodes and mark them. These values are also added to the queue.

* Step -1 Each vertex or node in the graph is known. For instance, you can mark the node as V 
* Step -2 In case the vertex V is not accessed then add the vertex V into the BFS Queue
* Step -3 Start the BFS search, and after completion, Mark vertex V as visited.
* Step -4 The BFS queue is still not empty, hence remove the vertex V of the graph from the queue.
* Step -5 Retrieve all the remaining vertices on the graph that are adjacent to the vertex V
* Step -6 For each adjacent vertex let’s say V1, in case it is not visited yet then add V1 to the BFS queue
* Step -7 BFS will visit V1 and mark it as visited and delete it from the queue.
* Step -8 Move to the next vertex and repeat the process 
<br>
### Which Data Structure to Use for the Solution (Details of the Data Structure)
We will be using GRAPH for the solution.  
Graphs have a wide range of applications in our world. Graphs are used to model paths in a city, as often seen in Google Maps. They are used to model social networks such as Facebook or LinkedIn. Graphs are also used to monitor website backlinks, internal employee networks, etc. 
A graph is an image that represents a set of objects to which other pairs of objects are linked. Connecting objects are represented by points called vertices or nodes, and connecting connectors with vertices are called edges. A Graph is a non-linear data structure that can be represented using an array of vertices and a two-dimensional array of edges. We will also use GRID for implementing our algorithm. Grids are important data structures to represent geometric structures or their subdivision. Grids are a form of the implicit graph because we 




