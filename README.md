# Visualiser
A visualiser of molecules hitting the mass photometer

Summary so far:

-	We created 3 text files containing the x, y and frame indices.
-	Created an algorithm to find possible frame range from all frames text data (range of 4 between number set + 3 number of more).
-	Created another algorithm to check through the text output of the previous algorithm and output another text file with a refined frame range.
-	Now I use frame range to match up to the (x,y) coordinates and then colour code each plot based on if it was a 3rd, 4th, 5th.... 11th reading in a range

-	Replace each integer in “framerange.txt” with the range/row they are found in at “xy.txt” and print new data on “framerange_row.txt”
-	For each integer in the 3rd column, find the row matching the integer in “xy.txt” then copy the integers in the 1st and 2nd column on a new text file called “3rd_overlap”.
-	For the 4th-11th columns, repeat the process and produce new text files called “4th_overlap”, “5th_overlap”, “6th_overlap” etc.
-	Plot green points on the scatter graph using the 1st and 2nd columns as x and y points, respectively from “3rd_overlap.txt”.
-	Plot yellow points on the scatter graph using x and y points, respectively from “4rd_overlap.txt”.
-	Repeat this logic and change colour for 5-11 overlap.txt files.
