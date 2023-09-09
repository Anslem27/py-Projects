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

x_center and y_center are the coordinates of the center of the circle. 
x and y represent the current position while drawing the circle. 
P is the decision parameter used to determine which pixel to plot in each step.

The algorithm starts by initializing x to 0 and y to the radius. P is calculated based on the initial radius.

The loop iterates as long as x is less than or equal to y. This ensures that the algorithm covers all points in the first octant of the circle.

For each iteration, it calculates the eight symmetric points around the center using the current values of x and y. These points are then plotted on the screen.

x is incremented by 1 in each iteration.

The decision parameter P is updated based on its current value. If P is less than 0, 
it uses the first update rule; otherwise, it uses the second update rule. 
This determines whether to move in the horizontal direction or the diagonal direction.

Finally, the radius y is decremented by 1 if the second update rule is used.

The code then uses Pygame to draw the points on the screen and updates the display
"""
# while-loop segment explanation
""" 
x: This is a variable that represents the current x-coordinate. It starts at 0 and is incremented in each iteration of the loop.
y: This is a variable that represents the current y-coordinate, which is initially set to the radius of the circle.
The condition x <= y means that the loop will continue executing as long as x is less than or equal to y. 
This ensures that the algorithm covers all points in the first octant of the circle.

As the loop iterates, x will gradually increase, and y will decrease (if needed), until the condition x <= y 
is no longer met. At that point, the loop will terminate, and the circle will be fully drawn. 
The Bresenham's algorithm ensures that the circle is drawn with a good approximation of symmetry and efficiency
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
