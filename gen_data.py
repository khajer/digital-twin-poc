import random


def simple_func(x, y, z):
    return (x+y)*2-z

def main():
    i = 500
    while i > 0:
        x = random.random()
        y = random.random()
        z = random.random()

        # print(x, ",", y,",", z,",", simple_func(x, y, z))
        print(f"{x}, {y}, {z}, {simple_func(x, y, z)}")
        i -= 1


main()
