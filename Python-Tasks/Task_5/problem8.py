Set .add()
https://www.hackerrank.com/challenges/py-set-add/problem


if __name__ == '__main__':
    n = int(input())
    countries = set()
    for _ in range(n):
        countries.add(input())
    print(len(countries))

Compiler Message
Success
Input (stdin)
7
UK
China
USA
France
New Zealand
UK
France
Expected Output
5
