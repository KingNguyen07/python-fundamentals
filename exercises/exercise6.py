# Lab Exercise - Control Flow

# Page 84 5-3 Alien Colors #1
alien_color = 'green'
if alien_color == 'green':
    print('You just earned 5 points!')


failed_alien_color = 'green'
if failed_alien_color == 'red':
    print('You just earned 5 points!')

# Page 84 5-3 Alien Colors #2
if_alien_color1 = 'yellow'
if if_alien_color1 == 'green':
    print('You just earned 5 points!')
else:
    print('You just earned 10 points!')


else_alien_color2 = 'yellow'
if else_alien_color2 == 'green':
    print('You just earned 5 points!')
else:
    print('You just earned 10 points!')


# Page 84 5-5 Alien Colors #3
alien_color_green = 'green'
if alien_color_green == 'green':
    print('You just earned 5 points!')
elif alien_color_green == 'yellow':
    print('You just earned 10 points!')
else:
    print('You just earned 15 points!')


alien_color_yellow = 'yellow'
if alien_color_yellow == 'green':
    print('You just earned 5 points!')
elif alien_color_yellow == 'yellow':
    print('You just earned 10 points!')
else:
    print('You just earned 15 points!')


alien_color_red = 'red'
if alien_color_red == 'green':
    print('You just earned 5 points!')
elif alien_color_red == 'yellow':
    print('You just earned 10 points!')
else:
    print('You just earned 15 points!')


# Page 84 5-6 Stages of Life
age = 18
if age < 2:
    print('You are a baby')
elif 2 <= age < 4:
    print('You are a toddler')
elif 4 <= age < 13:
    print('You are a kid')
elif 13 <= age < 20:
    print('You are a teenager')
elif 20 <= age < 65:
    print('You are an adult')
else:
    print('You are an elder')


# Number 5


def boolean_check(arg2):
    print(bool(arg2 == 12))


boolean_check(10)
# Arg2's boolean test results came back false.
