Mutations
https://www.hackerrank.com/challenges/python-mutations/problem


def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)



Compiler Message
Success
Input (stdin)
abracadabra
5 k
Expected Output
abrackdabra
