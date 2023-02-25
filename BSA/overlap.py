# Open the "framerange_line.txt" file
with open("framerange_line.txt") as framerange_file:
    # Read each line of the file and split it into columns
    for line in framerange_file:
        columns = line.split()
        # Get the 3rd column of the current line
        third_column = int(columns[2])
        
        # Open the "xy.txt" file
        with open("xy.txt") as xy_file:
            # Read each line of the file and split it into columns
            for xy_line in xy_file:
                xy_columns = xy_line.split()
                # If the first column of the current "xy.txt" line is equal
                # to the number from the 3rd column of "framerange_line.txt",
                # write the first two columns of the "xy.txt" line to the
                # "3rd_overlap" file
                if int(xy_columns[0]) == third_column:
                    with open("3rd_overlap.txt", "a") as overlap_file:
                        overlap_file.write(" ".join(xy_columns[:2]))
                        overlap_file.write("\n")
