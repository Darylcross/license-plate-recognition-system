import os
import cv2
import matplotlib.pyplot as plt
import numpy as np

plaka_adresler = os.listdir("plakalar/")
img = cv2.imread("plakalar/" + plaka_adresler[19])
img = cv2.resize(img, (500, 500))

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.show()

img_bgr = img
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.imshow(img_gray, cmap="gray")
plt.show()
