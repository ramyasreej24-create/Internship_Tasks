Collections.Counter()
https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

if __name__ == '__main__':
    X = int(input())
    shoes = Counter(map(int, input().split()))
    N = int(input())

    earned = 0
    for _ in range(N):
        size, price = map(int, input().split())
        if shoes[size] > 0:
            shoes[size] -= 1
            earned += price

    print(earned)

Compiler Message
Success
Input (stdin)
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
Expected Output
200
