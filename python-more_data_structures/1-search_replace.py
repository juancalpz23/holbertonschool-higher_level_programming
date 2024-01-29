#!/bin/usr/python3
def search_replace(my_list, search, replace):
    new_list = []
    for arr in my_list:
        if arr == search:
            new_list.append(replace)
        else:
            new_list.append(arr)
    return new_list