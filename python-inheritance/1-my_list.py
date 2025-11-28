#!/usr/bin/python3
""" this is path
it is important
"""


class MyList(list):
    ""This is class and this class have  a inherits"""

    def print_sorted(self):
    """"
        Siyahını artan sıralama qaydasında çap edir.
        Orijinal siyahıya eyisiklik etmir.
    """

        print(sorted(self))
