import cv2
from matplotlib import pyplot as plt
import numpy as np


def show_result(image_path):
    image = cv2.imread(image_path)
    plt.figure(figsize=(20, 10))

    transformed_linear = cv2.convertScaleAbs(image, alpha=1.5, beta=50)

    lut = np.zeros(shape=256, dtype=np.uint8)
    for i in range(256):
        lut[i] = 255 * pow(float(i) / 255, 5)
    transformed_nonlinear = cv2.LUT(image, lut)

    median_image = cv2.medianBlur(image, 5)
    gaussian_image = cv2.GaussianBlur(image, (5, 5), 0)
    bilateral_image = cv2.bilateralFilter(
        image, 9, 75, 75)

    kernel_sharpening = np.array([[-1, -1, -1],
                                  [-1, 9, -1],
                                  [-1, -1, -1]])
    sharpened_image = cv2.filter2D(image, -1, kernel_sharpening)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    salt_and_pepper_noise = np.zeros(shape=gray_image.shape, dtype=np.uint8)
    cv2.randu(salt_and_pepper_noise, 0, 255)
    salt = salt_and_pepper_noise > 250
    pepper = salt_and_pepper_noise < 5
    salt_and_pepper_image = image.copy()
    salt_and_pepper_image[salt] = 255
    salt_and_pepper_image[pepper] = 0

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    gauss_noise = np.zeros(shape=hsv_image.shape, dtype=np.uint8)
    cv2.randn(gauss_noise, 0, 100)
    gauss_noise_image = cv2.add(hsv_image, gauss_noise)
    gauss_noise_image = cv2.cvtColor(
        gauss_noise_image, cv2.COLOR_HSV2BGR)

    colors = ('b', 'g', 'r')

    plt.subplot(341)
    plt.title('Исходное изображение')
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    plt.subplot(342)
    plt.title('Шум Гаусса')
    plt.imshow(cv2.cvtColor(gauss_noise_image, cv2.COLOR_BGR2RGB))

    plt.subplot(343)
    plt.title('Шум "соль и перец"')
    plt.imshow(cv2.cvtColor(salt_and_pepper_image, cv2.COLOR_BGR2RGB))

    plt.subplot(344)
    plt.title('Медианный фильтр')
    plt.imshow(cv2.cvtColor(median_image, cv2.COLOR_BGR2RGB))

    plt.subplot(345)
    plt.title('Гауссов фильтр')
    plt.imshow(cv2.cvtColor(gaussian_image, cv2.COLOR_BGR2RGB))

    plt.subplot(346)
    plt.title('Билатеральный фильтр')
    plt.imshow(cv2.cvtColor(bilateral_image, cv2.COLOR_BGR2RGB))

    plt.subplot(347)
    plt.title('Увеличение резкости')
    plt.imshow(cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2RGB))

    plt.subplot(348)
    plt.title('Гистограмма исходного изображения')
    for idx, color in enumerate(colors):
        hist = cv2.calcHist([image], [idx], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])

    plt.subplot(349)
    plt.title('Гистограмма линейно трансформированного изображения')
    for idx, color in enumerate(colors):
        hist = cv2.calcHist([transformed_linear], [
            idx], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])

    plt.subplot(3, 4, 10)
    plt.title('Гистограмма нелинейно трансформированного изображения')
    for idx, color in enumerate(colors):
        hist = cv2.calcHist([transformed_nonlinear], [
            idx], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])

    plt.show()


if __name__ == '__main__':
    show_result('./laboratory_work_1/img/image_1.png')
