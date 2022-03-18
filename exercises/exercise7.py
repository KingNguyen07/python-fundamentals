# Lab Exercise - Looping

# Page 60 4-3 Counting to Twenty
def for1_loop():
    values = list(range(1, 21))
    for value in values:
        print(value)


for1_loop()


# Page 60 4-6 Odd Numbers
def for2_loop():
    values = list(range(1, 21, 2))
    for value in values:
        print(value)


for2_loop()


# Page 60 4-7 Threes
def for3_loop():
    values = list(range(3, 33, 3))
    for value in values:
        print(value)


for3_loop()


# Page 60 4-8 Cubes
def for4_loop():
    values3 = []
    for value1 in range(1, 11):
        value3 = value1 ** 3
        values3.append(value3)
    for value3 in values3:
        print(value3)


for4_loop()



for4_loop()