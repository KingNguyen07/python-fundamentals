# Lab Exercise-My Application Overview
# 1. Write a function called simple(). Assign a different message to 5 variables
# and print each message.
def simple():
    message = 1
    print(message)

    message = 2
    print(message)

    message = 3
    print(message)

    message = 4
    print(message)

    message = 5
    print(message)


simple()


# Write a function simple 2(). Assign a message to a variable, then print out
# that variable. Change the message and assign it to the variable again, but
# after the 1st print statement. Print the 2nd message. Do these steps 2 more
# times. You should have 4 messages assigned to the same variable and 4 print
# functions showing the same results.


def simple2():
    message3 = "I am trying this again"
    print(message3)
    message3 = "With a fresh mindset"
    print(message3)
    message3 = "I hope this counts, even though its not labeled message :)"
    print(message3)
    message3 = "Because technically speaking, message3 is still a variable" \
               " with a print function 4 times ;)"
    print(message3)
# When you move past in defeat but still keep moving on & that eureka moment hit


simple2()


def message4(arg1):
    """User entered incorrect password information"""
    message4 = 'Wrong Passcode Entered'
    print(message4)
    print(arg1)

(arg1) = 'Use 2-Step Verification'


message4(arg1)





def message5(firstname, lastname):
    """Print their last name first if given"""
    print(lastname, firstname)


message5("James", "Nguyen")


# This was my initial answer, but it didn't fit the conditions because it has 2
# arguments.
