# %%
import numpy as np
from graphics import *
import time
# %%

R, C = 5, 7
m = [['S', '.', '.', '#', '.', '.', '.'],
     ['.', '#', '.', '.', '.', '#', '.'],
     ['.', '#', '.', '#', '.', '.', '#'],
     ['.', '.', '#', '.', '#', '.', '.'],
     ['#', '.', '#', 'E', '.', '.', '#']]

# %%


class queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)


# %%
sr, sc = 0, 0
s = (sr, sc)
e = (0,0)
rq, cq = queue(), queue()

# %%
move_count = 0
nodes_left_in_layer = 1
nodes_in_next_layer = 0
# %%
reach_end = False
# %%
visited = np.zeros((5, 7))
# prev = np.empty((5, 7))
# prev.fill(0)
prev = [[0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]]
# %%
dr = [-1, +1, 0, 0]
dc = [0, 0, +1, -1]

#%%
def rectangle(rr,cc):
    rr *=100
    cc *=100
    rect = Rectangle(Point(cc,rr), Point(100+cc, 100+rr))
    rect.draw(win)

def circle(rr,cc):
    rr *=100
    cc *=100
    c = Circle(Point(cc+50,rr+50), 25)
    c.draw(win)

def text(rr,cc,text_input):
    rr *=100
    cc *=100
    text = Text(Point(cc+50,rr+50),text_input)
    text.setSize(30)
    text.draw(win)

class agent:
    def __init__(self,cr,cc):
        self.cr=cr*100
        self.cc=cc*100
        self.text = Text(Point(self.cc+50,self.cr+50),'X')
        self.text.draw(win)
    def movement(self,mr,mc):
        mr *=100
        mc *=100
        self.text.move((mc-self.cc),(mr-self.cr))
        self.cc= mc
        self.cr= mr

# %%
def draw_grid(R,C):
    for i in range(R):
        for j in range(C):
            rectangle(i,j)


#%%


def explore_neighbours(r, c):
    global nodes_in_next_layer, prev
    for i in range(0, 4):
        rr = r + dr[i]
        cc = c + dc[i]

        
        
        if rr < 0 or cc < 0:
            continue
        if rr >= R or cc >= C:
            continue

        if visited[rr][cc]:
            continue
        if m[rr][cc] == '#':
            circle(rr,cc)
            continue
        rq.enqueue(rr)
        cq.enqueue(cc)
        visited[rr][cc] = True
        prev[rr][cc] = (r, c)
        nodes_in_next_layer += 1

# %%


def solve():
    global reach_end, e,move_count, nodes_left_in_layer, nodes_in_next_layer
    rq.enqueue(sr)
    cq.enqueue(sc)
    visited[sr][sc] = True
    while rq.size() > 0:
        r = rq.dequeue()
        c = cq.dequeue()
        if m[r][c] == 'E':
            e = (r, c)
            text(r,c,"E")
            reach_end = True
            break
        explore_neighbours(r, c)
        nodes_left_in_layer -= 1
        if nodes_left_in_layer == 0:
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count += 1

    if reach_end:
        return move_count
    return -1

# %%


def reconstructPath(prev):
    global e
    path = []
    at = e
    while(at != 0.0):
        path.append(at)
        at = prev[at[0]][at[1]]
    path.reverse()

    if path[0] == s:
        return path
    return []
    
# %%
win = GraphWin("My Grid", 1000, 600)
draw_grid(R,C)
text(sc,sr,"S")
print(solve())
agent_0 = agent(sc,sr)
path_0 = reconstructPath(prev)
for i in path_0:
    agent_0.movement(i[0],i[1])
    time.sleep(1)
    line = Line(Point(agent_0.cc+100,agent_0.cr+100),Point((i[1])*100,(i[0])*100))
    line.draw(win)
    time.sleep(1)
win.getMouse() # Pause to view result
win.close()