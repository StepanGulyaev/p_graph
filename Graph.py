import copy

from Node import *

class Graph:

    def __init__(self, name):
        self.name = name
        self.nodes = []

    def addNode(self, node):
        self.nodes.append(node)

    def deleteNode(self,node):
        self.nodes.remove(node)
        node.__del__()

    def print(self):
        for i in range(len(self.nodes)):
            self.nodes[i].print()
            print()

    def printList(self):
        for i in range(len(self.nodes)):
            print(self.nodes[i].node_id,end="")
            print(";",end="")

    def addNodes(self):
        print("You're creating nodes now")
        while True:
            print("Type 1 to create a new node, type 0 to exit:",end=" ")

            option = str(input())

            match option:
                case "1":
                    print("Enter node's unique name:",end=" ")
                    name = str(input())
                    if self.getNode(name):
                        print("Node with that name already exists!")
                    else:
                        new_node = Node(name)
                        self.addNode(new_node)
                case "0":
                    break;
                case _:
                    print("Wrong input!")
                    continue

            print("Nodes created:",end=" ");
            self.printList()
            print()

        print()
        print("Nodes you have created:",end=" ");
        self.printList()
        print()
        print()

    def getNode(self,node_id):
        return next((node for node in self.nodes if node.node_id == node_id), None)


    def addVerticles(self):
        print("Now, create the verticles:");
        while True:
            print("Type 1 to create a new verticle, type 0 to exit:", end=" ")
            option = str(input())
            match option:
                case "1":
                    while True:
                        print("Enter two nodes verticle connects and verticle's weight.")
                        print("(Don't divide info by spaces.Better use node/node/weight format)")
                        print("Enter verticle info:", end=" ");
                        info = str(input()).split("/")
                        if len(info) != 3:
                            print("Wrong input format!")
                        elif int(info[2]) == 0:
                            print("Verticle weight can't be 0!")
                        elif not (self.getNode(info[0]) and self.getNode(info[1])):
                            print("There is no nodes with names like that!")
                        else:
                            node1 = self.getNode(info[0])
                            node2 = self.getNode(info[1])
                            if node1.getVerticle(node2):
                                while True:
                                    print("Verticle between these nodes already exists, do you want to overwrite it?")
                                    print("1 - yes, 0 - no:", end=" ")
                                    option1 = str(input())
                                    match option1:
                                        case "1":
                                            node1.deleteVerticle(node2)
                                            node1.createVerticle(int(info[2]), node2)
                                            break
                                        case "0":
                                            break
                                        case _:
                                            print("Wrong input!")
                                            continue
                            else:
                                node1.createVerticle(int(info[2]), node2)
                            break
                case "0":
                    break
                case _:
                    print("Wrong input!")
                    continue

    def searchPath(self,node1,node2):
        visited = []
        self.__searchInDepth(node1,node2,visited)
        if len(visited) == 0:
            print("")
            print("There is no way between these nodes!")
            print("")
        else:
            print()
            print("Way:",end= " ")
            print(visited[0].node_id,end= "")
            for i in range(1,len(visited)):
                print("-",end="")
                print(visited[i].node_id,end="")
            print(" Length:",end= " ")
            print(self.__getWayLength(visited))
            self.__setDefaultTags()
            print()
            print()

    def __searchInDepth(self,fromNode,toNode,visited):
        fromNode.visit_tag = 1
        visited.append(fromNode)
        if toNode.visit_tag == 1:
            return
        else:
            for i in range(len(fromNode.connected_verticles)):
                if fromNode.connected_nodes[i].visit_tag == 0:
                    self.__searchInDepth(fromNode.connected_nodes[i],toNode,visited)
                    if toNode.visit_tag == 1:
                        break

            if toNode.visit_tag != 1:
                visited.remove(fromNode)

    def __getWayLength(self,visited):
        sum = 0
        for i in range (len(visited)-1):
            sum+= visited[i].getVerticle(visited[i+1]).weight
        return sum

    def __setDefaultTags(self):
        for i in range(len(self.nodes)):
            self.nodes[i].visit_tag = 0

    def __setDefaultShortestWay(self):
        for i in range(len(self.nodes)):
            self.nodes[i].shortest_way_to = sys.maxsize


    def searchShortestPath(self,nodeFrom,nodeTo):
        result = [0]
        nodeFrom.shortest_way_to = 0
        if self.__isNegativeVerticles():
            result[0] = self.__bellmanFordAlgorithm(nodeTo)
        else:
            self.__dijkstraAlgorithm(nodeFrom,nodeTo,result)

        print()
        if result[0] == sys.maxsize:
            print("There is no way between these nodes!")
        else:
            print("Shortest path between ",end="")
            print(nodeFrom.node_id,end="")
            print(" and ",end="")
            print(nodeTo.node_id, end="")
            print(" has length:", end="")
            print(result[0])
        print()



    def __isNegativeVerticles(self):
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes[i].connected_verticles)):
                if self.nodes[i].connected_verticles[j].weight < 0:
                    return True
        return False


    def __bellmanFordAlgorithm(self,nodeTo):
        for i in range(len(self.nodes)-1):
            tmp = copy.deepcopy(self.nodes)
            for j in range(len(tmp)):
                cur_node_in_copy = tmp[j]
                desc_ways = self.__descWay(cur_node_in_copy)
                for k in range(len(desc_ways)):
                    name = desc_ways[k].node_id
                    node_to_change_short_way = next((node for node in self.nodes if node.node_id == name), None)
                    node_to_change_short_way.shortest_way_to = desc_ways[k].shortest_way_to
                    cur_node_in_copy.deleteVerticle(desc_ways[k])
        return nodeTo.shortest_way_to

    def __dijkstraAlgorithm(self,nodeFrom,nodeTo,result):
        for i in range(len(nodeFrom.connected_nodes)):
            if (nodeFrom.shortest_way_to + nodeFrom.connected_verticles[i].weight < nodeFrom.connected_nodes[i].shortest_way_to) and (nodeFrom.visit_tag !=1):
                nodeFrom.connected_nodes[i].shortest_way_to = nodeFrom.shortest_way_to + nodeFrom.connected_verticles[i].weight
        closest_node = nodeFrom.getClosestUnvisitedNode()
        if closest_node != None:
            nodeFrom.visit_tag = 1
            self.__dijkstraAlgorithm(closest_node,nodeTo,result)
        result[0] = nodeTo.shortest_way_to


    def __descWay(self,node):
        to_delete_ways_array = []
        for i in range(len(node.connected_verticles)):
            if node.shortest_way_to + node.connected_verticles[i].weight <= node.connected_nodes[i].shortest_way_to:
                node.connected_nodes[i].shortest_way_to = node.shortest_way_to + node.connected_verticles[i].weight
                to_delete_ways_array.append(node.connected_nodes[i])
        return to_delete_ways_array


    def components(self):
        print("Components: ")
        while len(self.nodes) != 0:
            print()
            component = []
            component.append(self.nodes[0])
            for i in range(len(self.nodes[0].connected_nodes)):
                component.append(self.nodes[0].connected_nodes[i])
                self.nodes.remove(self.nodes[0].connected_nodes[i])
            for i in range(1,len(self.nodes)):
                visited = []
                self.__searchInDepth(self.nodes[0],self.nodes[i],visited)
                if len(visited) != 0:
                    component.append(self.nodes[i])
                    self.nodes.remove(self.nodes[i])
            self.nodes.remove(self.nodes[0])
            print("        ",end="")
            for i in range(len(component)):
                print(component[i].node_id, end="")
                print(";", end="")
            print()




















