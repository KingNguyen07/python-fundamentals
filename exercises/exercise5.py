# Lab Exercise - Operators

# 1. On page 78 of your book, do 5-1 of the try it yourself.
# 5-1 Conditional Statements

# Phone Object
phone = 'iPhone'
print("Is phone == 'iPhone'? I predict True.")
print(phone == 'iPhone')

phone1 = 'iPhone7'
print("Is phone == 'iPhone'? I predict False.")
print(phone1 == 'iPhone')
# Watch Object
watch = 'Apple Smart Watch'
print("Is watch == 'Apple Smart Watch'? I predict True.")
print(watch == 'Apple Smart Watch')

watch1 = 'Apple Smart Watch'
print("Is watch == 'Analog'? I predict False.")
print(watch1 == 'Analog')
# Shoe Object
shoe = 'Nike Air Jordan 1'
print("Is shoe == 'Nike Air Jordan 1'? I predict True.")
print(shoe == 'Nike Air Jordan 1')

shoe = 'Nike Air Jordan 1'
print("Is shoe == 'Nike Air Jordan 4'? I predict False.")
print(shoe == 'Nike Air Jordan 4')
# Console Object
console = 'Playstation 5'
print("Is console == 'Playstation 5'? I predict True.")
print(console == 'Playstation 5')

console = 'Playstation 5'
print("Is console == 'Xbox'? I predict False.")
print(console == 'Xbox')
# Video Game Object
game = 'Dark Souls'
print("Is game == 'Dark Souls'? I predict True.")
print(game == 'Dark Souls')


game = 'Dark Souls 3'
print("\nIs game == 'Dark Souls'? I predict False.")
print(game == 'Dark Souls')


# 5-2

# Tests for equality and inequality methods with strings.
Jack = 24
drinking_age = 21
adulthood = 18
print(f" Is {Jack} >= {drinking_age}? I predict True.")
print(Jack >= drinking_age)

print(f" Is {Jack} == {drinking_age}? I predict False.")
print(Jack == drinking_age)


# Tests using the lower method
var1 = 'UPPERCASE'
var2 = 'uppercase'
print(f" Is {var2} == {var1.lower()}? I predict True.")
print(var2 == var1.lower())

print(f" Is {var1} == {var1.lower()}? I predict False.")
print(var1 == var1.lower())


# Numerical Tests
# equal & not equal
def factual_equal(value1, value2):
    result_equal = value1 == value2
    print(result_equal)
    print(f"Is {value1} == {value2}? I predict True.")


factual_equal(8, 8.0)


def nonfactual_equal(value1, value2):
    result_equal = value1 == value2
    print(result_equal)
    print(f"Is {value1} == {value2}? I predict False.")


nonfactual_equal(12, 30)


def factual_unequal(value1, value2):
    result = value1 != value2
    print(result)
    print(f"Is {value1} != {value2} ? I predict True.")


factual_unequal(8, 5)


def nonfactual_unequal(value1, value2):
    result = value1 != value2
    print(result)
    print(f"Is {value1} != {value2} ? I predict False.")


nonfactual_unequal(12, 12)
# Tests using the and keyword and the or keyword
var3 = 24
var4 = 25
# Greater Than or Equal To or Less Than or Equal To
var5 = 26
var6 = 26
var7 = 28
var8 = 25


def factual_great_less_equal():
    result_great = var5 >= var6
    result_less = var6 <= var5
    print(result_great)
    print(result_less)
    print(f"Is {var5} >= {var6}? I predict True.")
    print(f"Is {var6} <= {var5}? I predict True.")


factual_great_less_equal()


def nonfactual_great_less_equal():
    result_great = var5 >= var6
    result_less = var6 <= var5
    print(result_great)
    print(result_less)
    print(f"Is {var8} >= {var7}? I predict False.")
    print(f"Is {var7} <= {var8}? I predict False.")


nonfactual_great_less_equal()
# and


def factual_and():
    result = var4 > 24 and var3 > 23
    print(result)
    print(f"Is {var4} > {24} and {var3} > {23}? I predict True.")
    print(var4 > 24 and var3 > 23)


factual_and()


def nonfactual_and():
    result = var4 > 26 and var3 > 25
    print(result)
    print(f"Is {var4} > {26} and {var3} > 25? I predict False.")
    print(var4 > 26 and var3 > 25)


nonfactual_and()
# or


def factual_or():
    result = var4 > var3 or var3 < var4
    print(result)
    print(f"Is {var4} > {var3} or {var3} < {var4}? I predict True.")
    print(var4 > var3 or var3 < var4)


factual_or()


def nonfactual_or():
    result = var3 > var4 or var4 < var3
    print(result)
    print(f"Is {var3} > {var4} or {var4} < {var3}? I predict False.")
    print(var3 > var4 or var4 < var3)


nonfactual_or()


# Test whether an item is in a list
Foxtrot = "What's your favorite color?"


def factual_in(arg):
    result = arg in Foxtrot
    print(f"Is {'your'} in {Foxtrot} ? I predict True.")
    print(result)


factual_in('your')


def nonfactual_in(arg):
    result = arg in Foxtrot
    print(f"Is {'Neon Green'} in {Foxtrot} ? I predict False.")
    print(result)


nonfactual_in('Neon Green')


# Test whether an item is not in a list
def factual_not_in(arg):
    result = arg not in Foxtrot
    print(f"Is {'Neon Green'} not in {Foxtrot}? I predict True.")
    print(result)


factual_not_in('Neon Green')


def nonfactual_not_in(arg):
    result = arg not in Foxtrot
    print(f"Is {'your'} not in {Foxtrot}? I predict False.")
    print(result)


nonfactual_not_in('your')


# 3










