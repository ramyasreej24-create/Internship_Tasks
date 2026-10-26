Introduction to Sets
https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    distinct = set(array)
    return round(sum(distinct) / len(distinct), 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

Compiler Message
Success
Input (stdin)
10
161 182 161 154 176 170 167 171 170 174
Expected Output
169.375
