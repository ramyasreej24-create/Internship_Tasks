Piling Up!

https://www.hackerrank.com/challenges/piling-up/problem

T = int(input())
for _ in range(T):
    n = int(input())
    blocks = list(map(int, input().split()))

    left, right = 0, n - 1
    top = float('inf')
    ok = True

    while left <= right:
        # always take the larger of the two ends
        if blocks[left] >= blocks[right]:
            pick = blocks[left]
            left += 1
        else:
            pick = blocks[right]
            right -= 1

        if pick > top:
            ok = False
            break
        top = pick
    print("Yes" if ok else "No")
Compiler Message
Success
Input (stdin)
2
6
4 3 2 1 3 4
3
1 3 2
Expected Output
Yes
No
