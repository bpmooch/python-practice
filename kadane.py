input = """2
5
1 2 3 -2 5
4
-1 -2 -3 -4
3
1 2 3
"""

def find_max_sum(num_items, items):
    max_start, max_end = 0, 0
    max_sum = 0
    for i in range(0, num_items):
        last_sum = 0
        for j in range(i, num_items):
            cur_sum = last_sum + items[j]
            if cur_sum < last_sum:
                if last_sum > max_sum:
                    max_start = i
                    max_end = i + j
                    max_sum = last_sum
                break
            last_sum = cur_sum
    print("Ouptut start idx: {} end idx: {}".format(max_start, max_end))
    print("max sum: {} set: {}\n".format(max_sum, items[max_start:max_end]))

if __name__ == '__main__':
    print("Input File:\n{}".format(input))
    lines = input.splitlines()
    num_examples = int(lines[0])
    for i in range(1, len(lines) - 1, 2):
        print("Example {}".format(i + 1))
        example_len = int(lines[i])
        example_set = [int(x) for x in lines[i+1].split()]
        print("Input len: {0} set: {1}".format(example_len, example_set))
        find_max_sum(example_len, example_set)
