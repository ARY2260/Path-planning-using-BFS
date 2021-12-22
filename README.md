# Path planning using BFS

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

**BFS Algorithm-**
<br>

Breadth-first search (BFS) is an algorithm that is used to graph data or search tree or traverse structures. Let us understand the working of the algorithm with an example
In the various levels of the data, you can mark any node as the starting or initial node to begin traversing. The BFS will visit the node and mark it as visited and places it in the queue. Now the BFS will visit the nearest and un-visited nodes and mark them. These values are also added to the queue.

* Step-1: Each vertex or node in the graph is known. For instance, you can mark the node as V 
* Step-2: In case the vertex V is not accessed then add the vertex V into the BFS Queue
* Step-3: Start the BFS search, and after completion, Mark vertex V as visited.
* Step-4: The BFS queue is still not empty, hence remove the vertex V of the graph from the queue.
* Step-5: Retrieve all the remaining vertices on the graph that are adjacent to the vertex V
* Step-6: For each adjacent vertex let’s say V1, in case it is not visited yet then add V1 to the BFS queue
* Step-7: BFS will visit V1 and mark it as visited and delete it from the queue.
* Step-8: Move to the next vertex and repeat the process 
<br>

### Which Data Structure to Use for the Solution (Details of the Data Structure)

We will be using GRAPH for the solution.  
Graphs have a wide range of applications in our world. Graphs are used to model paths in a city, as often seen in Google Maps. They are used to model social networks such as Facebook or LinkedIn. Graphs are also used to monitor website backlinks, internal employee networks, etc. 
A graph is an image that represents a set of objects to which other pairs of objects are linked. Connecting objects are represented by points called vertices or nodes, and connecting connectors with vertices are called edges. A Graph is a non-linear data structure that can be represented using an array of vertices and a two-dimensional array of edges. We will also use GRID for implementing our algorithm. Grids are important data structures to represent geometric structures or their subdivision. Grids are a form of the implicit graph because we can determine a node’s neighbors based on our location within the grid.

### Justify Why This is the Best Data Structure for this Application?

Graphs data structure are used in the implementation of this project that is BFS algorithm is used on these graphs because they are a powerful and versatile data structure that easily allows you to represent real-life relationships between different types of data. Since graphs can easily map any size of area or system and in a sequential manner using the system of coordinates It gives us a good medium to apply our algorithm on. No other data structure can be used to visualize the paths between two points much less find the most efficient path. Secondly, Graphs are the best choices here because they are easy to implement by using a list or array. You have the flexibility to choose representation according to your requirement. Finally, graphs are the way to go because they provide a compact model of the system or map and can store data of the relations between each entity or vertex in the graph (example weighted edges) and also allow access and manipulation of this data as and when required systemically.

### Implementation Details (Experimental Setup)

The BFS algorithm is implemented over a 5X7 grid (example) in Python3 language. The grid contains various elements such as '.' representing a clear path, '#' representing the obstacles, 'S' representing Start, and 'E' representing Exit.

**Backend:**
<br>

Three key functions involved are: explore_neighbour(), solve() and reconstructPath().
<br>

* The explore_neighbour() function uses direction vectors to explore nearest neighbours and adds suitable neighbours for further exploration in queue objects defined based on queue class. It also keeps track of already visited nodes as well as parent nodes of the current node using 2d arrays named visited and prev respectively. 
* The solve() function is where the algorithm implementation takes place. It explores the nodes present in queue objects until the exit node ‘E’ is found or the queue objects are empty.
* The reconstructPath() function traverses through the prev 2d array and stores the path in the form of an array of tuples containing nodes’ indices. If the path starts from the Start node, then the generated path is returned, else the empty path is returned.
<br>

**Frontend: (visualisation)**
<br>

The visuals are generated using a user-defined package named: graphics.py which is built upon the Tkinter library. (Credits: written by John Zelle for use with the book "Python Programming: An Introduction to Computer Science)
<br>

The entire visualization is executed in a 1000 X 600 pixels window. For grid and objects visualization, the indices of nodes were scaled 100 times and were used as coordinates for the generation of objects like rectangles, circles, and letters on the graphic window. A separate agent class is defined which is represented by the letter ‘X’ that moves across the grid along the generated path. 

### Complexity Analysis

**Time Complexity**
A graph is a pair of sets (V, E), where V is the set of vertices and E is the set of edges, connecting the pairs of vertices. The time complexity of BFS can be computed as the total number of iterations performed by the for a loop.
Let E' be the set of all edges in the connected component visited by the algorithm. For each edge {u, v} in E,' the algorithm makes two for loop iteration steps: one time when the algorithm visits the neighbours of u, and one time when it visits the neighbours of v. Hence, the time complexity is Θ (|V| + |E'|).
<br>

**Space Complexity**
When the number of vertices in the graph is known ahead of time, and additional data structures are used to determine which vertices have already been added to the queue, the space complexity can be expressed as O(|V|), where |V| is the number of vertices. This is in addition to the space required for the graph itself, which may vary depending on the graph representation used by an implementation of the algorithm.

### Observations and Conclusions

Path planning algorithms are used by mobile robots, unmanned aerial vehicles, and autonomous cars to identify safe, efficient, collision-free, and least-cost travel paths from an origin to a destination. In our model, we have built a matrix grid cell of 5X7. With some obstacles at some grids represented by “#”, no obstacles represented by “.”, start point represented by “S”, and endpoint represented by “E” So, using our algorithm we found the shortest path for our object for movement from S-> E. Using python graphical library, we showed our shortest path and detected obstacles in a new window named “My grid”.

We can apply this algorithm to real-life applications like path planning for autonomous vehicles, robot path planning, etc., and get the desired output.


