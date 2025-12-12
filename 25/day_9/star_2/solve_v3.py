"""
This solution took a while to find, but it is much simpler.
The idea is that any rectangle with an edge passing through it is guaranteed to be
invalid (as I am writing this, I realize that this is untrue in very specific cases
but hey it worked! I might ammend this code later on as this was the hardest puzzle 
of this year so far and was fun to do).
So if we had a way of detecting these rectangles with an edge passing through them,
all we would need to do is determine if the rectangle is in the shape or outside of it
in a weird cut going into the shape (ex: _|¯¯¯|_).

To do all this, we stop filling the matrix. This makes the edges stand out AND saves the
time of filling the matrix, win-win.
We can then use a sum over the interior of the rectangle, excluding the edges, to determine
if an edge passes there. The edges do not have to be checked as they are necessarily in the
shape if there are no edges in the interior.

To do the second step, we take any point in the rectangle and do a raycast and count the 
edges we meet. I do this using another sum. If the sum is even, we are outside of the shape.
I do a diagonal raycast to avoid hitting horizontal/vertical edges on my path which throw
off my math.

As I mention earlier, there is a small error in this, but it could be fixed with one step of 
pre-processing where we only draw the outermost edge of the shape.

After a bit of extra work, the process is 60 times faster, taking 40 seconds total.
"""

import time
import numpy as np
from math import prod
from scipy.sparse import lil_matrix

file_root = "25/day_9/star_2"

with open(f"{file_root}/input.txt") as f:
    corners = [np.array([int(iter) for iter in line.rstrip().split(',')]) for line in f.readlines()]

start = time.time()

# Initialize the smallest matrix possible, adjust corners to be in new referential
lowest_x, lowest_y = np.min(corners, axis=0)
highest_x, highest_y = np.max(corners, axis=0) + 1
corners -= np.array([lowest_x,lowest_y])
matrix = lil_matrix((highest_x-lowest_x, highest_y-lowest_y), dtype=np.int8)

# Initialize the edge of the matrix
for i, current in enumerate(corners):
    x1,y1 = corners[i-1]
    x2,y2 = current
    
    if y1 == y2:
        for j in range(min(x1,x2), max(x1,x2) + 1):
            matrix[j,y1] = 1
    else:
        for j in range(min(y1,y2), max(y1,y2) + 1):
            matrix[x1,j] = 1

# Convert to a csr matrix to optimize future operations
matrix = matrix.tocsr()

# Iterate over all corner pairs
biggest_rectangle = 0
for i, v1 in enumerate(corners):
    # print(i,v1,biggest_rectangle)
    x1,y1 = v1
    for j,v2 in enumerate(corners[i+1:]):
        x2,y2 = v2

        # Special case for thin rectangles, avoids issues with raycast later
        if abs(x1-x2) <= 1 or abs(y1-y2) <= 1:
            area = prod(np.abs(v2-v1) + 1)
            biggest_rectangle = max(biggest_rectangle, area)
            continue

        frst_x = min(x1,x2)
        last_x = max(x1,x2)
        frst_y = min(y1,y2)
        last_y = max(y1,y2)

        # The inside of the rectangle cannot contain any edges
        if matrix[frst_x+1:last_x, frst_y+1:last_y].getnnz() != 0:
            continue

        # Diagonal raycast to count intersections with the edges
        checkpoint = time.time()
        x_range = []
        y_range = []
        x_start = int((frst_x + last_x)//2)
        y_start = int((frst_y + last_y)//2)
        for _ in range(min(x_start,y_start)):
            x_range.append(x_start)
            y_range.append(y_start)
            x_start -= 1
            y_start -= 1
        # An even amount of hits indicates we are outside of the shape
        if np.sum(matrix[x_range,y_range]) % 2 == 0:
            continue

        # Rectangle is valid, find area
        area = prod(np.abs(v2-v1) + 1)
        biggest_rectangle = max(biggest_rectangle, area)

duration = time.time() - start

print(biggest_rectangle, f"In {duration} seconds")
