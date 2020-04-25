"""
Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). 
Take this opportunity to practice using functions, described below.
"""




number = int(input("Enter a number to check whether it is Prime or Not Prime number: \n"))

def prime(a):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print(number, "is not a prime number")
                break
        else:
            print(number, "is a prime number")


    else:
        print(number, "is not a prime number")

prime(number)