# Visualiser
A visualiser of molecules hitting a mass photometer rectangle.

**Summary so far:**

-	Created 2 initial text files from BSA.csv: (1) recorded (x,y) values on mass photometer rectangle, (2) frame indices of each coordinate.
-	Created an algorithm to find possible frame range from frame indices (range of 4 between number set + 3 number of more). 
-	Created new algorithm to check through the text output of the previous algorithm (possibleframerange.txt - OLD) and output a refined frame range (framerange.txt - NEW).
-	framerange_row.py works out the line of x,y coordinates 
-	Currently matching frame range to match up to the (x,y) coordinates and then colour code each plot based on if it was a 3rd, 4th, 5th.... 11th reading.
-	Then plotting each reading sequentially.





**Order overall:**
1. xy.txt
2. frame_indicies.txt
3. sortframe.py
4. framerange.txt
5. framerange_row.py
6. framerange_line.txt
7. overlap.py
8. ...

**Misc files:**
1. max.py
2. sort_frame_indices.py creates possibleframerange.txt - unsure what I used this for.





**Current logic:**
-	Replace each integer in “framerange.txt” with the range/row they are found in at “xy.txt” and print new data on “framerange_row.txt”
-	For each integer in the 3rd column, find the row matching the integer in “xy.txt” then copy the integers in the 1st and 2nd column on a new text file called “3rd_overlap”.
-	For the 4th-11th columns, repeat the process and produce new text files called “4th_overlap”, “5th_overlap”, “6th_overlap” etc.
-	Plot green points on the scatter graph using the 1st and 2nd columns as x and y points, respectively from “3rd_overlap.txt”.
-	Plot yellow points on the scatter graph using x and y points, respectively from “4rd_overlap.txt”.
-	Repeat this logic and change colour for 5-11 overlap.txt files.

