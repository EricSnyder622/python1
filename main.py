# This is a sample Python script.
import re, os

def regex1():
    #Practice regex
    workingDir = os.getcwd()
    uName = os.name
    search = input("Enter a search term: ")
    find1 = re.findall(search, workingDir)
    find2 = re.findall(search, uName)
    print(find1)
    print(find2)
    search1 = re.search(search, workingDir)
    search2 = re.search(search, uName)
    print(search1)
    print(search2)
    split1 = re.split(search, workingDir)
    split2 = re.split(search, uName)
    print(split1)
    print(split2)

if __name__ == '__main__':
    regex1()
