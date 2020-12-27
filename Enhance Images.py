'''from PIL import Image

img = Image.open('download.jfif')

#transposing
transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)

transposed_img.save('corrected.png')
print('Done Flipping')'''

#Image Enhancement CLAHE

import cv2

img = cv2.imread('images (1).jfif')

clahe = cv2.createCLAHE()

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#apply enhancement

enh_img = clahe.apply(gray_img)

#save it to a file
cv2.imwrite('enhance.png',enh_img)
print('DONE ENHANCING')