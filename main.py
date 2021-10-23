import datetime

def datetimeExample():
    now = datetime.datetime.now()
    print(now.year, "\n", now.strftime("%A"))
    now = datetime.datetime(2010, 6, 22)
    print(now.year, "\n", now.strftime("%A"))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    datetimeExample()
