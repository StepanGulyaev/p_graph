from Graph import *

if __name__ == '__main__':
    gr = Graph("Gr1")
    while True:
        print("Graph builder menu")
        print("  Press 1 to create graph")
        print("  Press 2 to add node")
        print("  Press 3 to add verticle")
        print("  Press 4 to delete node")
        print("  Press 5 to delete verticle")
        print("  Press 6 to search path between two nodes")
        print("  Press 7 to search shortest path between two nodes")
        print("  Press 8 to see connected components")
        print("  Press 9 to delete graph")
        print("  Press 0 to exit")
        print("Enter option:",end=" ")

        option = str(input())
        match option:

            case "1":
                gr.addNodes()
                gr.addVerticles()
                print()
                gr.print()
                print()

            case "2":
                print("Enter node's unique name:", end=" ")
                name = str(input())
                if gr.getNode(name):
                    print("Node with that name already exists!")
                else:
                    new_node = Node(name)
                    gr.addNode(new_node)
                print()
                gr.print()
                print()

            case "3":
                while True:
                    print("Enter two nodes verticle connects and verticle's weight.")
                    print("(Don't divide info by spaces.Better use node/node/weight format)")
                    print("Enter verticle info:", end=" ");
                    info = str(input()).split("/")
                    if len(info) != 3:
                        print("Wrong input format!")
                    elif int(info[2]) == 0:
                        print("Verticle weight can't be 0!")
                    elif not (gr.getNode(info[0]) and gr.getNode(info[1])):
                        print("There is no nodes with names like that!")
                    else:
                        node1 = gr.getNode(info[0])
                        node2 = gr.getNode(info[1])
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
                print()
                gr.print()
                print()

            case "4":
                print("Enter node's unique name:", end=" ")
                name = str(input())
                node = gr.getNode(name)
                if not node:
                    print("Node with that name doesn't exist!")
                else:
                    node = gr.getNode(name)
                    gr.deleteNode(node)
                print()
                gr.print()
                print()

            case "5":
                print("Enter first node name:", end=" ")
                info1 = str(input())
                print("Enter second node name:", end=" ")
                info2 = str(input())
                node1 = gr.getNode(info1)
                node2 = gr.getNode(info2)
                if not (node1 and node2):
                    print("There is no nodes with names like that!")
                else:
                    if node1.getVerticle(node2):
                        node1.deleteVerticle(node2)
                    else:
                        print("Verticle doesn't exist!")
                print()
                gr.print()
                print()

            case "6":
                print("Enter first node name:", end=" ")
                info1 = str(input())
                print("Enter second node name:", end=" ")
                info2 = str(input())
                node1 = gr.getNode(info1)
                node2 = gr.getNode(info2)
                if not (node1 and node2):
                    print("There is no nodes with names like that!")
                else:
                    gr.searchPath(node1,node2)

            case "7":
                grCopy = copy.deepcopy(gr)
                print("Enter first node name:", end=" ")
                info1 = str(input())
                print("Enter second node name:", end=" ")
                info2 = str(input())
                node1 = grCopy.getNode(info1)
                node2 = grCopy.getNode(info2)
                if not (node1 and node2):
                    print("There is no nodes with names like that!")
                else:
                    grCopy.searchShortestPath(node1,node2)
                    gr.print()
                    print()

            case "8":
                grCopy = copy.deepcopy(gr)
                grCopy.components()
                print()

            case "9":
                gr = Graph("gr1")

            case "0":
                break


