#for value in range(1,5):
#    print (value)
#In the example in the previous section, we simply printed out a series of
# numbers. We can use list() to convert that same set of numbers into a list:
#numbers=list(range(1,6))
#print (numbers)
# If you pass a third argument to range(), Python uses that value
# as a step size when generating numbers
even_numbers = list(range(2, 11, 2))
print("he last three items in the list are",even_numbers[-3:])
print("item from the middle of the list are:",even_numbers[2:3])
print("The first three items in the list are:",even_numbers[:3])

#You can create almost any set of numbers you want to using the range()
# function. For example, consider how you might make a list of the first 10
# square numbers (that is, the square of each integer from 1 through 10). In
# Python, two asterisks (**) represent exponents. Here’s how you might put
# the first 10 square numbers into a list:






