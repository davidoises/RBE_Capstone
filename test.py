from PIL import Image

# read in fogColor.png to see what structure is like

# Open the image file
img = Image.open('/home/vboxuser/UrbanFireRobot/ros2_ws/src/warehouse_simulation/models/fog_generator/materials/textures/fogcolors.png')

# Get image data
pixels = list(img.getdata())

# Print the first few pixel values to see the structure
print(pixels[:10])
# Define a function to change fog color to fire color
def change_fog_to_fire(pixels):
    fire_pixels = []
    for pixel in pixels:
        r, g, b, a = pixel
        # Change the color to a fire-like color
        fire_pixel = (min(255, r + 100), max(0, g - 100), max(0, b - 100), a)
        fire_pixels.append(fire_pixel)
    return fire_pixels

# Change the fog color to fire color
fire_pixels = change_fog_to_fire(pixels)

# Create a new image with the fire color
fire_img = Image.new(img.mode, img.size)
fire_img.putdata(fire_pixels)

# Save the new image
fire_img.save('/home/vboxuser/UrbanFireRobot/ros2_ws/src/warehouse_simulation/models/fire_generator/materials/textures/firecolors.png')


# Open the fire image file
fire_img = Image.open('/home/vboxuser/UrbanFireRobot/ros2_ws/src/warehouse_simulation/models/fire_generator/materials/textures/fire_texture3.jpeg')

# Convert the image to the same format as fogcolors.png
fire_img = fire_img.convert(img.mode)

# Save the converted image
fire_img.save('/home/vboxuser/UrbanFireRobot/ros2_ws/src/warehouse_simulation/models/fire_generator/materials/textures/fire.png')