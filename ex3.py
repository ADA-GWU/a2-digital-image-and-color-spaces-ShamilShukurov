from PIL import ImageEnhance, ImageOps
from skimage.color import rgb2hsv, hsv2rgb
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img_path = "winner.jpg"
image = Image.open(img_path)
image_hsv = image.convert('HSV')
hsv_array = np.array(image_hsv)

# Function to change Hue, which rotates the hue channel (0-360 degrees scaled to 0-255 in PIL)
def change_hue(hsv_array, shift):
    hsv_array[:, :, 0] = (hsv_array[:, :, 0] + shift) % 256
    return Image.fromarray(hsv_array, 'HSV').convert('RGB')

# Adjusting hue by +30 
hue_shifted_image = change_hue(hsv_array, 30)

# Function to adjust saturation and brightness
def adjust_saturation_brightness(image, saturation_factor, brightness_factor):
    converter = ImageEnhance.Color(image)
    image_sat_adjusted = converter.enhance(saturation_factor)
    
    converter = ImageEnhance.Brightness(image_sat_adjusted)
    image_bright_adjusted = converter.enhance(brightness_factor)
    
    return image_bright_adjusted

sat_bright_adjusted_image = adjust_saturation_brightness(hue_shifted_image, 1.2, 0.8)

# Display the adjusted images
fig, ax = plt.subplots(1, 2, figsize=(12, 6))
ax[0].imshow(hue_shifted_image)
ax[0].set_title('Hue Shifted Image')
ax[0].axis('off')

ax[1].imshow(sat_bright_adjusted_image)
ax[1].set_title('Saturation & Brightness Adjusted Image')
ax[1].axis('off')

plt.show()
