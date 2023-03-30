#!/usr/bin/env python
# coding: utf-8


import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import platform
import sys

img = cv.imread('duck0.jpg')


def zero_pad(img, pad):
    img_pad = np.pad(img, ((pad, pad), (pad, pad)), mode = 'constant', constant_values = (0, 0))

    return img_pad

def conv_filter(img, stride, padding, kernel):
    h, w = img.shape
    f, f = kernel.shape

    n_h = int(int(h + 2 * padding - f) / stride + 1)
    n_w = int(int(w + 2 * padding - f) / stride + 1)
    z = np.zeros([n_h, n_w])

    img_pad = zero_pad(img, padding)

    for h in range(n_h):
        vertical_start = stride * h
        verttical_end = vertical_start + f
        for w in range(n_w):
            horizontal_start = stride * w
            horizontal_end = horizontal_start + f
            target = img_pad[vertical_start:verttical_end, horizontal_start:horizontal_end]
            conv = np.multiply(target, kernel)
            conv_sum = np.sum(conv)
            z[h, w] = conv_sum

    return z

kernel_y = np.array([[-1, -2, -1],
                     [0,   0,  0],
                     [1,   2,  1]])

kernel_x = np.array([[-1, 0,  1],
                     [-2, 0,  2],
                     [-1, 0,  1]])




cap = cv.VideoCapture(1)
thres1 = 30
thres2 = 100
count = 0
kernel = np.array([[-3, 0, 3], [-10, 0, 10], [-3, 0, 3]])
kernel_mol = np.ones((3,3),np.uint8)


while True:
    ret, frame = cap.read()
    
    cropped = cv.resize(frame[400:800, 760:1160, :], dsize = (815, 815))
    
    processed = cropped
    #Canny Filter
    
    
#     processed = cv.Canny(processed, thres1, thres2)
#     processed = cv.dilate(processed,kernel,iterations =4)
#     processed = cv.morphologyEx(processed, cv.MORPH_OPEN, kernel)
#     cv.putText(processed, str(thres1), (0, 50), cv.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 5, cv.LINE_AA)
#     cv.putText(processed, str(thres2), (0, 100), cv.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 5, cv.LINE_AA)

#
# Sobel
#

    blured = cv.GaussianBlur(cropped, (11, 11), 0)
    grays = cv.cvtColor(blured, cv.COLOR_BGR2GRAY)
    #processed = cv.Sobel(processed, cv.CV_32F, 1, 1, ksize = 3, scale = 0.5)
    dst = np.sqrt(np.square(cv.filter2D(grays, cv.CV_16S, kernel)) +  
                  np.square(cv.filter2D(grays, cv.CV_16S, kernel.T)))

    processed = ((dst - dst.min()) / (dst.max() - dst.min()) * 255).astype(np.uint8)
    #processed = cv.normalize(dst, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)
    ret, processed = cv.threshold(processed,thres1,255,cv.THRESH_BINARY)    
    #processed = cv.morphologyEx(processed, cv.MORPH_OPEN, kernel_mol)
    cv.putText(processed, str(thres1), (0, 50), cv.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 5, cv.LINE_AA)


    #
    #  Sobel using np
    #
#     processed = cv.cvtColor(processed, cv.COLOR_BGR2GRAY) 
#     processed = conv_filter(cropped, stride = 1, padding = 0, kernel = kernel_x) + conv_filter(img, stride = 1, padding = 0, kernel = kernel_y)
    

    
    count += 1
    if count == 10:
        cv.imwrite('duckpros.png', processed)
        cv.imwrite('duckpros_col.png', cropped)
        #break
        


    #cv.imshow('cam', cropped)

    cv.imshow('duck', processed)
    
    k = cv.waitKey(1)
    
    if k == 113:
        break
    if k == 119:
        thres1+= 1
    if k == 115:
        thres1-= 1
    if k == 101:
        thres2+= 5   
    if k == 100:
        thres2-= 5
        
    #plt.imshow(processed)
   # plt.show()

        
        
cap.release()
cv.destroyAllWindows()
cv.waitKey(1)

