

def piglatin():
    # cache for pigwords
    yay = "yay"
    ay = "ay"
    cons = ('B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z')
    vow = ('A', 'E', 'I', 'O', 'U')
    # cluster = ('CH','GR')
    pig_string = ''
    #input and split string
    orig_string = input("Enter any string: ")
    words = orig_string.split()


    for orig_word in words:
        print(orig_word)
        #grab first letter from word
        first_char = orig_word[0]
        first_char = str(first_char)
        first_char = first_char.upper()

        #create piglatin string
        if first_char in cons:
            len_word = len(orig_word)
            rem_first_char = orig_word[1:len_word]
            pig_latin = rem_first_char+first_char+ay
            pig_string = pig_string+' '+pig_latin
        elif first_char in vow:
            pig_latin = orig_word+yay
            pig_string = pig_string+ ' '+pig_latin
        else:
            print(' ')

    print(pig_string)

if __name__ == '__main__':
    piglatin()