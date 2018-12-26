"""
Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows. The first line of each test case contains a single integer N denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
Print the maximum sum of the contiguous sub-array in a separate line for each test case.

https://en.wikipedia.org/wiki/Maximum_subarray_problem
"""

input = """2
5
1 2 3 -2 5
4
-1 -2 -3 -4
3
1 2 3
5
-4 1 -5 2 3
4
-8 -7 -3 -1
8
-2 -3 4 -1 -2 1 5 -3
9
-2 1 -3 4 -1 2 1 -5 4
"""
def kadane(num_items, items):
    max_so_far = 0
    max_here = 0
    for i in range(0, num_items):
        max_here += items[i]
        if max_here < 0:
            max_here = 0
        if max_so_far < max_here:
            max_so_far = max_here
    print("Kadane's Output sum: {}".format(max_so_far))

def kadane2(items):
    max_here = max_so_far = items[0]
    for x in items[1:]:
        # this either continues the max sub sequence
        # or starts a new sequence
        max_here = max(x, max_here + x)

        # is the current subsequence bigger than the largest
        # maximum to this point
        max_so_far = max(max_so_far, max_here)

    print("Kadane's 2: {}".format(max_so_far))

def kadane_set(items):
    max_here = max_so_far = items[0]
    max_start = max_end = 0
    cur_start = cur_end = 0
    for i in range(1, len(items)):
        x = items[i]
        if x > max_here + x:
            max_here = x
            cur_start = i
            cur_end = i
        else:
            max_here += x
            cur_end += 1

        if max_here > max_so_far:
            max_start = cur_start
            max_end = cur_end
            max_so_far = max_here

    print("Kadane's set sum: {} set: {}".format(max_so_far, items[max_start:max_end+1]))

def naive_max_set(num_items, items):
    max_start, max_end = 0, 0
    max_sum = items[0]
    for i in range(0, num_items):
        cur_sum = 0
        for j in range(i, num_items):
            cur_sum += items[j]
            if cur_sum > max_sum:
                max_start = i
                max_end = j
                max_sum = cur_sum
    print("Chris Ouptut start idx: {} end idx: {}".format(max_start, max_end))
    print("max sum: {} set: {}".format(max_sum, items[max_start:max_end+1]))

if __name__ == '__main__':
    print("Input File:\n{}".format(input))
    lines = input.splitlines()
    num_examples = int(lines[0])
    for i in range(1, len(lines) - 1, 2):
        print("Example {}".format((i + 1) / 2))
        example_len = int(lines[i])
        example_set = [int(x) for x in lines[i+1].split()]
        print("Input len: {0} set: {1}".format(example_len, example_set))
        naive_max_set(example_len, example_set)
        kadane(example_len, example_set)
        kadane2(example_set)
        kadane_set(example_set)
        print()
