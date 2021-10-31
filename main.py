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

    def arg2():


if __name__ == '__main__':
    sumdigits()
    arg2()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/