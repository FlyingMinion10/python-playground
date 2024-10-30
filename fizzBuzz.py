# FIZZ BUZZ

print ("Welcome to the Fizz-Buzz Game Solution")

n = 0

for i in range (100):
    n += 1

    if n%3 == 0 and n%5 == 0:
        print ("FizzBuzz")
    elif n%3 == 0:
        print ("Fizz")
    elif n%5 == 0:
        print ("Buzz")
    else:
        print (n)