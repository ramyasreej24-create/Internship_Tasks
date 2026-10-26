Symmetric Difference
https://www.hackerrank.com/challenges/symmetric-difference/problem

if __name__ == '__main__':
    m = int(input())
    a = set(map(int, input().split()))
    n = int(input())
    b = set(map(int, input().split()))

    for x in sorted(a ^ b):
        print(x)



Compiler Message
Success
Input (stdin)
4
2 4 5 9
4
2 4 11 12
Expected Output
5
9
11
12
