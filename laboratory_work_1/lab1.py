import cv2
from constants.constant import RGB, Images
from matplotlib import pyplot as plt


def show_pixel_info(image):
    def move_event(event, x, y, flags, params):
        """Обработчик передвижения мышки"""
        imgk = image.copy()
        hsv_img = cv2.cvtColor(imgk, cv2.COLOR_BGR2HSV)

        # Отслеживаем перемещение курсора мыши
        if event == cv2.EVENT_MOUSEMOVE:
            font = cv2.FONT_HERSHEY_SIMPLEX
            org = (x, y)

            # Получение значения пикселя в формате RGB
            B = imgk[y, x, 0]
            G = imgk[y, x, 1]
            R = imgk[y, x, 2]

            # Получение значения пикселя в формате HSV
            H = hsv_img.item(x, y, 0)
            S = hsv_img.item(x, y, 1)
            V = hsv_img.item(x, y, 2)

            # Интенсивность пикселя
            intensity = (int(R) + int(G) + int(B)) // 3

            coordinate = f'(x, y)=({x}, {y})'
            rgb_value = ' '*(len(coordinate) + 1) + \
                f', RGB=({R}, {G}, {B})'
            hsv_value = ' '*(len(rgb_value) + 1) + \
                f', HSV=({H}, {S}, {V})'
            intensity_value = ' '*(len(hsv_value) + 2) + \
                f', Intensity={intensity}'

            cv2.putText(imgk, coordinate, org, font,
                        0.35, RGB.WHITE, 1, cv2.LINE_8)

            cv2.putText(imgk, rgb_value, org, font,
                        0.35, RGB.RED, 1, cv2.LINE_8)
            cv2.putText(imgk, hsv_value, org, font,
                        0.35, RGB.GREEN, 1, cv2.LINE_8)
            cv2.putText(imgk, intensity_value, org, font,
                        0.35, RGB.BLUE, 1, cv2.LINE_8)

            # Вырезаем окно размером 25х25 с центром в текущем пикселе
            window = cv2.getRectSubPix(imgk, (25, 25), (x, y))

            # Вычисляем среднее значение и стандартное отклонение по каждой компоненте цвета
            mean, std_dev = cv2.meanStdDev(window)
            mean_b, mean_g, mean_r = mean.flatten()
            std_dev_b, std_dev_g, std_dev_r = std_dev.flatten()

            mean_values = f', Mean RGB=({round(mean_r, 2)}, {round(mean_g, 2)}, {round(mean_b, 2)})'
            std_dev_values = ' ' * \
                (len(mean_values) + 3) + \
                f', Std Dev RGB=({round(std_dev_r)},{round(std_dev_g)},{round(std_dev_b)})'

            cv2.putText(window, mean_values, (5, 15), font,
                        0.1, RGB.WHITE, 1, cv2.LINE_8)
            cv2.putText(window, std_dev_values, (5, 30), font,
                        0.1, RGB.GREEN, 1, cv2.LINE_8)

            cv2.imshow('Window', window)
            cv2.imshow('Image', imgk)

    cv2.setMouseCallback('Image', move_event)


def show_image_and_hists(image):
    colors = ('b', 'g', 'r')
    fig = plt.figure(figsize=(20, 10))

    # Отображение гистограммы каждого цветового канала
    for idx, color in enumerate(colors):
        ax = fig.add_subplot(1, 3, idx+1)
        histr = cv2.calcHist([image], [idx], None, [256], [0, 256])
        ax.plot(histr, color=color)
        ax.set_xlim([0, 256])
        ax.set_title(f'{color.upper()} Histogram')

    # Отображение информации о пикселе при перемещении курсора мыши
    show_pixel_info(image)

    plt.show()


if __name__ == '__main__':
    image = cv2.imread(Images.IMAGE_1)
    assert image is not None, "file could not be read"
    cv2.imshow('Image', image)
    show_image_and_hists(image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
