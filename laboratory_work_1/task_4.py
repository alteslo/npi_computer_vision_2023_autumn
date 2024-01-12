import cv2
from constants.constant import RGB, Images


# 4) вырезать окно заданного размера (например 25х25) с центром в текущем
#    пикселе (т.е. пиксель под курсором мыши является центром окна),
#    отобразить содержимое окна, для
#    этого окна вычислить по каждой компоненте цвета:
# а) среднее значение;
# б) стандартное отклонение.


def show_image(image):
    img = cv2.imread(image)
    assert img is not None, "file could not be read"
    cv2.imshow('Image', img)

    def click_event(event, x, y, flags, params):
        """Обработчик клика левой кнопки мыши"""
        imgk = img.copy()
        window_size = 25

        # Отследиваем щелчок левой клавиши мыши
        if event == cv2.EVENT_LBUTTONDOWN:
            font = cv2.FONT_HERSHEY_SIMPLEX
            org = (x, y)

            # Получаем окно размером 25x25 в центре (x, y)
            window = cv2.getRectSubPix(imgk, (window_size, window_size), (x, y))

            mean, std_dev = cv2.meanStdDev(window)
            mean_b, mean_g, mean_r = mean.flatten()
            std_dev_b, std_dev_g, std_dev_r = std_dev.flatten()

            mean_values = f', Mean RGB=({round(mean_r, 2)}, {round(mean_g, 2)}, {round(mean_b, 2)})'
            std_dev_values = ' ' * (len(mean_values) + 3) + f', Std Dev RGB=({round(std_dev_r)},{round(std_dev_g)},{round(std_dev_b)})'

            cv2.putText(imgk, mean_values, org, font, 0.35, RGB.WHITE, 1, cv2.LINE_8)
            cv2.putText(imgk, std_dev_values, org, font,
                        0.35, RGB.GREEN, 1, cv2.LINE_8)

            cv2.imshow('window', window)
            cv2.imshow('Image', imgk)

    cv2.setMouseCallback('Image', click_event)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    show_image(Images.IMAGE_1)
