import  numpy as np

from PIL import Image

img =  Image.open('download.jfif')
pixelMap = img.load()
'''mat = np.asanyarray(Image.open('download.jfif'))
print(mat)'''
im = Image.new(img.mode,img.size)

pixelNew = im.load()

for i in range(im.size[0]):
    for j in range(im.size[1]):
        if(pixelMap[i,j]>=0 and pixelMap[i,j]<=31):

            pixelNew[i,j] = 0
        elif (pixelMap[i,j]>=32 and pixelMap[i,j]<=63):
            pixelNew[i,j]=1
        elif (pixelMap[i, j] >= 64 and pixelMap[i, j] <= 95):
            pixelNew[i, j] = 2
        elif (pixelMap[i, j] >= 96 and pixelMap[i, j] <= 127):
            pixelNew[i, j] = 3
        elif (pixelMap[i, j] >= 128 and pixelMap[i, j] <= 159):
            pixelNew[i, j] = 4
        elif (pixelMap[i, j] >= 160 and pixelMap[i, j] <= 191):
            pixelNew[i, j] = 5
        elif (pixelMap[i, j] >= 192 and pixelMap[i, j] <= 223):
            pixelNew[i, j] = 6
        elif (pixelMap[i, j] >= 224 and pixelMap[i, j] <= 255):
            pixelNew[i, j] = 7
im.save('download2.jpg')
#j=np.asanyarray(Image.open('download1.jpg'))