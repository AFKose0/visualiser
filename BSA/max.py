# open file and read ranges
with open("framerange.txt") as f:
    ranges = [list(map(int, line.strip().split())) for line in f]

# find maximum number of numbers in a range
max_length = max(len(r) for r in ranges)

# print maximum number of numbers in a range
print(max_length)