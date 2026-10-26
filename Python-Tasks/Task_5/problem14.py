Finding the percentage
https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    marks = student_marks[query_name]
    print(f"{sum(marks) / len(marks):.2f}")

Compiler Message
Success
Input (stdin)
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
Expected Output
56.00

