'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

from collections import Counter

def arrange_stud(students, capacity):
    lengths = [len(x) for x in students]
    counts = Counter(lengths)
    for count in counts.values():
        if count != capacity:
            return 'Not possible'
    return 'Possible'
    
# Write your code here
if __name__ == "__main__":
    testcases = int(input())
    for _ in range(testcases):
        n, k = list(map(int, input().rstrip().split()))
        people = []
        for _ in range(n):
            people.append(str(input()))
        print(arrange_stud(people, k))
    return 
