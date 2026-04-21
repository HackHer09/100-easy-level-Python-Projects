print("Welcome to the Multiplication Table Generator!")
n =int(input("Enter a number : "))#taking input from user 
i = 0

#code starts here
while i<=10 :
    result = n * i
    #f is format used to combine number,alphabets and special characters
    print(f"{n} x {i} = {result}")
    i+=1#increment