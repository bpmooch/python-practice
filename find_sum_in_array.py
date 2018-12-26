"""
Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which 
adds to a given number.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases 
follow. Each test case consists of two lines. The first line of each test case is N and S, where N 
is the size of array and S is the sum. The second line of each test case contains N space 
separated integers denoting the array elements.

Output:
For each testcase, in a new line, print the starting and ending positions(1 indexing) 
of first such occuring subarray from the left if sum equals to subarray, else print -1.
"""

input = """2
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10
5 8
1 9 3 3 2
"""

"""
'efficient' solution I found online that doesn't seem to work for my final test case
"""
def find_number(sum_to_find, list_size, num_list):
    cur_sum = num_list[0]
    start = 0
    i = 1
    while i < list_size:
        while cur_sum > sum_to_find and start < i - 1:
            cur_sum -= num_list[start]
            start += 1

        if cur_sum == sum_to_find:
            print("better start: {} end: {}".format(start, i -1))
            return
        
        if i < list_size:
            cur_sum += num_list[i]

        i += 1

    print("-1")

def naive_find_number(sum_to_find, list_size, num_list):
    if num_list[0] == sum_to_find:
        print("1 1")
        return

    cur_start = cur_end = 0
    start_idx = end_idx = 0
    for i in range(0, list_size):
        cur_sum = 0
        for j in range(i, list_size):
            x = num_list[j]
            cur_sum += x
            if cur_sum == sum_to_find:
                print("Naive start: {} end: {}".format(i + 1, j + 1))
                print("set: {}".format(num_list[i:j + 1]))
                return
            elif cur_sum > sum_to_find:
                break
    print("-1")

if __name__ == "__main__":
    lines = input.splitlines()
    num_examples = int(lines[0])

    for i in range(1, len(lines), 2):
        size, sum_to_find = (int(x) for x in lines[i].split())
        num_list = [int(x) for x in lines[i+1].split()]
        print("Input array size: {} sum to find: {}".format(size, sum_to_find))
        print("array: {}".format(num_list))
        naive_find_number(sum_to_find, size, num_list)
        find_number(sum_to_find, size, num_list)
        print()
