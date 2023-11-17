import cv2
from constants.constant import Images


def show_image(image):
    image = cv2.imread(image)
    assert image is not None, "file could not be read"
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    show_image(Images.IMAGE_1)
