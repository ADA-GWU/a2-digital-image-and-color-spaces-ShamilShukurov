from sklearn.cluster import KMeans
from skimage.color import rgb2hsv, hsv2rgb
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def color_quantization(img, n_colors):
    # Reshape the image to be a list of pixels
    img_pixels = img.reshape(-1, 3)

    kmeans = KMeans(n_clusters=n_colors, random_state=0).fit(img_pixels)
    new_colors = kmeans.cluster_centers_[kmeans.labels_]

    quantized_image = new_colors.reshape(img.shape).astype(np.uint8)
    return quantized_image


img_path = "starry_night.jpg"
image = Image.open(img_path)


img_array = np.array(image)
small_img = image.resize((image.width // 4, image.height // 4))

small_img_array = np.array(small_img)


n_colors = 16  # reducing to 16 colors
print("Quantization Starts.")

quantized_img = color_quantization(small_img_array, n_colors)
print("Quantization Successfull.")
# Display the quantized image
plt.figure(figsize=(8, 6))
plt.imshow(quantized_img)
plt.title('Color Quantized Image (16 Colors)')
plt.axis('off')
plt.show()