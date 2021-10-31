
def breakup1():
    user_input = input("Please enter a sentence: ")
    x = user_input.split()
    print('\n'.join(map(str, x)))

def breakup2():
    user_input = input("Please enter a sentence: ")
    x = user_input.split()
    print(*x, sep = "\n")

if __name__ == '__main__':
    breakup1()
    breakup2()