##Tucker Styles
##C00460610
##INFX 301
##Section 001
##Certificate of Authenticity:
##Due Date : 10/23/23 @ 11:59 PM
##Program Description: Depth-First Search w/ Stack Implementation
##I, Tucker Styles, certify that the work I have submitted for this assignment is
##entirely my own work.

class Graph:
    
    def __init__(self, size):
        self.adjacencyMatrix = None
        self.graphSize = size
        self.visited = None

        self.createGraph(self.graphSize)

        

    def createGraph(self, graphSize):
        rowsList = []

        nodeNeighbors = ""

        i = 0

        while i < graphSize:
            print("Node " + str(i) + ": \n=============================")
            colsList = []
            j = 0
            while j < graphSize:
                isNeighbor = input("Enter 1 if [" + str(i) + "]["+ str(j) + "] is a neighbor of Node " + str(i) + ", or 0 if it's not a neighbor: ")

                while (isNeighbor != "1" and isNeighbor != "0"):
                    print("Invalid input!")
                    isNeighbor = input("Enter 1 if [" + str(i) + "]["+ str(j) + "] is a neighbor of Node " + str(i) + ", or 0 if it's not a neighbor: ")

                colsList.append(int(isNeighbor))
                if isNeighbor == "1":
                    nodeNeighbors += str(j) + " "
                j += 1
            
            rowsList.append(colsList)
            print("Node " + str(i) + " neighbors: " + nodeNeighbors)
            nodeNeighbors = ""
            i += 1
            self.adjacencyMatrix = rowsList

    def createVisited(self):
        array = []
        i = 0
        while i < self.graphSize:
            array.append(0)
            i += 1
        return array


    def graphToString(self):
        count = 0
        for i in self.adjacencyMatrix:
            print("Node: " + str(count) + str(i))
            count += 1

    def dfsWithStack(self, startNode):
        #print("Entered dfsWithStack")
        stack = createStack()
        visited = self.createVisited()
        currentNode = startNode
        push(stack, startNode)  # Push as integer
        print("Current stack: " + str(stack) + "\n\n")
        
        while (isEmpty(stack) is False):
            currentNode = pop(stack)  # Popping returns an integer
            print("Current stack: " + str(stack))
            visited[currentNode] = 1
            print("visited[]: " + str(visited))

            i = 0 
            while i < self.graphSize:
                #print("Does " + str(self.adjacencyMatrix[currentNode][i]) + " == 1 AND visited[ " + str(i) + "] -> (" + str(visited[i]) + ") == 0 ? : ")
                #print((self.adjacencyMatrix[currentNode][i] == 1) and (visited[i] == 0))
                if (self.adjacencyMatrix[currentNode][i] == 1) and (visited[i] == 0):
                    if visited[i] == 0:                       
                        print("Pushing node " + str(i) + " into stack. ")
                        push(stack, i)  # Push as integer
                i += 1

            print("Current stack: " + str(stack) + "\n")
            
        self.visited = visited
        return self.visited

def createStack():
    return []

def push(s, i):
    s.append(i)
    
def pop(s):
    if len(s) == 0:
        print("Nothing to pop, the stack was empty!")
    else:
        print("Popping node " + str(s[len(s)-1]) + " from the stack.") #shows the user which value it's removing
        temp = s[len(s)-1]
        del s[len(s)-1]
        return temp
    
def top(s):
    if len(s) == 0:
        print("The stack is empty!")
    else:
        return s[len(s)-1]
    
def isEmpty(s):
    if len(s) == 0:
        return True #why is the true/false capitilized in this language??? 
    else:
        return False


menuOption = ""
while menuOption != "0":
    menuOption = input("Enter 1 to enter new graph, enter 2 to select new start node, otherwise enter 0 to end program: ")
    while menuOption != "1" and menuOption != "2":
        if menuOption == "0":
            break
        print("Invalid input!")
        menuOption = input("Enter 1 to enter new graph, enter 2 to select new start node, otherwise enter 0 to end program: ")
        
    if menuOption == "1":
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
        graphTest.graphToString()
        
    elif menuOption == "2":
        startNode = input("Enter the starting node of the graph: ")
        while startNode.isdigit() == False:
            print("Invalid input!")
            startNode = input("Enter the size of the graph: ")

        while (int(startNode) < 0) or (int(startNode) >= graphSize):
            print("Non-existing node!")
            startNode = input("Enter the starting node of the graph: ")
            while startNode.isdigit() == False:
                print("Invalid input!")
                startNode = input("Enter the starting node of the graph: ")

        startNode = int(startNode)
        graphTest.dfsWithStack(startNode)
print("Program Ended")
