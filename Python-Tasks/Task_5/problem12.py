Capitalize!
https://www.hackerrank.com/challenges/capitalize/problem

def solve(s):
    return ' '.join(word.capitalize() for word in s.split(' '))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


Compiler Message
Success
Input (stdin)
hello world
Expected Output
Hello World
