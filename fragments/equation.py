#
# Create on 1/12/2018
#
# Author: Sylvia
#

"""
Equation
Make a() == 1 and a() == 2 and a() == 3 as True
"""

import platform

x = (n for n in range(1, 10))

py_version = platform.python_version()[0]


def a():
    if py_version is '3':
        return x.__next__()
    return x.next()


if __name__ == '__main__':
    print(a() == 1 and a() == 2 and a() == 3)
