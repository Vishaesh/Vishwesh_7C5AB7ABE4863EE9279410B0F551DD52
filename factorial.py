# vishwesh.M.S
# Function for factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
      
num = int(input("Enter a number: "))

if num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", factorial(num))

print("Thankyou!!!!")