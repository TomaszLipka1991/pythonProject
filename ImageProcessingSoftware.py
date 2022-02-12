import numpy as np
# import pandas as pd
# import matplotlib as mpl
import matplotlib.pyplot as plt
import cv2
image = cv2.imread('Lenna.png')
# print(type(image))
#
# plt.imshow(image)
# plt.show()

# konwersja do rgb

# rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# # plt.imshow(rgb)
# # plt.show()
#
# # grey scale
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# plt.imshow(gray, cmap='gray')
# plt.show()
#
# cv2.imwrite('szara_lenna.jpg', gray)

# przetwarzanie wideo

video = []
object = cv2.VideoCapture("akiyo_cif.y4m")
retval, image = object.read()
while retval:
    video.append(image)
    retval, image = object.read()
object.release()
plt.imshow(cv2.cvtColor(video[0], cv2.COLOR_BGR2RGB))
# plt.show()
fourcc = cv2.VideoWriter_fourcc(*"MJPG")  # *"MJPG" == "M", "J", "P", "G"
object = cv2.VideoWriter("akiyo_cif.avi", fourcc, 30, (352, 288))
for image in video:
    object.write(image)
object.release()

new = []
object = cv2.VideoCapture("akiyo_cif.avi")
retval, image = object.read()
while retval:
    new.append(image)
    retval, image = object.read()
object.release()

# plt.imshow(cv2.cvtColor(new[150], cv2.COLOR_BGR2RGB))
# plt.show()

# modyfikowanie pikseli :D
# wszystko jest na ten moment w numpy !
image = cv2.imread('Lenna.png')
# print(image[100,100,0])
image[100,100,0]=255
image[100,100,1]=255
image[100,100,2]=255
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# plt.show()
image[10, 10, 2] = 0
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# plt.show()

d = image.shape
n = image.size
o = image.dtype

# print(d)
# print(n)
# print(o)

# narysujmy kółko
# image = cv2.imread("Lenna.png")
# circle = cv2.circle(image, (256, 256), 128, (255, 255, 255), -1)
# plt.imshow(cv2.cvtColor(circle, cv2.COLOR_BGR2RGB))
# plt.show()

# prostokat

# image = cv2.imread("Lenna.png")
# rectangle = cv2.rectangle(image, (128, 128), (384, 384), (255, 255, 255), -1)
# plt.imshow(cv2.cvtColor(rectangle, cv2.COLOR_BGR2RGB))
# plt.show()

# elipsa
# image = cv2.imread("Lenna.png")
# ellipse = cv2.ellipse(image, (256, 256), (128, 128), 50, 45, 360, (0, 0, 255), -1)
# plt.imshow(cv2.cvtColor(ellipse, cv2.COLOR_BGR2RGB))
# plt.show()

# filtering

# image = cv2.imread("Lenna.png")
# bilateral = cv2.bilateralFilter(image, 55, 75, 100)
# plt.imshow(cv2.cvtColor(bilateral, cv2.COLOR_BGR2RGB))
# plt.show()

# rozmazac blurring

# image = cv2.imread("Lenna.png")
# blur = cv2.blur(image, (20, 20))
# plt.imshow(cv2.cvtColor(blur, cv2.COLOR_BGR2RGB))
# plt.show()


# ćw1
# Given the “Lenna” image load it using OpenCV, split the channels using NumPy
# and display each channel in a new windows called as the channel.
#
# image = cv2.imread("Lenna.png")
# # plt.imshow(cv2.)
# # plt.show()
# ar = np.zeros((image.shape[0],image.shape[1], 3), dtype=int)
# # plt.imshow(ar)
# # plt.show()
#
# # ar[:, :, 0] = image[:, :, 2]
# plt.imshow(image[:, :, 1])
# plt.show()
#
# cw 2

image = cv2.imread("Lenna.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray, cmap='gray')
# plt.show()
gray2 = 120<= gray
plt.imshow(gray2, cmap='gray')
# plt.show()

c = np.zeros((512,512,3), dtype=int)
c[:,:,0] = image[:,:, 2]*gray2
c[:,:,1] = image[:,:, 1]*gray2
c[:,:,2] = image[:,:, 0]*gray2
plt.imshow(c)
plt.show()
