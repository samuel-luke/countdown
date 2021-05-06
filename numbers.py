import time

def calculate(target, array):
    global traceback
    if array[0] == target:
        traceback.insert(0, " = %s" % array[0])
        return True
    
    if len(array) <= 2:
        return False
    
    add = calculate(target, [array[0] + array[1]] + array[2:])
    if add:
        traceback.insert(0, "+")
    
    subtract = calculate(target, [array[0] - array[1]] + array[2:])
    if subtract:
        traceback.insert(0, "-")
    
    multiply = calculate(target, [array[0] * array[1]] + array[2:])
    if multiply:
        traceback.insert(0, "*")
    
    divide = False
    if (array[0] / array[1]).is_integer():
        divide = calculate(target, [int(array[0] / array[1])] + array[2:])
        if divide:
            traceback.insert(0, "/")
    
    return subtract or add or multiply or divide


def heapPermutation(a, size, n, permutations): 
    # if size becomes 1 then adds the permutation
    if (size == 1): 
        permutations.append([a[0], a[1], a[2], a[3], a[4], a[5]])
        return
  
    for i in range(size): 
        heapPermutation(a, size - 1, n, permutations); 
  
        # if size is odd, swap first and last element
        # else If size is even, swap ith and last element 
        if size&1: 
            a[0], a[size-1] = a[size-1], a[0] 
        else: 
            a[i], a[size-1] = a[size-1], a[i]
    return permutations


traceback = []
def countdown(given, target):
    global traceback
    permutations = heapPermutation(given, len(given), len(given), [])
    output = []

    for line in permutations:
        if calculate(target, line):
            string = '(' * (len(traceback) - 2)
            string += "%s%s" % (line[0], traceback[0])
            for i in range(1, len(traceback)-1):
                string += "%s)%s" % (line[i], traceback[i])
            string += "%s%s" % (line[len(traceback)-1], traceback[-1])
            
            if traceback[0] == "+" or traceback[0] == "*":
                if line[1] > line[0]:
                    string = string.replace("%s%s%s" % (line[0], traceback[0], line[1]),"%s%s%s" % (line[1], traceback[0], line[0]))
            
            if traceback[1] == "*" and traceback[0] == "*":
                array = sorted(line[:3], reverse=True)
                string = "(" + str(array[0]) + "*" + str(array[1]) + "*" + str(array[2]) + ")" + string[11:]
               
            if string not in output:
                output.append(string)
            
            traceback = []
            
    output = sorted(output,key=len,reverse=True)
    return output
            


def main():
    ## Test Cases
    # array = [25, 100, 4, 1, 1, 5]
    # goal = 599 

    # array = [25, 100, 5, 2, 7, 10]
    # goal = 585

    # array = [50, 75, 9, 6, 6, 5]
    # goal = 949

    # array = [75, 25, 50, 100, 7, 4]
    # goal = 453

    # array = [100, 50, 1, 6, 5, 10]
    # goal = 811

    #Command Line Input
    array = []
    print("--- Countdown ---")
    print("Enter numbers, one per line")
    array.append(int(input(": ")))
    array.append(int(input(": ")))
    array.append(int(input(": ")))
    array.append(int(input(": ")))
    array.append(int(input(": ")))
    array.append(int(input(": ")))
    print("Enter the goal")
    goal = int(input(": "))

    # Timing
    # startTime = int(round(time.time() * 1000))
    # output = countdown(array, goal)
    # endTime = int(round(time.time() * 1000))
    # print("Time:", endTime-startTime, "ms")
    
    # Evaluates values close to goal until solution is found
    index = 2
    output = []
    while not output:
        output = countdown(array, goal)
        if not output:
            print("Unable to find solution for", goal, " Trying next value...")
            if index % 2 == 0:
                goal = goal-index//2
            else:
                goal = goal+index//2
            index += 1
            
    for line in output:
        print(line)
    print("Total Solutions:", len(output))
            
    
if __name__ == "__main__":
    main()
