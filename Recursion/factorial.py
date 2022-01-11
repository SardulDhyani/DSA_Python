def factorial(n):
    if n<=0:
        print("Factorial not Possible")
        return
    elif n==1:
        return 1
    else:
        return n*factorial(n-1)

print("Factorial of 5 is ", factorial(0))