import cv2
from matplotlib import pyplot as plt
from constants.constant import Images

# 2) отобразить гистограммы всех трех цветовых каналов изображения;


def show_three_channel_hist(image):
    image = cv2.imread(image)
    colors = ('b', 'g', 'r')

    for idx, color in enumerate(colors):
        histr = cv2.calcHist([image], [idx], None, [256], [0, 256])
        plt.plot(histr, color=color)
        plt.xlim([0, 256])
    plt.show()


if __name__ == '__main__':
    show_three_channel_hist(Images.IMAGE_1)
