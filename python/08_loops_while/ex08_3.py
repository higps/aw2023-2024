# 3. 
# Do the common FizzBuzz interview challenge. As this is a
# popular interview challenge this has been solved a bunch
# of times online, DON’T fall for the temptation and go
# straight to the solution!
# The challenge goes as follow:
# Write a code that prints the integer 1 to 100, but if the
# number is dividable by 3 print “Fizz”, if the number is
# dividable by 5 print “Buzz”, and if the number is dividable
# by both 5 and 3 print “FizzBuzz”. Dividable is defined as
# giving 0 in rest. Hence the result should look like this:
# 1, 2, Fizz, 4, Buzz, Fizz, 7, …,14, FizzBuzz, 16, …
# Hint: The modulo operator “%” might be useful.

for i in range(100):
    num = i+1

    Fizz = ["Fizz", num % 3]
    Buzz = ["Buzz", num % 5]

    if (Fizz[1] == 0 and Buzz[1] == 0):
        print(Fizz[0]+Buzz[0])
    elif(Fizz[1] == 0 and not Buzz[1] == 0):
        print(Fizz[0])
    elif(Buzz[1] == 0 and not Fizz[1] == 0):
        print(Buzz[0])
    else:
        print(i)