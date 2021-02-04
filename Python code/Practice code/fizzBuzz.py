#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#
# If 'i' is a multiple of both 3 and 5, print FizzBuzz
#
# If 'i' is a multiple of 3, print Fizz
# 
# If 'i' is a multiple of 5, print Buzz
# 
# If 'i' is not a multiple of 3 or 5, print the value of 'i'

def fizzBuzz(n):

    for i in range(1, n+1):
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")

        elif (i % 3 == 0) and (i % 5 != 0):
            print("Fizz")

        elif (i % 3 != 0) and (i % 5 == 0):
            print("Buzz")

        else:
            print(i)


print(fizzBuzz(15))

