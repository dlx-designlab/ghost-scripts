#!/usr/bin/env python
# coding: utf-8


import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import platform
import sys

img = cv.imread('duck0.jpg')

#duck image
cv.imshow('duck', img)
#test various algorhythm for edge detection
duck_mono = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('sob', cv.Sobel(duck_mono, cv.CV_32F, 1, 1, ksize = 3))
cv.imshow('lap', cv.Laplacian(duck_mono, cv.CV_32F))
cv.imshow('can', cv.Canny(duck_mono, 60, 150))

cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1)


#bilateral filter is edge-preserving smoothing
pros = cv.bilateralFilter(img, 15, 20, 20)
cv.imshow('duck_bilateral', pros)


#test various algorhythm for edge detection with bilateral filter
duck_mono = cv.cvtColor(pros, cv.COLOR_BGR2GRAY)
cv.imshow('sob', cv.Sobel(duck_mono, cv.CV_32F, 1, 1, ksize = 3))
cv.imshow('lap', cv.Laplacian(duck_mono, cv.CV_32F))
cv.imshow('can', cv.Canny(duck_mono, 60, 150))


cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(1)
