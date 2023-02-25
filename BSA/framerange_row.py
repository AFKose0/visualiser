# 1. Read “xy.txt”.
with open('xy.txt') as f:
    lines = f.readlines()

# Note the 3rd column data in “xy.txt” as "frame".
frame_data = [line.split()[2] for line in lines]

# 2. Copy data “framerange.txt” and print new data on “framerange_line.txt”.
with open('framerange.txt') as f:
    frame_range = f.readlines()

with open('framerange_line.txt', 'w') as f:
    f.writelines(frame_range)

# 3. Match the data in “framerange_line.txt” to "frame" in “xy.txt”.
# Replace the first line in “framerange_line.txt” with the number of the line the "frame" is found in the “xy.txt” file.
with open('framerange_line.txt') as f:
    frame_range = f.readlines()

with open('framerange_line.txt', 'w') as f:
    for frame in frame_range:
        # Split the string on spaces and convert each number to an integer.
        frame_numbers = [int(x) for x in frame.split()]

        # Find the index of each number in frame_data.
        line_numbers = [frame_data.index(str(x)) for x in frame_numbers]

        # Write the line numbers to the output file.
        f.write(' '.join(str(x) for x in line_numbers) + '\n')

# 4. Replace all lines in “framerange_line.txt” with the number of the line the "frame" is found in the “xy.txt” file.
# This step is not necessary, since step 3 already replaces all lines in the file.

# 5. Print “framerange_line.txt”.
with open('framerange_line.txt') as f:
    print(f.read())
