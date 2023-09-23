print("Python")
#Python
print("\tPython")
#Python
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")
#Python can look for extra whitespace on the right and left sides of a
# string. To ensure that no whitespace exists at the right end of a string, use
# the rstrip() method.
favorite_language = 'python '
print(favorite_language)
favorite_language.rstrip()
print(favorite_language)

favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(favorite_language)