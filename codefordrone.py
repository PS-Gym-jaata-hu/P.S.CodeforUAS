import cv2
import numpy as np

def count_houses(mask):
    """Counts the number of houses in the given mask."""
    contours, _ = cv2.findContours(mask.astype(np.uint8), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return len(contours)

def get_house_priority(color):
    """Returns the priority of the houses of the given color."""
    if color == red_house_color:
        return 1
    elif color == blue_house_color:
        return 2
    return 0  # Default priority for other colors

def calculate_rescue_ratio(pb, pg):
    """Calculates the rescue ratio."""
    return pb / pg if pg != 0 else float('inf')

# Define colors and priorities
red_house_color = (0, 0, 255)   # Red color in BGR format
blue_house_color = (255, 0, 0)  # Blue color in BGR format

# Load the input image
input_image_path = 'image2.jpg'
image = cv2.imread(input_image_path)

# Define color ranges with tolerance
red_lower = np.array([0, 0, 150])
red_upper = np.array([100, 100, 255])
blue_lower = np.array([150, 0, 0])
blue_upper = np.array([255, 100, 100])

#Green:

#Lower Bound: np.array([0, 100, 0]) (lower limit of green color)
#Upper Bound: np.array([100, 255, 100]) (upper limit of green color)
#Brown:

#Lower Bound: np.array([50, 50, 0]) (lower limit of brown color)
#Upper Bound: np.array([150, 100, 50]) (upper limit of brown color)

# Create masks for red and blue houses
red_house_mask = cv2.inRange(image, red_lower, red_upper)
blue_house_mask = cv2.inRange(image, blue_lower, blue_upper)

# Count houses
houses_on_burnt = count_houses(red_house_mask)
houses_on_green = count_houses(blue_house_mask)

# Calculate priorities of houses
priority_burnt = get_house_priority(red_house_color) * houses_on_burnt + \
                 get_house_priority(blue_house_color) * houses_on_burnt
priority_green = get_house_priority(red_house_color) * houses_on_green + \
                 get_house_priority(blue_house_color) * houses_on_green

# Calculate rescue ratio
rescue_ratio = calculate_rescue_ratio(priority_burnt, priority_green)

# Print the results
print("House Counts (Hb, Hg):", houses_on_burnt, houses_on_green)
print("House Priorities (Pb, Pg):", priority_burnt, priority_green)
print("Rescue Ratio:", rescue_ratio)