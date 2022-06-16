import numpy as np
import matplotlib.pyplot as plt
import sys
import pdb
np.set_printoptions(threshold=sys.maxsize) #useful for debugging

class Node: #Format copied from https://www.annytab.com/a-star-search-algorithm-in-python/
    def __init__(self,position:(),parent:()):
        self.position=position
        self.parent=parent
        self.g=0 #Distance to goal
        self.s=0 #Distance to start
        self.f=0 #Cost
    def __eq__(self, other):
        return self.position == other.position
    def __lt__(self,other):
        return self.f<other.f
    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.f))

    


def search(map, start, end):
    openNode = []


    closedNode = []
    start_node = Node(start.tolist(), None)
    goal_node = Node(end.tolist(), None)

    openNode.append(start_node)

    while len(openNode) > 0:
        openNode.sort()
        currentNode = openNode.pop(0)
        closedNode.append(currentNode)
    #    pdb.set_trace()
        if ((currentNode) == (goal_node)):
            path = []
            while currentNode != start_node:
                path.append(currentNode.position)
                currentNode = currentNode.parent
            path.append(start_node.position)
            return path[::-1]
        [x,y]=currentNode.position
        neighbors=[(x,y-1),(x,y+1),(x-1,y),(x+1,y),(x-1,y-1),(x-1,y+1),(x+1,y-1),(x+1,y+1)]
        for nextNode in neighbors:
            value=map[nextNode[1],nextNode[0]]
            #pdb.set_trace()
            if value==1:
                continue
            Neighbor=Node([nextNode[0],nextNode[1]],currentNode)
           # print(Neighbor)
           # pdb.set_trace()
            if (Neighbor in closedNode):
                continue
            Neighbor.g = abs(Neighbor.position[0] - start_node.position[0]) + abs(Neighbor.position[1] - start_node.position[1])
            Neighbor.h = abs(Neighbor.position[0] - goal_node.position[0]) + abs(Neighbor.position[1] - goal_node.position[1])
            Neighbor.f = Neighbor.g + Neighbor.h
            # Check if neighbor is in open list and if it has a lower f value
            if(add_to_open(openNode, Neighbor) == True):
                # Everything is green, add neighbor to open list
                openNode.append(Neighbor)
    # Return None, no path is found
    return None
# Check if a neighbor should be added to open list
def add_to_open(openNode, neighbor):
    for node in openNode:
        if (neighbor == node and neighbor.f >= node.f):
            return False
    return True