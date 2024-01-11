##Tucker Styles
##C00460610
##INFX 301
##Section 001
##Certificate of Authenticity:
##Due Date : 11/13/23 @ 11:59 PM
##Program Description: Linked List
##I, Tucker Styles, certify that the work I have submitted for this assignment is
##entirely my own work.

class LinkedList:
    def __init__(self):
        self.dataList = []
        self.linkList = []
        self.freeNodes = []
        self.headPtr = -1

    def getNode(self):
        i = 0
        while(i < len(self.freeNodes)):
            if(self.freeNodes[i] == True):
                return i
            else:
                return -1
            i = self.linkList[i];

    def searchList(self, findNode):
        i = self.headPtr
        while(i != -1):
            if(self.dataList[i] == findNode):
                return i
            i = self.linkList[i]
        
        print("Node not found!")
        return -1

    def printListContents(self):
        if len(self.linkList) == 0 and len(self.dataList) == 0:
            print("No items in the list!")
        else:
            i = self.headPtr
            while i != -1:
                nodeData = self.dataList[i]
                print("\t" + str(nodeData))
                i = self.linkList[i]
                del nodeData
        print()


    def printListFull(self):
        if len(self.linkList) == 0 and len(self.dataList) == 0:
            print("No items in the list!")
        else:
            i = self.headPtr
            print("\tHeadPointer: " + str(i))
            print("\tData List | Link List | Free Node")
            while(i != -1):
                #if(self.freeNodes[i] != True):
                nodeData = self.dataList[i]
                nodeLink = self.linkList[i]
                isNodeFree = self.freeNodes[i]
                print("\t\t" + str(nodeData) + " | " + str(nodeLink) + " | " + str(isNodeFree))
                del nodeData
                del nodeLink
                del isNodeFree
                i = self.linkList[i]
            print("\nUnordered Full: ")
            print("\t" + str(self.dataList))
            print("\t" + str(self.linkList))
            print("\t" + str(self.freeNodes))
        print()

    def searchFreeNode(self):
        i = 0
        while(self.linkList[i] != -1):
            if(self.freeNodes[i] == True):
                return i
            i = i + 1
        return -1


    def insertNode(self, newNode):
       
        if(len(self.linkList) == 0 and len(self.dataList) == 0):
            self.dataList.append(newNode)
            self.linkList.append(self.headPtr) #if its empty headPtr should equal -1
            self.freeNodes.append(False)
            self.headPtr = 0
            return 1
        
        elif(self.searchFreeNode() != -1):
            freeNodeIndex = self.searchFreeNode()
            self.dataList[freeNodeIndex] = newNode
            self.freeNodes[freeNodeIndex] = False
            prevIndex = -1
            currentIndex = self.headPtr
            
            while(currentIndex != -1 and self.dataList[currentIndex] < newNode):
                prevIndex = currentIndex
                currentIndex = self.linkList[currentIndex]
    
            if(prevIndex == -1):
                self.linkList[freeNodeIndex] = self.headPtr
                self.headPtr = freeNodeIndex
                return 1
            else:
                self.linkList[freeNodeIndex] = currentIndex
                self.linkList[prevIndex] = freeNodeIndex
                return 1
            return -1
            
        else:
            
            if(newNode < self.dataList[self.headPtr]):
                self.dataList.append(newNode)
                self.linkList.append(self.headPtr)
                self.freeNodes.append(False)
                self.headPtr = (len(self.linkList) - 1)
                
            else:
                nextNode = self.linkList[self.headPtr] #grabs index after headPtr
                prevNode = self.headPtr #sets prev to headPtr
                while(nextNode != -1):
                    if(newNode < self.dataList[nextNode]): #is newNode alphabetically less than the next node
                        self.dataList.append(newNode) #add newNode to dataList
                        self.linkList.append(nextNode) #add 
                        self.linkList[prevNode] = (len(self.linkList) - 1)
                        self.linkList[len(self.linkList) - 1] = nextNode
                        self.freeNodes.append(False)
                        return 1
                    prevNode = nextNode
                    nextNode = self.linkList[nextNode]
                    
                if(nextNode == -1):
                    self.linkList.append(-1)
                    self.dataList.append(newNode)
                    self.freeNodes.append(False)
                    self.linkList[prevNode] = (len(self.linkList) - 1)
                    self.linkList[len(self.linkList) - 1] = nextNode
        
        return -1

    def deleteNode(self, removeNode):
        if len(self.linkList) == 0 and len(self.dataList) == 0:
            print("Nothing to delete!")
            return -1
            
        removeIndex = self.searchList(removeNode)
        
        if(removeIndex != -1):
            if(removeIndex == self.headPtr):
                self.freeNodes[removeIndex] = True
                self.headPtr = self.linkList[removeIndex]
                return 1
            elif(self.linkList[removeIndex] == -1):
                prevNode = self.headPtr
                i = self.linkList[self.headPtr]
                while(self.linkList[i] != -1):
                    prevNode = i
                    i = self.linkList[i]
                self.linkList[prevNode] = -1
                self.linkList[removeIndex] = 0
                self.freeNodes[removeIndex] = True
                return 1
            else:
                
                prevNode = self.headPtr
                while self.linkList[prevNode] != removeIndex:
                    prevNode = self.linkList[prevNode]

                nextNode = self.linkList[removeIndex]
                self.linkList[prevNode] = nextNode
                self.freeNodes[removeIndex] = True
            return 1
        else:
            print("Node not found!")
            return -1



def menu():
    
    print("A. Insert a new item (i.e., string) into the ordered singly-linked list.\n"
        + "B. Delete a specified item (i.e., string) from the ordered singly-linked list.\n"
        + "C. Print all items (i.e., strings) in the ordered singly-linked list.\n"
        + "D. Print the contents of the following:\n"
        + "\t• Data array\n"
        + "\t• Link array\n"
        + "\t• FreeNodes array\n"
        + "\t• Value of headPtr\n"
        + "E. End program.")
    
    userIn = input("Enter the letter that corresponds to the desired link list operation:\n" )
    
    while(userIn.lower() != "e"): 
        if(userIn.lower() == "a"):
            userIn = input("\nEnter data to insert into linked list: ")
            linkListTest.insertNode(userIn)
            print("Inserting " + userIn + " into Linked List.\n")
        elif(userIn.lower() == "b"):
            userIn = input("\nEnter data to delete from linked list: ")
            linkListTest.deleteNode(userIn)
            print("Removing " + userIn + " from Link List.\n")
        elif(userIn.lower() == "c"):
            print("\nData List: ")
            linkListTest.printListContents()
        elif(userIn.lower() == "d"):
            print("\nFull Link List: ")
            linkListTest.printListFull()
        else: 
            print("\nInvalid option! Please enter A, B, C, D, or E.")
            
        print("A. Insert a new item (i.e., string) into the ordered singly-linked list.\n"
            + "B. Delete a specified item (i.e., string) from the ordered singly-linked list.\n"
            + "C. Print all items (i.e., strings) in the ordered singly-linked list.\n"
            + "D. Print the contents of the following:\n"
            + "\t• Data array\n"
            + "\t• Link array\n"
            + "\t• FreeNodes array\n"
            + "\t• Value of headPtr\n"
            + "E. End program.\n")
        
        userIn = input("Enter the letter that corresponds to the desired link list operation: " )

linkListTest = LinkedList()
menu()
print("Ending Program...")


        
            
            
        
