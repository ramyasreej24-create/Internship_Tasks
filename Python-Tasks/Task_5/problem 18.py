The Minion Game
https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    vowels = 'AEIOU'
    n = len(string)
    kevin = stuart = 0

    for i, ch in enumerate(string):
        if ch in vowels:
            kevin += n - i
        else:
            stuart += n - i

    if kevin > stuart:
        print('Kevin', kevin)
    elif stuart > kevin:
        print('Stuart', stuart)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)

Compiler Message
Success
Input (stdin)
BANANA
Expected Output
Stuart 12
