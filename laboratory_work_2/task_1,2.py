import cv2
from matplotlib import pyplot as plt
from constants.constant import Images
import numpy as np


def show_hists(image, alpha, beta, gamma):

    # выполнить линейное преобразование
    transformed_linear = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

    # выполнить нелинейное преобразование
    lut = np.zeros(256, dtype=np.uint8)
    for i in range(256):
        lut[i] = 255 * pow(float(i) / 255, gamma)
    transformed_nonlinear = cv2.LUT(image, lut)

    # добавить гауссов шум
    noise = np.zeros(image.shape, np.uint8)
    cv2.randn(noise, 0, 100)
    noisy_image = cv2.add(image, noise)

    # добавить шум соль и перец
    salt_and_pepper_noise = np.zeros(image.shape, np.uint8)
    cv2.randu(salt_and_pepper_noise, 0, 255)
    salt = salt_and_pepper_noise > 250
    pepper = salt_and_pepper_noise < 5
    salt_and_pepper_image = image.copy()
    salt_and_pepper_image[salt] = 255
    salt_and_pepper_image[pepper] = 0

    # отобразить гистограммы до и после преобразования
    colors = ('b', 'g', 'r')

    plt.figure(figsize=(20, 10))

    # стандартное изображение
    plt.subplot(231)
    plt.title('Original Image')
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # изображение с гауссовым шумом
    plt.subplot(232)
    plt.title('Noisy Image')
    plt.imshow(cv2.cvtColor(noisy_image, cv2.COLOR_BGR2RGB))

    # изображение с шумом соль и перец
    plt.subplot(233)
    plt.title('Noise salt and pepper')
    plt.imshow(cv2.cvtColor(salt_and_pepper_image, cv2.COLOR_BGR2RGB))

    # гистограммы до преобразования
    plt.subplot(234)
    plt.title('Histogram of Original Image')
    for idx, color in enumerate(colors):
        histr = cv2.calcHist([image], [idx], None, [256], [0, 256])
        plt.plot(histr, color=color)
        plt.xlim([0, 256])

    # гистограммы после линейного преобразования
    plt.subplot(235)
    plt.title('Histogram of Linear Transformed Image')
    for idx, color in enumerate(colors):
        histr = cv2.calcHist([transformed_linear], [
                             idx], None, [256], [0, 256])
        plt.plot(histr, color=color)
        plt.xlim([0, 256])

    # гистограммы после нелинейного преобразования
    plt.subplot(236)
    plt.title('Histogram of Nonlinear Transformed Image')
    for idx, color in enumerate(colors):
        histr = cv2.calcHist([transformed_nonlinear], [
                             idx], None, [256], [0, 256])
        plt.plot(histr, color=color)
        plt.xlim([0, 256])

    plt.show()


def show_lab_two(image):
    image = cv2.imread(image)
    assert image is not None, "file could not be read"
    show_hists(image, 1.5, 50, 10)


if __name__ == '__main__':
    show_lab_two(Images.IMAGE_1)
