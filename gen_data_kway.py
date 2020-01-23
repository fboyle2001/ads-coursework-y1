import random

f = open("test_large.dat", "w+")
values = [x for x in range(100)]
random.shuffle(values)

for value in values:
    f.write(str(value) + "\n")

f.close()
