import cv2
from matplotlib import pyplot as plt
from constants.constant import Images
import numpy as np


def show_hists(image, alpha, beta, gamma):
    plt.figure(figsize=(20, 10))

    # выполнить линейное преобразование
    transformed_linear = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

    # выполнить нелинейное преобразование
    lut = np.zeros(shape=256, dtype=np.uint8)
    for i in range(256):
        lut[i] = 255 * pow(float(i) / 255, gamma)
    transformed_nonlinear = cv2.LUT(image, lut)

    # добавить гауссов шум
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # Чтобы избавиться от ухода в синий перевел в hsv
    gauss_noise = np.zeros(shape=hsv_image.shape, dtype=np.uint8)
    cv2.randn(gauss_noise, 0, 100)
    gauss_noise_image = cv2.add(hsv_image, gauss_noise)
    gauss_noise_image = cv2.cvtColor(gauss_noise_image, cv2.COLOR_HSV2BGR)  # И обратно в bgr

    # добавить шум соль и перец
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    salt_and_pepper_noise = np.zeros(shape=gray.shape, dtype=np.uint8)
    cv2.randu(salt_and_pepper_noise, 0, 255)
    salt = salt_and_pepper_noise > 250
    pepper = salt_and_pepper_noise < 5
    salt_and_pepper_image = image.copy()
    salt_and_pepper_image[salt] = 255
    salt_and_pepper_image[pepper] = 0

    median_image = cv2.medianBlur(image, 5)  # медианный фильтр
    gaussian_image = cv2.GaussianBlur(image, (5, 5), 0)  # фильтр Гаусса
    bilateral_image = cv2.bilateralFilter(image, 9, 75, 75)  # билатеральный фильтр

    # увеличить резкость изображения
    kernel_sharpening = np.array([[-1, -1, -1],
                                  [-1, 9, -1],
                                  [-1, -1, -1]])
    sharpened_image = cv2.filter2D(image, -1, kernel_sharpening)

    colors = ('b', 'g', 'r')

    # стандартное изображение
    plt.subplot(341)
    plt.title('Original Image')
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # изображение с гауссовым шумом
    plt.subplot(342)
    plt.title('Noise Gaussian')
    plt.imshow(cv2.cvtColor(gauss_noise_image, cv2.COLOR_BGR2RGB))

    # изображение с шумом соль и перец
    plt.subplot(343)
    plt.title('Noise salt and pepper')
    plt.imshow(cv2.cvtColor(salt_and_pepper_image, cv2.COLOR_BGR2RGB))

    # медианный фильтр
    plt.subplot(344)
    plt.title('Median Filter')
    plt.imshow(cv2.cvtColor(median_image, cv2.COLOR_BGR2RGB))

    # фильтр Гаусса
    plt.subplot(345)
    plt.title('Gaussian Filter')
    plt.imshow(cv2.cvtColor(gaussian_image, cv2.COLOR_BGR2RGB))

    # билатеральный фильтр
    plt.subplot(346)
    plt.title('Bilateral Filter')
    plt.imshow(cv2.cvtColor(bilateral_image, cv2.COLOR_BGR2RGB))

    # изображение с повышенной резкостью
    plt.subplot(347)
    plt.title('Sharpened Image')
    plt.imshow(cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2RGB))

    # гистограммы до преобразования
    plt.subplot(348)
    plt.title('Histogram of Original Image')
    for idx, color in enumerate(colors):
        histr = cv2.calcHist([image], [idx], None, [256], [0, 256])
        plt.plot(histr, color=color)
        plt.xlim([0, 256])

    # гистограммы после линейного преобразования
    plt.subplot(349)
    plt.title('Histogram of Linear Transformed Image')
    for idx, color in enumerate(colors):
        histr = cv2.calcHist([transformed_linear], [
                             idx], None, [256], [0, 256])
        plt.plot(histr, color=color)
        plt.xlim([0, 256])

    # гистограммы после нелинейного преобразования
    plt.subplot(3, 4, 10)
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
    show_hists(image, 1.5, 50, 5)


if __name__ == '__main__':
    show_lab_two(Images.IMAGE_1)
