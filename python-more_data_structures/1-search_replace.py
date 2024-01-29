#!/bin/usr/python3
def search_replace(my_list, search, replace):
    new_list = []
    for ar in my_list:
        if ar == search:
            new_list.append(replace)
        else:
            new_list.append(ar)
    return new_list
