def check_even_odd():
    #get user input
    num = int(input("Enter a whole number: "))

    #use if/else statement if the number is even or odd
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

# Call the function to run the program
check_even_odd(num)
