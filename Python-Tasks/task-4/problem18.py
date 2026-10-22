Lists
https://www.hackerrank.com/challenges/python-lists/problem
if __name__ == '__main__':
    n = int(input())
    arr = []

    for _ in range(n):
        command, *args = input().split()

        if command == "insert":
            arr.insert(int(args[0]), int(args[1]))
        elif command == "print":
            print(arr)
        elif command == "remove":
            arr.remove(int(args[0]))
        elif command == "append":
            arr.append(int(args[0]))
        elif command == "sort":
            arr.sort()
        elif command == "pop":
            arr.pop()
        elif command == "reverse":
            arr.reverse()
