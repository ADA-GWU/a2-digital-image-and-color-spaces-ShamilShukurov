import cv2
import numpy as np
from skimage.color import deltaE_ciede2000, rgb2lab

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        try:
            # Get the LAB color of the clicked pixel
            lab_clicked = rgb2lab([[image[y, x]]])[0][0]

            # Compute the LAB values for all pixels (optimization step)
            lab_image = rgb2lab(image)

            # Calculate the DeltaE values efficiently using broadcasting
            delta_es = np.sqrt(np.sum((lab_image - lab_clicked) ** 2, axis=2))
            mask = (delta_es < threshold).astype(np.uint8) * 255

            # Display the mask
            cv2.imshow("Color Similarity Mask", mask)
        except Exception as e:
            print(f"Error during processing: {e}")

# Predefined image path
image_path = "modernart.jpg"
original_image = cv2.imread(image_path)
original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

# Resize image if it's too large
scale_percent = 15  # percent of original size
width = int(original_image.shape[1] * scale_percent / 100)
height = int(original_image.shape[0] * scale_percent / 100)
dim = (width, height)
image = cv2.resize(original_image, dim, interpolation=cv2.INTER_AREA)

# Define a threshold for color similarity
threshold = 15  # Adjust this value based on your needs

# Create a window and set a callback function for mouse clicks
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", click_event)

# Display the image
cv2.imshow("Image", image)
key = cv2.waitKey(0)
if key == 27:  # Esc key to close all windows
    cv2.destroyAllWindows()
