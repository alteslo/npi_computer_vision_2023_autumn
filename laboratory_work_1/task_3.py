import cv2
from constants.constant import Images, RGB

# 3) перемещая курсор мыши поверх изображения, для текущего пикселя показать:
#    а) значение цвета пикселя в формате RGB;
#    б) значение цвета пикселя в формате HSV;
#    в) интенсивность пикселя (усреднение по всем компонентам цвета);


def move_event(event, x, y, flags, params):
    imgk = img.copy()
    # checking for right mouse clicks
    if event == cv2.EVENT_MOUSEMOVE:
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (x, y)
        B = imgk[y, x, 0]
        G = imgk[y, x, 1]
        R = imgk[y, x, 2]

        coordinate = f'(x, y)=({x}, {y})'
        red_value = ' '*(len(coordinate) + 1) + f', R={R}'
        green_value = ' '*(len(red_value) + 1) + f', G={G}'
        blue_value = ' '*(len(green_value) + 1) + f', B={B}'

        cv2.putText(imgk, coordinate, org, font, 0.35, RGB.WHITE, 1, cv2.LINE_8)

        cv2.putText(imgk, red_value, org, font, 0.35, RGB.RED, 1, cv2.LINE_8)
        cv2.putText(imgk, green_value, org, font, 0.35, RGB.GREEN, 1, cv2.LINE_8)
        cv2.putText(imgk, blue_value, org, font, 0.35, RGB.BLUE, 1, cv2.LINE_8)

        cv2.imshow('image', imgk)


# reading the image
img = cv2.imread(Images.IMAGE_1)
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.setMouseCallback('image', move_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
