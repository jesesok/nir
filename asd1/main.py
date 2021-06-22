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


class ImageHandler():
    """ Содержит базовый набор функций для обработки изображения
    и поиска дефектных семян на нем"""

    def apply_bilateral_filter(self, image):
        bilateral = cv2.bilateralFilter(image, 9, 75, 75)
        return bilateral

    def mark_seeds_by_counters(self, image_gray, origin, min_val: int, max_val: int):
        """ Ищет контуры объектов, "замыкает" их. """

        countered_image = cv2.Canny(image_gray, min_val, max_val)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        closed_countered_image = cv2.morphologyEx(countered_image, cv2.MORPH_CLOSE, kernel)
        counturs, hierarchy = cv2.findContours(closed_countered_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        for countur in counturs:
            try:
                perimetr = cv2.arcLength(countur, True)
                approx = cv2.approxPolyDP(countur, 0.02 * perimetr, True)
                original = cv2.drawContours(origin, [approx], -1, (0, 255, 0), 1)
            except Exception as err:
                print(err)
        return origin

