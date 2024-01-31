#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    elem = 0
    new_list = [0 for a in range(list_length)]
    while elem < list_length:
        try:
            new_list[elem] = my_list_1[elem] / my_list_2[elem]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            elem += 1
    return new_list
