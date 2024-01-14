import cv2
import numpy as np
from constants.constant import Images
from constants.constant import RGB


# https://docs.opencv.org/3.4/d9/db0/tutorial_hough_lines.html

def show_image(image):
    image = cv2.imread(image)
    assert image is not None, "file could not be read"
    # преобразовать изображение в оттенки серого
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # применить фильтр Гаусса для сглаживания изображения
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # применить алгоритм Canny для обнаружения границ на изображении
    edges = cv2.Canny(blurred, 70, 250, apertureSize=3)

    # применить преобразование Хафа для поиска линий и окружностей на изображении
    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=60, minRadius=0, maxRadius=100)
    lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=30, minLineLength=40, maxLineGap=5)

    # lines = cv2.HoughLines(edges, rho=1, theta=np.pi / 180, threshold=130)

    # отобразить найденные линии и окружности на изображении
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(image, (x, y), r, RGB.GREEN, 2)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(image, (x1, y1), (x2, y2), RGB.RED, 2)

    # if lines is not None:
    #     for line in lines:
    #         rho, theta = line[0]
    #         a = np.cos(theta)
    #         b = np.sin(theta)
    #         x0 = a * rho
    #         y0 = b * rho
    #         x1 = int(x0 + 1000 * (-b))
    #         y1 = int(y0 + 1000 * (a))
    #         x2 = int(x0 - 1000 * (-b))
    #         y2 = int(y0 - 1000 * (a))
    #         cv2.line(image, (x1, y1), (x2, y2), RGB.RED, 2)

    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    show_image(Images.IMAGE_1)
