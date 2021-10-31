
def user_input():
    user_string = input("Enter any string: ")
    return user_string

def mod_text():
    orig_string = user_input()
    temp_string = original_string.split()
    for index, letter in enumerate(orig_string, 1):
        print(index, ':', letter)
    print(temp_string)
    last_char = orig_string[-1]
    print(last_char)
    without_last = orig_string[:-1]
    print(without_last)

if __name__ == '__main__':
  mod_text()