
def greet_user(username):
    ''' username in the definition of greet_user() is an example of a
parameter, a piece of information the function needs to do its job'''

    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('Tito')

'''The value
'tito' in greet_user('tito') is an example of an argument. An argument
is a piece of information that’s passed from a function call to a function.
When we call the function, we place the value we want the function to work
with in parentheses. In this case the argument 'jesse' was passed to the
function greet_user(), and the value was assigned to the parameter username'''