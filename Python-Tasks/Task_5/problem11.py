Text Wrap
https://www.hackerrank.com/challenges/text-wrap/problem

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

Compiler Message
Success
Input (stdin)
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Expected Output
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
