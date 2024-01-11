##Tucker Styles
##C00460610
##INFX 301
##Section 001
##Certificate of Authenticity:
##Due Date : 11/29/23 @ 11:59 PM
##Program Description: Critical Path Algorithm
##I, Tucker Styles, certify that the work I have submitted for this assignment is
##entirely my own work.
class Graph:
    def __init__(self, size):
        self.adjacencyMatrix = None
        self.graphSize = size
        self.visited = [0] * size

        self.createGraph(self.graphSize + 2)

    def createGraph(self, graphSize):
        print("Enter createGraph()")
        print(graphSize)

        rowsList = []
        i = 0

        while i < graphSize:
            colsList = []
            j = 0
            while j < graphSize:  # Fix: Change i to j
                colsList.append(-1)
                j += 1
            rowsList.append(colsList)
            i += 1
        self.adjacencyMatrix = rowsList

        print("Graph initialized")

        i = 0
        while i < len(self.adjacencyMatrix):
            if(i < self.graphSize):
                print("Node " + str(i) + ": \n=============================")
            elif (i == self.graphSize):
                print("Start node (s): \n=============================")
            else:
                print("Stop node (t): \n=============================")
            j = 0
            while j < len(self.adjacencyMatrix[i]):
                while True:
                    isNeighbor = input("Enter any non-negative value if [" + str(i) + "][" + str(j) + "] is a neighbor of Node " + str(i) + ", or -1 if it's not a neighbor: ")
                    if isNeighbor.isdigit() or (isNeighbor.startswith('-') and isNeighbor[1:].isdigit()): #uses string slice to check if value after '-' is a digit, 
                        isNeighbor = int(isNeighbor)
                        if isNeighbor >= -1:
                            break
                    print("Invalid input! Please enter a valid non-negative integer or -1.")
                self.adjacencyMatrix[i][j] = int(isNeighbor)
                j += 1
            i += 1
                    

    def createVisited(self):
        array = []
        i = 0
        while i < len(self.adjacencyMatrix):
            array.append(0)
            i += 1
        return array


    def graphToString(self):
        count = 0
        i = 0
        while i < self.graphSize:
            print("Node: " + str(count) + str(self.adjacencyMatrix[i]))
            count += 1
            i += 1
            
        print("Node: s" + str(self.adjacencyMatrix[self.graphSize]))
        print("Node: t" + str(self.adjacencyMatrix[self.graphSize + 1]))
        
    def criticalPath(self):
    
        dist = [0] * len(self.adjacencyMatrix)
        dist[len(self.adjacencyMatrix) - 1] = 0  # Set the source node distance to 0
        pred = [-1] * len(self.adjacencyMatrix)
        sortedNodes = self.topologicalSort()
    
        i = 0
        while i < len(sortedNodes):
            topVal = sortedNodes[i]
            j = 0
            while j < len(self.adjacencyMatrix[topVal]):
                if ( self.adjacencyMatrix[topVal][j] != -1 and dist[j] < dist[topVal] + self.adjacencyMatrix[topVal][j]):
                    dist[j] = dist[topVal] + self.adjacencyMatrix[topVal][j]
                    pred[j] = topVal
                j += 1
            i += 1
            
        outputPred = []
        outputPred.append(-1)
        outputPred.append(len(pred) - 2)
        i = 1
        while i < (len(pred) - 2) and pred[i] != -1:
            outputPred.append(pred[i])
            i += 1
        outputPred.append(pred[(len(pred) - 1)])
        
        outputDist = []
        outputDist.append(0)
        i = 0
        while i < (len(dist) - 2) and dist[i] != -1:
            outputDist.append(dist[i])
            i += 1
        outputDist.append(dist[(len(dist) - 1)])
        
        
        path = [0] * len(self.adjacencyMatrix)
        path[0] = len(self.adjacencyMatrix) - 2
        path[len(self.adjacencyMatrix) - 1] = len(self.adjacencyMatrix) - 1
        i = 1
        while i < len(self.adjacencyMatrix) - 1:
            path[i] = i - 1
            i += 1
        
        finalList = []
        finalList.insert(0, "t")
        i = path[len(path) - 1]
        while i != path[1]:
            finalList.insert(0, pred[i])
            i = path[pred[i] + 1]
        finalList.insert(0, "s")
        
        print("==============================")
        print("pred[]: " + str(outputPred))
        print("dist[]: " + str(outputDist))
        print("Longest Path: " + str(finalList))
        print("==============================")
        
        
    def topologicalSort(self):
        self.visited = self.createVisited()
        sortedNodes = []
    
        i = 0
        while i < len(self.adjacencyMatrix):
            if self.visited[i] == 0:
                self.dfsTopologicalSort(i, sortedNodes)
            i += 1
        return sortedNodes

        
    def dfsTopologicalSort(self, node, sortedNodes):
        self.visited[node] = 1
    
        neighbor = 0
        while neighbor < len(self.adjacencyMatrix[node]):
            if (
                self.adjacencyMatrix[node][neighbor] != -1
                and neighbor < len(self.visited)
                and self.visited[neighbor] == 0
            ):
                self.dfsTopologicalSort(neighbor, sortedNodes)
            neighbor += 1
    
        sortedNodes.insert(0, node)

def menu():
    graphTest = None
    
    print("A. Input a task scheduling graph G, and generate an adjacencyList for graph G.\n"
        + "B. Calculate and print the nodes that are on the critical path.\n"
        + "C. Print the adjacency list for graph G.\n"
        + "D. End program. ")
    
    userIn = input("Enter the letter that corresponds to the desired link list operation:\n" )
    
    while(userIn.lower() != "d"): 
        if(userIn.lower() == "a"):
            graphSize = input("Enter the size of the graph: ")
            while graphSize.isdigit() == False:
                print("Invalid input!")
                graphSize = input("Enter the size of the graph: ")

            graphSize = int(graphSize)
            while graphSize <= 0:
                graphSize = input("Size must be greater than zero! Enter the size of the graph: ")
                while graphSize.isdigit() == False:
                    print("Invalid input!")
                    graphSize = input("Enter the size of the graph: ")
                graphSize = int(graphSize)
                
            graphTest = Graph(graphSize)
            #graphTest.adjacencyMatrix = testCriticalPath
            graphTest.graphSize = len(graphTest.adjacencyMatrix) - 2
            graphTest.graphToString()
                
        elif(userIn.lower() == "b"):
            if(graphTest == None):
                print("Graph doesn't exist! Please create a graph!")
            else:
                graphTest.criticalPath()

            
        elif(userIn.lower() == "c"):
            if(graphTest == None):
                print("Graph doesn't exist! Please create a graph!")
            else:
                graphTest.graphToString();
            
        else: 
            print("\nInvalid option! Please enter A, B, C, or D. ")
            
            print("A. Input a task scheduling graph G, and generate an adjacencyList for graph G.\n"
                + "B. Calculate and print the nodes that are on the critical path.\n"
                + "C. Print the adjacency list for graph G.\n"
                + "D. End program. ")
        
        userIn = input("Enter the letter that corresponds to the desired link list operation: " )


#testCriticalPath = [
#    [-1, 6, -1, 4, -1, -1, -1, -1],  # node 0
#    [-1, -1, 5, -1, -1, -1, -1, -1],  # node 1
#    [-1, -1, -1, -1, 12, 3, -1, -1],  # node 2
#    [-1, -1, 9, -1, -1, -1, -1, -1],  # node 3
#    [-1, -1, -1, -1, -1, -1, -1, 0],  # node 4
#    [-1, -1, -1, -1, 2, -1, -1, -1],  # node 5
#    [0, -1, -1, -1, -1, -1, -1, -1],  # node 6 (s)
#    [-1, -1, -1, -1, -1, -1, -1, -1]  # node 7 (t)
#]

menu()
print("\nEnding program...")
