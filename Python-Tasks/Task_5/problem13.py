Nested Lists
https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    second_lowest = sorted({score for _, score in records})[1]

    for name in sorted(name for name, score in records if score == second_lowest):
        print(name)


Compiler Message
Success
Input (stdin)
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Expected Output
Berry
Harry
