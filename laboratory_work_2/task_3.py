import cv2
from constants.constant import Images, RGB

# 3) перемещая курсор мыши поверх изображения, для текущего пикселя показать:
#    а) значение цвета пикселя в формате RGB;
#    б) значение цвета пикселя в формате HSV;
#    в) интенсивность пикселя (усреднение по всем компонентам цвета);


def show_pixel_info(image):
    img = cv2.imread(image)
    assert img is not None, "file could not be read"
    cv2.imshow('image', img)

    def move_event(event, x, y, flags, params):
        """Обработчик передвижения мышки"""
        imgk = img.copy()
        hsv_img = cv2.cvtColor(imgk, cv2.COLOR_BGR2HSV)

        # Отслеживаем перемещение курсорамыши
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
            rgb_value = ' '*(len(coordinate) + 1) + f', RGB=({R},{G},{B})'
            hsv_value = ' '*(len(rgb_value) + 1) + f', HSV=({H},{S},{V})'
            intensity_value = ' '*(len(hsv_value) + 2) + f', Intensity={intensity}'

            cv2.putText(imgk, coordinate, org, font, 0.35, RGB.WHITE, 1, cv2.LINE_8)

            cv2.putText(imgk, rgb_value, org, font, 0.35, RGB.RED, 1, cv2.LINE_8)
            cv2.putText(imgk, hsv_value, org, font, 0.35, RGB.GREEN, 1, cv2.LINE_8)
            cv2.putText(imgk, intensity_value, org, font, 0.35, RGB.BLUE, 1, cv2.LINE_8)

            cv2.imshow('image', imgk)

    cv2.setMouseCallback('image', move_event)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    show_pixel_info(Images.IMAGE_1)
