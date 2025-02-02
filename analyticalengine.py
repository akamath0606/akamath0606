#function for getting which operation the user would like to do
def getOp():
    x = ""
    while(x != "0" and x != "1"): #error checking loop
        x = input("Insert a punch card to select the operation you would like to carry out:\n0. Factorial\n1. Fibonacci\n")
        if(x != "0" and x != "1"): #error checking message
            print("Invalid operation choice. Please select either 0 or 1")
    print("Staching choice in the store...")
    return x

#function for getting whether or not the user would like to show intermediate calculation steps
def getInter():
    x = ""
    while(x != "0" and x != "1"): #error checking loop
        x = input("Insert a punch card to select whether or not you would like to show intermediate calculation steps: \n0. Yes\n1. No\n")
        if(x != "0" and x != "1"): #error checking message
            print("Invalid operation choice. Please select either 0 or 1")
    print("Staching choice in the store...")
    return x

#function for retrieving the argument the user would like to be used in calculating factorial or fibonacci
def getNumIn():
    inp = ""
    print("Leave holes in the punch card for the binary digits you would like present")
    print("Example: 11111110 -> 1 in decimal") #punch card for input of factorial number, mimics binary with holes
    while(len(inp) != 8):
        print("")
        inp = input("Please enter the punch card for the number you would like passed to the calculation:\nNumber to calculate the factorial of or the desired number in the Fibonacci Sequence\n")
        if(len(inp) != 8):
            print("Error: punch card must contain 8 holes")
    
    inp = list(inp) #change to list for easier manipulation

    #flip all digits of punch card to form binary number from input
    for n in range(8):
        if(inp[n] == "0"):
            inp[n] = "1"
        elif(inp[n] == "1"):
            inp[n] = "0"
    
    inp = "".join(inp) #join all elements of the list back into a string

    sum = 0 #calculate decimal equivalent of punch card entry
    for n in range(8):
        dig = inp[n]
        dig = int(dig)
        sum += dig * pow(2, 7-n)

    print("Decimal Number Entered: " + str(sum))
    print("Staching entered number in the store...")
    return sum

#function for calculating factorials using only addition, as the analytical 
def calcFact(num, option):
    iter = num #numbers we will be multiplying by down to 1, excluding num
    ret = 1 #start with num as return, begin multiplying with num - 1, aka iter
    while(iter > 0):
        ret *= iter
        if(option == "0" and iter != 1):
            print("Iteration " + str(num - iter + 1) + ": " + str(ret))
        iter -= 1
    
    print("Final Calculation: " + str(num) + "! = " + str(ret))
    return ret

def calcFib(num, option):
    if(num < 1): #error check for numbers < 1
        print("Error in the mill. Number for calculation retrieved from the store was less than 1.")
        return
    sum = 0
    iter = 2
    first = 0
    second = 1
    if(num == 1):
        print("Fibonacci Sequence #1: 0")
    elif(num == 2):
        print("Fibonacci Sequence #2: 1")
    else:
        if(option == "0"): #print intermediate results
            print("Iteration 1: 0")
            print("Iteration 2: 1")
        while(iter < num): #while number of iterations less than desired 
            sum = first + second
            first = second
            second = sum
            iter += 1
            if(option == "0" and iter != num): #print intermediate calculations if desired
                print("Iteration " + str(iter) + ": " + str(sum))

    print("Final Calculation for Fibonacci Sequence #" + str(num) + ": " + str(sum)) #print final calculation no matter what the intermediate choice was
    return sum 



#instructions to be run every execution...
choice = getOp() #get operation to calculate, stored in "store"
inter = getInter() #get whether or not to show intermediate steps, stored in "store"
i = getNumIn() #get number to be used for calculation, stored in "store"
if(choice == "0"):
    calcFact(i, inter) #make calculation, uses "mill" to crunch numbers, then uses printer to output answer
elif(choice == "1"):
    calcFib(i, inter) #make calculation, uses "mill" to crunch numbers, then uses printer to output answer