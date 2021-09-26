# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def assignment2():
    # get users name
    name = input("Tell me your name:")
    print(f'Hello {name}')

    # enter a number and multiply by itself
    x = int(input("Enter a number: "))
    print(x * x)

    #enter a word and calculate letter number
    word = input("Please enter a word: ")
    print("The number of letters in the word is: ", len(word))
import random
def assignment3():
    #Print 2-d array
    rows = 9
    col = 9
    grid = [[0, 0, 0, 0, 0]]
    for i in range(rows):
        print("".join('.' for j in range(col)))

    #Coin Flip
    coin = int(input("Enter a value 1 or 0: "))
    flip = random.randint(0, 1)
    if(coin == flip):
        print("You win!")
    else:
        print("You lose!")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    #assignment2()
    assignment3()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
