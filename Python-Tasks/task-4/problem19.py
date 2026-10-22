Collections.Counter()
https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

if __name__ == '__main__':
    x = int(input())
    shoes = Counter(map(int, input().split()))
    n = int(input())
    earned = 0

    for _ in range(n):
        size, price = map(int, input().split())
        if shoes[size] > 0:
            earned += price
            shoes[size] -= 1

    print(earned)
