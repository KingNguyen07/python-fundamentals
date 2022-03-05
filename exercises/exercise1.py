print("Hello World")

print('Hello Again')
# Make a typo somewhere in the line and run the program again.
# print("Hello World")

# print('Hello Again']

# Question 1A/1B : Can you make a typo that generates an error? Can you make sense of the error message?
# Answer 1A      : Yes. By not matching parenthesis in ('Hello Again'] I generated the error message,
# "SyntaxError: closing parenthesis ']' does not match opening parenthesis '[' ".
# Answer 1B      : Yes, not matching the opening and closing parenthesis causes a string to be incomplete.

# print("Hello World")

# print('Helo Again')
# Question 2A/2B :Can you make a typo that doesn't generate an error? Why do you think it didn't make an error?
# Answer 2A      :Yes. By misspelling "Helo" in ('Helo Again') it didn't generate an error message.
# Answer 2B      :I believe it didn't generate an error message because the typo was a misspelling within a
# print string, so regardless of the spelling, it will respond back the exact strings spelling.

# Zen of Python
# If you input "import this" into a Python Terminal Session it will output back too you,
# The Zen of Python, by Tim Peters
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!

# Book Exercise Pg131 8-1 Message
def display_message():
    """Display the message """
    print("In this chapter we learned how to define a function ,pass information to one, and set arguments and "
          "parameters within a function.")
display_message()


# Book Exercise pg131 8-2 Favorite Book
def favorite_book(name):
    """Display favorite book"""
    print(f'One of my favorite books is {name.title()}!')


favorite_book("A Game Of Thrones- George R.R Martin")













