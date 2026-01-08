# Python program to take screenshots and save in the course folder

import numpy as np
import pyautogui
from PIL import Image
import time
from skimage.metrics import structural_similarity as ssim
import cv2
import os

course_name = "{insert-course-name-here}"
counter = 1

def convert_to_cv2_gray(img_raw):
    img_np_rgb = np.array(img_raw)
    img_np_gray = cv2.cvtColor(img_np_rgb, cv2.COLOR_RGB2GRAY)
    return img_np_gray

def make_dir(d):
    if not os.path.exists(d):
        os.makedirs(d)

make_dir(course_name)
img1_raw = pyautogui.screenshot()
img1 = convert_to_cv2_gray(img1_raw)

time.sleep(5)

while True:
    img2_raw = pyautogui.screenshot()
    img2 = convert_to_cv2_gray(img2_raw)
    score, _ = ssim(img1, img2, full=True)
    print(f"SSIM score: {score}")

    if score > 0.9:
        print("Images are identical")
    else:
        print("Images are different, generating screenshot")
        img2.save(f"{course_name}/screenshot-{counter:06}.png")
        img1_raw = img2_raw
        img1 = convert_to_cv2_gray(img1_raw)
        counter += 1
    time.sleep(5)
