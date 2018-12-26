"""
Given an array C of size N-1 and given that there are numbers from 1 to N with one element missing, 
the missing number is to be found.

Input:
The first line of input contains an integer T denoting the number of test cases. For each test case 
first line contains N(size of array). The subsequent line contains N-1 array elements.

Output:
Print the missing number in array.
"""

input = """2
5
1 2 3 5
10
1 2 3 4 5 6 7 8 10
"""

def sum_find_missing(count, numbers):
    summation = (count * (count + 1)) / 2
    sum_numbers = sum(numbers)
    print("Summation Missing Number: {}".format(summation - sum_numbers))

def naive_find_missing(count, numbers):
    full_set = {x for x in range(1, count + 1)}
    print("Naive Missing Number: {}".format(full_set - numbers))

if __name__ == "__main__":
    lines = input.splitlines()
    num_examples = int(lines[0])
    for i in range(1, len(lines), 2):
        count = int(lines[i])
        numbers = {int(x) for x in lines[i+1].split()}
        print("Input missing: {} numbers: {}".format(count, numbers))
        naive_find_missing(count, numbers)
        sum_find_missing(count, numbers)
        print()
