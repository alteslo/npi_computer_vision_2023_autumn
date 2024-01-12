import cv2
from matplotlib import pyplot as plt
from constants.constant import Images


def show_hists(image, alpha, beta):

    # выполнить линейное преобразование
    transformed = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

    # отобразить гистограммы до и после преобразования
    colors = ('b', 'g', 'r')

    plt.figure(figsize=(10, 5))

    # гистограммы до преобразования
    plt.subplot(121)
    plt.title('Histogram of Original Image')
    for idx, color in enumerate(colors):
        histr = cv2.calcHist([image], [idx], None, [256], [0, 256])
        plt.plot(histr, color=color)
        plt.xlim([0, 256])

    # гистограммы после преобразования
    plt.subplot(122)
    plt.title('Histogram of Transformed Image')
    for idx, color in enumerate(colors):
        histr = cv2.calcHist([transformed], [idx], None, [256], [0, 256])
        plt.plot(histr, color=color)
        plt.xlim([0, 256])

    plt.show()


def show_lab_two(image):
    image = cv2.imread(image)
    assert image is not None, "file could not be read"
    show_hists(image, 1.5, 50)


if __name__ == '__main__':
    show_lab_two(Images.IMAGE_1)
