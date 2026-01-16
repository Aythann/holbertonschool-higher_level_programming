#!/usr/bin/python3
def uppercase(str):
    upper_str = ""
    for char in str:
        ascii_code = ord(char)
        if 97 <= ascii_code <= 122:
            upper_str += chr(ascii_code - 32)
        else:
            upper_str += char
    print("{}".format(upper_str))
