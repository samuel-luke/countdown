# Returns every permutation of given array
def heapPermutation(a, size, n, permutations): 
    # if size becomes 1 then adds the permutation
    if (size == 1):
        array = []
        for letter in a:
            array.append(letter)
        permutations.append(array)
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

# Finds and prints every dictionary word in set of letters
def countdown(given):
    permutations = heapPermutation(given, len(given), len(given), [])
    
    d = set()
    file = open("words_alpha.txt", "r")
    for word in file:
        d.add(word.strip().lower())
        
    words = []
    for line in permutations:
        for i in range(0, len(line) + 1):
            string = ""
            for j in range(0, i):
                string += line[j]
            if string in d:
                if i >= 3 and string not in words:
                    words.append(string)
        
    words = sorted(words, key=len)
    for word in words:
        print(word)
    print("Words Found:", len(words))
             

# Command Line Input
def getUserInput():
    array = []
    print("--- Countdown ---")
    print("Enter nine letters")
    userInput = list(str(input(": ")).strip())
    for letter in userInput:
        if letter.isalpha():
            array.append(letter)
    return array

def main():
    # Test Cases
    # array = ['u', 'a', 'g', 's', 't', 'e', 'n', 'r', 'o']                 
    # array = ['s', 'o', 'y', 'a', 'p', 'i', 'm', 't', 'r']    
    # array = ['a', 'o', 'g', 'l', 'r', 'f', 'i', 'p', 'e']    
    # array = ['n', 'i', 'c', 'e', 's', 'h', 'i', 't', 's']  
    
    # Command Line Input
    array = getUserInput()  
    
    if len(array) < 9:
        print("Warning: Only", len(array), "letters were entered")
    elif len(array) > 9:
        print("Warning:", len(array), "letters were entered")
    if len(array) == 1:
        print("No Words Found")
    else:
        countdown(array)


if __name__ == "__main__":
    main()