# load frame indices from text file
with open("frame_indices.txt") as f:
    frame_indices = [int(i.strip()) for i in f]

# find all possible ranges of integers in frame_indices
ranges = []
for i in range(len(frame_indices)):
    # initialize range with first integer
    _range = [frame_indices[i]]

    # iterate over remaining integers in frame_indices
    for j in range(i + 1, len(frame_indices)):
        # add integer to range if difference is 4 or less
        if frame_indices[j] - _range[0] <= 4:
            _range.append(frame_indices[j])
        else:
            break

    # only consider ranges with 3 or more integers
    if len(_range) >= 3:
        ranges.append(_range)

# iterate over ranges
i = 0
while i < len(ranges):
    # check if any of the numbers in the current range are present in any of the other ranges
    current_range = ranges[i]
    ranges_to_remove = []
    for j in range(len(ranges)):
        if i != j:
            other_range = ranges[j]
            for number in current_range:
                if number in other_range:
                    ranges_to_remove.append(other_range)
                    break

    # remove ranges that were identified for removal
    for range_to_remove in ranges_to_remove:
        ranges.remove(range_to_remove)

    # move to next range
    i += 1

# write remaining ranges to new text file
with open("framerange.txt", "w") as f:
    for _range in ranges:
        f.write(" ".join([str(i) for i in _range]) + "\n")
