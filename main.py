import sys

def example():
    print(f"Arguments count:  {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")

def sumdigits():
    #intake args
    passedargs = len(sys.argv)
    print("\nNumber of passed args:", passedargs)
    #Display passed args
    print("\nArguments passed:", end=" ")
    for i in range(1, passedargs):
        print(sys.argv[i], end=", ")
    # Addition of numbers
    Sumargs = 0
    #argparse
    for i in range(1, passedargs):
        Sumargs += int(sys.argv[i])
    #Display sum
    print("\nSUM: ", Sumargs)

    def floatsum():
        flsum = 0.0
        num = len(sys.argv)
        for i in range(1, n):
            flsum += float(sys.argv[i])
        print("the sum is :", flsum)


if __name__ == '__main__':
    sumdigits()
    floatsum()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/