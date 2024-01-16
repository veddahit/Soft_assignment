from PIL import Image

# Open the image file
image_path = r'C:\files\Class\Software now\Assignment 2/chapter1.jpg'

original_image = Image.open(image_path)

# Get the dimensions of the image
width, height = original_image.size

# Print top 5 RGB values in the existing image
print("Top 5 RGB values in the existing image:")
for y in range(min(5, height)):
    for x in range(min(5, width)):
        r, g, b = original_image.getpixel((x, y))
        print(f"Original RGB at ({x}, {y}): ({r}, {g}, {b})")

# Get the generated number using the provided algorithm
import time

current_time = int(time.time())
generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10

# Modify the image with the generated number
for y in range(height):
    for x in range(width):
        r, g, b = original_image.getpixel((x, y))

        # Add the generated number to each RGB value
        new_r = r + generated_number
        new_g = g + generated_number
        new_b = b + generated_number

        # Update the pixel with the new RGB values
        original_image.putpixel((x, y), (new_r, new_g, new_b))

# Save the modified image
output_image_path = r'C:\files\Class\Software now\Assignment 2\Modified_Chapter1.png'
original_image.save(output_image_path)

# Open the modified image
modified_image = Image.open(output_image_path)

# Print top 5 RGB values in the newly created image with the generated number
print("\nTop 5 RGB values in the newly created image with the generated number:")
for y in range(min(5, height)):
    for x in range(min(5, width)):
        r, g, b = modified_image.getpixel((x, y))
        print(f"Modified RGB at ({x}, {y}): ({r}, {g}, {b})")

print(f"\nImage has been modified and saved as {output_image_path}")


from PIL import Image

def read_rgb_values(image_path):
    # Open the image
    image = Image.open(image_path)

    # Get the RGB values of each pixel
    rgb_values = list(image.getdata())

    return rgb_values

# Example usage
image_path =output_image_path## r'C:\files\Class\Software now\Assignment 2/chapter1.jpg'
rgb_values = read_rgb_values(image_path)

# Display the RGB values of the first few pixels
for i in range(min(5, len(rgb_values))):
    print(f"Pixel {i + 1}: {rgb_values[i]}")


from PIL import Image

def read_rgb_values(image_path):
    # Open the image
    image = Image.open(image_path)

    # Get the RGB values of each pixel
    rgb_values = list(image.getdata())

    return rgb_values

# Example usage
image_path =r'C:\files\Class\Software now\Assignment 2/chapter1.jpg'
rgb_values = read_rgb_values(image_path)

# Display the RGB values of the first few pixels
for i in range(min(5, len(rgb_values))):
    print(f"Pixel {i + 1}: {rgb_values[i]}")
