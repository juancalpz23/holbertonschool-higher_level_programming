#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if ord('a') <= ord(x) <= ord('z'):
            x = chr(ord(x) + (ord('A') - ord('a')))
        print("{:s}".format(x), end='')
    print('')
