import cv2
import subprocess

original_image_path = input("input image file path: ")
#ex) /home/ossuser/demo.jpg
image = cv2.imread(original_image_path)

new_width = int(input("input image width: "))
#ex) 500
new_height = int(input("input image height: "))
#ex) 300
resized_image = cv2.resize(image, (new_width, new_height))

angle = float(input("input image angle: "))
#ex) 90
rows, cols = resized_image.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((cols /2, rows / 2), angle, 1)
rotated_image = cv2.warpAffine(resized_image, rotation_matrix, (cols, rows))

print("color code")
print("1: cv2.COLOR_BGR2GRAY\n2: cv2.COLOR_BGR2RGB\n3: cv2.COLOR_BGR2BGR555\n4: cv2.COLOR_BGR2BGR565\n5: cv2.COLOR_BGR2LUV\n")
color_conversion_choice = int(input("input color code(number): "))
#ex) 1

color_conversions = {1: cv2.COLOR_BGR2GRAY, 2: cv2.COLOR_BGR2RGB, 3: cv2.COLOR_BGR2BGR555, 4: cv2.COLOR_BGR2BGR565, 5: cv2.COLOR_BGR2LUV}

chosen_color_conversion = color_conversions.get(color_conversion_choice)
improved_image = cv2.cvtColor(rotated_image, chosen_color_conversion)

output_image_path = input("input image file path: ")
#ex) /home/ossuser/demo1.jpg

cv2.imwrite(output_image_path, improved_image)

subprocess.run(['xdg-open', output_image_path], check=True)