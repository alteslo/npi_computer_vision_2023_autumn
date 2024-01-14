import cv2
import numpy as np


def show_result(image_path):
    image = cv2.imread(image_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(
        gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    kernel = np.ones((5, 5), np.uint8)
    opening = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel, iterations=2)
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(
        opening)

    colors = np.random.randint(0, 255, size=(num_labels, 3), dtype=np.uint8)
    for i in range(1, num_labels):
        color = tuple(map(int, colors[i]))
        x, y, w, h, area = stats[i]
        cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)

    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    show_result('./laboratory_work_3/img/image_1.png')
