import cv2
import numpy as np
import os

img = cv2.imread('C:/work/defects_pic/figs_bzt/149.png')
img_gs = cv2.imread('C:/work/defects_pic/figs_bzt/149.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('r', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
kernel1 = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
kernel2 = np.transpose([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
t1 = cv2.filter2D(img_gs, -1, kernel1)
t2 = cv2.filter2D(img_gs, -1, kernel2)
cv2.imshow('1', t1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('2', t2)
cv2.waitKey(0)
cv2.destroyAllWindows()
path = 'C:/Users/ThinkPad/Desktop/1234'
cv2.imwrite(os.path.join(path, 'pic1.jpg'), t1)
cv2.imwrite(os.path.join(path, 'pic2.jpg'), t2)
cv2.waitKey()

