import cv2
import numpy as np
import os

img = cv2.imread('C:/work/defects_pic/figs_bzt/149.png')
img_gs = cv2.imread('C:/work/defects_pic/figs_bzt/149.png', cv2.IMREAD_GRAYSCALE)
_, binary = cv2.threshold(gray)