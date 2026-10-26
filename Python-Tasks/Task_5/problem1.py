Find the Runner-Up Score!
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(sorted(set(arr))[-2])



Compiler Message
Success
Input (stdin)
5
2 3 6 6 5
Expected Output
5
