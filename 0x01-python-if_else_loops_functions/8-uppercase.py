#!/usr/bin/python3
def uppercase(str):
    result = ''
    '''prints a string in uppercase followed by a new line'''
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            result += chr(ord(char) - 32)
            print("{}".format(chr(int(str))))
        return result
    else:
        print("{}".format(chr(str)))
