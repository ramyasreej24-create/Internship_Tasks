Word Order
https://www.hackerrank.com/challenges/word-order/problem


from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    counts = OrderedDict()
    for _ in range(n):
        word = input().strip()
        counts[word] = counts.get(word, 0) + 1

    print(len(counts))
    print(*counts.values())


Compiler Message
Success
Input (stdin)
4
bcdef
abcdefg
bcde
bcdef
Expected Output
3
2 1 1

