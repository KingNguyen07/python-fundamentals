# This is a comment 'and you should have a space after the number sign.
# Click the enter key after the comment to remove the squiggly yellow line.

# This statement below is a top level statement.
# It is defined outside a function and class.This specific statement
# is a function called print that takes information and displays
# that information to the terminal.
print("Hello World")

# A basic string can be defined using either single or double quotes.
print('Hello Again')


def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")


greet_user('James')
