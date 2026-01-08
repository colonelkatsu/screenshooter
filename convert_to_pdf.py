# Python program to generate PDF found inside intended folder

from PIL import Image
import os

course_name = "{input-course-name-here}"
# Folder containing PNG files
image_folder = f"{course_name}/"
output_pdf = f"{course_name}.pdf"

# Get all PNG files in folder
png_files = [f for f in os.listdir(image_folder) if f.lower().endswith('.png')]
png_files.sort()  # Optional: to ensure order

# Open and convert images to RGB
image_list = []
for file in png_files:
    img_path = os.path.join(image_folder, file)
    img = Image.open(img_path).convert('RGB')
    image_list.append(img)

# Save all images into a single PDF
if image_list:
    image_list[0].save(
        output_pdf, save_all=True, append_images=image_list[1:]
    )
    print(f"Saved {output_pdf} successfully.")
else:
    print("No PNG files found.")
