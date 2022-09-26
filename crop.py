import cv2
import numpy as np
import argparse

par = argparse.ArgumentParser()
par.add_argument('-i', '--image' , help="Image",)
img = cv2.imread('img.jpg')


h=50
crop = img[h:, h:]

cv2.imshow('image befor', img)
cv2.imshow('cropped image', crop)

cv2.waitKey(0) 
