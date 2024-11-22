from PIL import Image, ImageDraw, ImageFont

#pip install pillow
# Step 1: Create a blank image
width, height = 500, 300
image = Image.new('RGB', (width, height), color=(255, 255, 255))  # White background

# Step 2: Draw text on the image
draw = ImageDraw.Draw(image)
text = "Hello, World!"
font_size = 30
try:
    # Load a TrueType or OpenType font file (if available)
    font = ImageFont.truetype("DejaVuSans.ttf", font_size)
except IOError:
    # Default font if the specified one isn't available
    font = ImageFont.load_default()

# Calculate text position using textbbox
bbox = draw.textbbox((0, 0), text, font=font)
text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
text_x = (width - text_width) // 2
text_y = (height - text_height) // 2
draw.text((text_x, text_y), text, font=font, fill=(0, 0, 0))  # Black text

# Step 3: Save the image
output_path = "../hello-world.jpg"
image.save(output_path, "JPEG")

print(f"Image saved as {output_path}")
