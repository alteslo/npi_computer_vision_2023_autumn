import cv2
from constants.constant import Images

# 3) перемещая курсор мыши поверх изображения, для текущего пикселя показать:
#    а) значение цвета пикселя в формате RGB;
#    б) значение цвета пикселя в формате HSV;
#    в) интенсивность пикселя (усреднение по всем компонентам цвета);


def move_event(event, x, y, flags, params):
    imgk = img.copy()
    # checking for right mouse clicks
    if event == cv2.EVENT_MOUSEMOVE:

        # displaying the coordinates
        # on the Shell
        # print(x, ' ', y)

        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (x, y)
        B = imgk[y, x, 0]
        G = imgk[y, x, 1]
        R = imgk[y, x, 2]

    cv2.putText(imgk, f'(x, y)=({x}, {y})', org, font, 1, (255, 255, 255), 1, cv2.LINE_8)
    cv2.putText(imgk, '                  ,R={}'.format(R),
                org, font, 1, (0, 0, 255), 1, cv2.LINE_8)
    cv2.putText(imgk, '                         ,G={}'.format(G),
                org, font, 1, (0, 255, 0), 1, cv2.LINE_8)
    cv2.putText(imgk, '                                 ,B={}'.format(
        B), org, font, 1, (255, 0, 0), 1, cv2.LINE_8)
    cv2.imshow('image', imgk)


# reading the image
img = cv2.imread(Images.IMAGE_1)

# displaying the image
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow('image', img)

# setting mouse hadler for the image
# and calling the click_event() function
cv2.setMouseCallback('image', move_event)

# wait for a key to be pressed to exit
cv2.waitKey(0)

# close the window
cv2.destroyAllWindows()
