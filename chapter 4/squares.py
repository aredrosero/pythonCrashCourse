
squares = []
for values in range(1,11):
    square= values **2
    squares.append(square)

print(squares)

#To write this code more concisely, omit the temporary variable square
#and append each new value directly to the list:
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

squares = [value**2 for value in range(1, 11)]
print(squares)
