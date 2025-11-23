#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # Skip elements that are not integers
            continue
        except IndexError:
            # Stop if we try to access beyond the list
            break
    print()
    return count
