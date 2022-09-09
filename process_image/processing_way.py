from re import I
from skimage.color import rgb2gray
import numpy as np
import cv2
#import matplotlib.pyplot as plt
#matplotlib inline
from scipy import ndimage
import math

image = cv2.imread('12.jpg')
# image.shape
#img_name = image
grayo = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(grayo,(39,39),sigmaX=0)

imgresize = cv2.resize(image,(530,303))
greyresize = cv2.resize(gray,(530,303))


# cv2.imshow('Original image',image)
# cv2.imshow('Gray12', grayo)

# cv2.imshow('Gray image', greyresize)

greyreshape = greyresize.reshape(530*303)
for i in range(greyreshape.shape[0]):
    if greyreshape[i] > 150 and greyreshape[i] < 170 :
        greyreshape[i] = 255
    
    # elif greyreshape[i] > 150 :
    #     greyreshape[i] = 100 
    else:
        greyreshape[i] = 0

grey = greyreshape.reshape(303,530)
lowThresh = 50
upThresh = 200

ret, bw = cv2.threshold(grey, 120, 255, cv2.THRESH_BINARY)
# cv2.imshow("Result bw", bw)
kernel = np.ones((7,7), np.uint8)
img_dilation = cv2.dilate(bw, kernel, iterations=1)
cv2.imshow("Result dilate", img_dilation)

edge = cv2.Canny(img_dilation,lowThresh,upThresh)
# cv2.imshow("Result canny", edge)
lines = cv2.HoughLines(edge,rho=1,theta=np.pi/180,threshold=43,min_theta = 2.2, max_theta = 2.355)
lines2 = cv2.HoughLines(edge,rho=1,theta=np.pi/180,threshold=41,min_theta = 0.02, max_theta = 0.91)
# linemin = (lines2+lines)/2

leg = len(lines)
img2 = imgresize.copy()
for i in range (leg) :
    for rho,theta in lines[i]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        print('line 1')
        print(x1)
        print(x2)
        cv2.line(img2,(x1,y1),(x2,y2),(0,0,255),1)
    i=i+1

    



leg2 = len(lines2)
for i in range (leg2) :
    for rho,theta in lines2[0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        print('line 2')
        print(x1)
        print(x2)
        cv2.line(img2,(x1,y1),(x2,y2),(0,0,255),1)
    i=i+1



# Show result

img3 = img2[202,0:530]

leg_center = len(img3)

line_center =0

for i in range(leg_center):  
    if (img3[i][2] > 250):
        center = img3[i][2]
        print('Index : ',i,img3[i][2])
        # line_center = i
        line_center = i+line_center
        sum_line_center = line_center/2
print('Center : ',sum_line_center)  

center_Image = 265
ce_line = center_Image - sum_line_center

if ce_line != 0 :
    if ce_line > 0 :
        print("turn right")
    elif ce_line < 0 :
        print("turn left")
else:
    print("go ahead")

# legmin = int(sum_line_center)
# # print(legmin)
# for i in range (legmin) :
#     for rho,theta in i :
#         a = np.cos(theta)
#         b = np.sin(theta)
#         x0 = a*rho
#         y0 = b*rho
#         x1 = int(x0 + 1000*(-b))
#         y1 = int(y0 + 1000*(a))
#         x2 = int(x0 - 1000*(-b))
#         y2 = int(y0 - 1000*(a))
#         print(x1)
#         print(x2)
#         cv2.line(img2,(x1,y1),(x2,y2),(0,0,255),2)
#     i=i+1

cv2.imshow("Result Image", img2)
cv2.imwrite('houghlines3.jpg',img2)

# print(l)
# cv2.imshow('greyreshape',edge2 )


# print(img2.shape)
#cv2.imshow('img_name',image)
cv2.waitKey(0)
cv2.destroyAllWindows()