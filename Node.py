import sys
from Verticle import *

class Node:
    
    def __init__(self,node_id):
        self.node_id = node_id
        self.connected_nodes = []
        self.connected_verticles = []
        self.shortest_way_to=sys.maxsize
        self.visit_tag = 0

    def createVerticle(self,weight,destination):
        vert = Verticle(weight)
        self.__addVerticle(vert,destination)
        if (self.node_id != destination.node_id):
            destination.__addVerticle(vert,self)

    def __addVerticle(self, verticle, node_to_connect):
        self.connected_verticles.append(verticle)
        self.connected_nodes.append(node_to_connect)

    def deleteVerticle(self,node):
        vert = self.getVerticle(node)

        index = self.connected_verticles.index(vert)
        index1 = node.connected_verticles.index(vert)

        self.__removeVerticle(index)
        if (self.node_id != node.node_id):
            node.__removeVerticle(index1)

    def __removeVerticle(self,index):
        self.connected_nodes.pop(index)
        self.connected_verticles.pop(index)

    def getConnectedNode(self,node_id):
        return next((node for node in self.connected_nodes if node.node_id == node_id), None)

    def getVerticle(self,node):
        if self.getConnectedNode(node.node_id):
            return self.connected_verticles[self.connected_nodes.index(node)]
        else:
            return None

    def getClosestUnvisitedNode(self):
        closest_unvisited_node = None
        min = sys.maxsize
        for i in range(len(self.connected_nodes)):
            if self.connected_verticles[i].weight < min and self.connected_nodes[i].visit_tag != 1:
                min = self.connected_verticles[i].weight
                closest_unvisited_node = self.connected_nodes[i]
        return closest_unvisited_node



    def __del__(self):
        while len(self.connected_nodes) != 0:
            self.connected_nodes[0].deleteVerticle(self)

    def print(self):
        print(self.node_id,end=" ")
        for i in range (len(self.connected_nodes)):
            print("->",end = " ")
            print(self.connected_nodes[i].node_id,end=" ")
            print(self.connected_verticles[i].weight, end=" ")




