'''
From: Google
Difficulty: Medium

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
'''

import random
import os

PI = 0
total_random_points = 0
points_in_circle = 0
while round(PI, 2) != 3.14:
    # randoms are between 0 and 1
    # hence our quadrant will be 1 X 1 square
    # and radius of our circle will be 1
    x = random.random()
    y = random.random()
    total_random_points += 1
    # checking if random points distance from origin (0, 0) is less than 1
    if x**2 + y**2 <= 1:
        # point is inside circle
        points_in_circle += 1

    # multiply by 4 for 4 quadrants
    PI = (points_in_circle / total_random_points) * 4
    print("\r" + str(PI*4))
    os.system("clear")

print(PI)
