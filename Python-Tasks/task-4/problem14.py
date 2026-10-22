Set .add()

https://www.hackerrank.com/challenges/py-set-add/problem
if __name__ == '__main__':
    n = int(input())
    stamps = []

    for _ in range(n):
        country = input()
        if country not in stamps:
            stamps.append(country)

    print(len(stamps))
