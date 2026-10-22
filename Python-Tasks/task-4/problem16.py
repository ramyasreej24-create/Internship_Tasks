Nested Lists
https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    lowest = min(score for name, score in students)
    second_lowest = min(score for name, score in students if score != lowest)

    for name in sorted(name for name, score in students if score == second_lowest):
        print(name)
