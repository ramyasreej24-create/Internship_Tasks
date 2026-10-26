Merge the Tools!

https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
     for i in range(0, len(string), k):
        chunk = string[i:i + k]
        print(''.join(dict.fromkeys(chunk)))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

Compiler Message
Success
Input (stdin)
AABCAAADA
3
Expected Output
AB
CA
AD
