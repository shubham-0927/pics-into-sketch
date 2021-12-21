import cv2
import matplotlib.pyplot as plt

img = cv2.imread("shiva.jpg")

RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#image into pencil sketch
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
invert_img = cv2.bitwise_not(grey_img)
invert_img = 255-grey_img
blur_img = cv2.GaussianBlur(invert_img, (111, 111), 0)
invblur_img = cv2.bitwise_not(blur_img)
invblur_img = 255 - blur_img
sketch_img = cv2.divide(grey_img, invert_img, scale=256.0)
#display using matplotlib
plt.figure(figsize=(14, 8))
plt.subplot(1,2,1)
plt.title('Original image', size=18)
plt.imshow(RGB_img)                        #original image
plt.axis('off')
plt.subplot(1,2,2)
plt.title('Sketch', size=18)
rgb_sketch=cv2.cvtColor(sketch_img, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_sketch)
plt.axis('off')
plt.show()