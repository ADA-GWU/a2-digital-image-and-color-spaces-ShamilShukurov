from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


img_path = "winner.jpg"
image = Image.open(img_path)

img_array = np.array(image)

def convert_to_grayscale(img):
    return np.dot(img[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)

grayscale_image = convert_to_grayscale(img_array)

average_grayscale = np.mean(img_array[..., :3], axis=2).astype(np.uint8)

# Display the grayscale images
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
axes[0].imshow(image)
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(grayscale_image, cmap='gray')
axes[1].set_title('Grayscale (Luminosity Method)')
axes[1].axis('off')

axes[2].imshow(average_grayscale, cmap='gray')
axes[2].set_title('Grayscale (Average Method)')
axes[2].axis('off')

plt.show()

# Quantitative comparison using mean squared error (MSE)
mse = np.mean((grayscale_image - average_grayscale) ** 2)
print("MSE between Luminosity and Average Methods:", mse)
