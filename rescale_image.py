import cv2
import  numpy as np

def rescaleFrame(frame, scale=1):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

img=cv2.imread('./jpppp.jpg')
img_back=cv2.imread('./back.jpg')
#日常缩放

img_back= rescaleFrame(img_back)
rows,cols,channels = img_back.shape
cv2.imshow('img_back',img_back)
print(rows)
print(cols)

img=rescaleFrame(img, scale=0.6)
rows,cols,channels = img.shape
cv2.imshow('img',img)
rows,cols,channels = img.shape#rows，cols最后一定要是前景图片的，后面遍历图片需要用到
print(rows)
print(cols)
#转换hsv
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#获取mask
lower_blue=np.array([78,43,46])
upper_blue=np.array([110,255,255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)
cv2.imshow('Mask', mask)

#腐蚀膨胀
erode=cv2.erode(mask,None,iterations=10)
cv2.imshow('erode',erode)
dilate=cv2.dilate(erode,None,iterations=1)
cv2.imshow('dilate',dilate)

#遍历替换
# center=[50,50]#在新背景图片中的位置
# for i in range(rows):
#     for j in range(cols):
#         if dilate[i,j]==0:#0代表黑色的点
#             # print(i, '-', j)
#             img_back[center[0]+i,center[1]+j]=img[i,j]#此处替换颜色，为BGR通道
# cv2.imshow('res',img_back)

cv2.waitKey(0)
cv2.destroyAllWindows()