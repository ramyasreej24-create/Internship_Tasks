Lists
https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        command, *args = input().split()
        args = list(map(int, args))

        if command == 'print':
            print(arr)
        else:
            getattr(arr, command)(*args

                                  Compiler Message
Success
Input (stdin)
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Expected Output
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
