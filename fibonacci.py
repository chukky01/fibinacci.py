
def fibonacci(n):#This line defines a function called fibonacci. The function takes a number n as input.
    if n == 0:#this takes the first value which is zero
        return 0;
    elif n == 1:#this takes the second value which is one 
        return 1;
    else:
        return fibonacci(n - 1) + fibonacci(n -2)# for any number entered which is not zero or one, perform this math on it


def main():#another function
    n = int(input("Enter a number: ")) # ask the user for input and calls the fibonacci function with the number that the user entered.
    for i in range (1, n + 1): #cycle through from 1 to n +1
        print(fibonacci(i))#print the final result
    
    
if __name__ == "__main__":#calls the main program
    main()
