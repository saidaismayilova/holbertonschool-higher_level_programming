#!/usr/bin/python3
def new_in_list(my_list, idx, element):
   if idx < 0 or if idx >= len(my_list):
        return my_list.copy()
    new_line = my_list.copy()
    new_line[idx] = element
    return  new_line
