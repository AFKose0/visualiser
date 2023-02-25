import numpy as np

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

# write possible ranges to new text file
with open("Possibleframerange.txt", "w") as f:
    for _range in ranges:
        f.write(" ".join([str(i) for i in _range]) + "\n")