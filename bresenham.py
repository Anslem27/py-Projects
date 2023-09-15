import pygame
import sys

# Ensure you have pygame installed as well as python
""" 
refer to: https://www.python.org/ and ensure to set the environment variable before using 

check with this to verify installation -> python --version   

pip install pygame
"""

# Function to draw a circle using Bresenham's algorithm

#  General algorithm brief explanation
""" 
Explanation:

The draw_circle function:

This function takes three arguments: screen, center, and radius.
screen is the Pygame surface on which the circle will be drawn.
center is a tuple containing the (x, y) coordinates of the circle's center.
radius is the radius of the circle.
Inside the function, there's a while-loop that implements Bresenham's circle drawing algorithm.
The while loop in draw_circle:

x and y are variables representing the current coordinates. x starts at 0, and y is initially set to the radius of the circle.
The loop continues as long as x is less than or equal to y, ensuring that the algorithm covers all points in the first octant of the circle.
In each iteration of the loop, the algorithm calculates eight symmetric points around the center using the current values of x and y.
The points list:

This list contains eight tuples, each representing a point around the center of the circle. These points are calculated based on the algorithm logic.
Plotting the points:

The pygame.draw.circle function is used to draw a single-pixel circle at each of the calculated points.
Incrementing x and updating P:

x is incremented by 1 in each iteration.
The decision parameter P is updated based on its current value. If P is less than 0, it uses the first update rule; otherwise, it uses the second update rule. This determines whether to move in the horizontal direction or the diagonal direction.
The main loop:

This loop handles the Pygame window, events, and drawing.
It clears the screen, draws the circle using draw_circle, and updates the display.
The Pygame initialization and setup:

Pygame is initialized using pygame.init().
The screen dimensions are set, and a window titled "Bresenham Circle Drawing Algorithm" is created.
The center and radius of the circle are specified.
Quitting Pygame:

After the main loop terminates (usually when the window is closed), Pygame is quit using pygame.quit().
"""


def draw_circle(screen, center, radius):
    x_center, y_center = center
    x = 0
    y = radius
    P = 3 - 2 * radius

    while x <= y:
        # Calculate points around the center in eight symmetric positions based off the algorithm logic
        points = [
            (x + x_center, y + y_center),
            (-x + x_center, y + y_center),
            (x + x_center, -y + y_center),
            (-x + x_center, -y + y_center),
            (y + x_center, x + y_center),
            (-y + x_center, x + y_center),
            (y + x_center, -x + y_center),
            (-y + x_center, -x + y_center)
        ]

        # Plot these points
        for point in points:
            pygame.draw.circle(screen, (255, 255, 255), point, 1)

        # Increment x
        x += 1

        # Update the decision parameter P
        if P < 0:
            P += 4 * x + 6
        else:
            P += 4 * (x - y) + 10
            y -= 1


""" 
The code below is for the pygame module
"""
# Initialize Pygame
pygame.init()

# Set screen dimensions
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bresenham Circle Drawing Algorithm")

# Set center and radius of the circle
center = (width // 2, height // 2)
radius = 100

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the circle
    draw_circle(screen, center, radius)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
