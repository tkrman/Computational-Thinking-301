##Tucker Styles
##C00460610
##INFX 301
##Section 001
##Certificate of Authenticity:
##Due Date : 9/20/23 @ 11:59 PM
##Program Description: Array-Based Stack Implementation
##I, Tucker Styles, certify that the work I have submitted for this assignment is
##entirely my own work.

def createStack():
    return []

def push(s, i):
    s.append(i)
    
def pop(s):
    if len(s) == 0:
        print("Nothing to pop, the stack was empty!")
    else:
        print("Popping (removing) number from the top of the stack: " + str(s[len(s)-1])) #shows the user which value it's removing
        del s[len(s)-1]
    
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
        
def menu():
    #apparently no do-while in this language 
    
    print("A. Push a number (i.e., integer) on the top of the stack.\n"
        + "B. Pop a number (i.e., integer) from the top of the stack.\n"
        + "C. Display the value of the number (i.e., integer) on the top of the stack.\n"
        + "D. Indicate whether the stack is EMPTY or NOT EMPTY.\n"
        + "E. End program.\n")
    userIn = input("Enter the letter that corresponds to the desired stack operation:\n" )
    
    #.lower() used to simplify code, turns all inputs lowercase and compares once, no AND/OR statement necessary    
    while userIn.lower() != "e": 
        if userIn.lower() == "a":
            numIn = int(input('Enter a number to push (add) to the top of the stack: '))
            push(stack, numIn)
            print("Current Stack: " + str(stack) + "\n" )
        elif userIn.lower() == "b":
            pop(stack)
            print("Current Stack: " + str(stack) + "\n" )
        elif userIn.lower() == "c":
            print("The top of the stack is: " + str(top(stack)))
        elif userIn.lower() == "d":
            
            if isEmpty(stack):
                emptyCheck = "EMPTY"
            else:
                emptyCheck = " NOT EMPTY"
            print("Is the stack empty? " + emptyCheck)
            
        #elif userIn.lower() == "e":  *removed; unnecessary due to loop already checking for that
        else: 
            print("\nInvalid option! Please enter A, B, C, D, or E.")
            
        print("A. Push a number (i.e., integer) on the top of the stack.\n"
            + "B. Pop a number (i.e., integer) from the top of the stack.\n"
            + "C. Display the value of the number (i.e., integer) on the top of the stack.\n"
            + "D. Indicate whether the stack is EMPTY or NOT EMPTY.\n"
            + "E. End program.\n")
        userIn = input("Enter the letter that corresponds to the desired stack operation:\n" )
            

stack = createStack()
menu()
#if the program is down here that means they have entered "E"/"e" and have exited the program
print("Closing program, goodbye.")
quit()

