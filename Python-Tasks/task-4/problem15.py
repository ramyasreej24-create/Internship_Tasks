Word Order
https://www.hackerrank.com/challenges/word-order/problem
import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    counts = {}

    for _ in range(n):
        word = sys.stdin.readline().strip()
        counts[word] = counts.get(word, 0) + 1

    print(len(counts))
    print(*counts.values())
