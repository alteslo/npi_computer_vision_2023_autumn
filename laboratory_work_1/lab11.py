import cv2
from matplotlib import pyplot as plt


def show(image):
    colors = ('b', 'g', 'r')
    fig, axs = plt.subplots(1, 3, figsize=(20, 10))

    for idx, color in enumerate(colors):
        axs[idx].hist(image[:, :, idx].ravel(), bins=256, color=color)
        axs[idx].set_xlim([0, 256])
        axs[idx].set_title(f'{color.upper()} Histogram')

    def move_event(event, x, y, flags, params):
        img = image.copy()
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        if event == cv2.EVENT_MOUSEMOVE:
            font = cv2.FONT_HERSHEY_SIMPLEX
            B, G, R = img[y, x]
            H, S, V = hsv_img[y, x]
            intensity = (int(R) + int(G) + int(B)) // 3
            coordinate = f'Coord=({x}, {y}),'
            rgb_value = ' '*20 + f'RGB=({R}, {G}, {B}),'
            hsv_value = ' '*40 + f'HSV=({H}, {S}, {V}),'
            intensity_value = ' '*60 + f', Intensity={intensity}'

            window = cv2.getRectSubPix(img, (25, 25), (x, y))
            mean, std_dev = cv2.meanStdDev(window)
            mean_b, mean_g, mean_r = mean.flatten()
            std_dev_b, std_dev_g, std_dev_r = std_dev.flatten()

            mean_values = f'Mean RGB=({round(mean_r, 2)},{round(mean_g, 2)},{round(mean_b, 2)}),'
            std_dev_values = f'Std_Dev RGB=({round(std_dev_r)},{round(std_dev_g)},{round(std_dev_b)})'

            cv2.putText(img, coordinate, (x+22, y), font, 0.4, (255, 255, 0), 1, cv2.LINE_8)
            cv2.putText(img, rgb_value, (x+22, y), font, 0.4, (0, 0, 255), 1, cv2.LINE_8)
            cv2.putText(img, hsv_value, (x+22, y), font, 0.4, (0, 255, 0), 1, cv2.LINE_8)
            cv2.putText(img, intensity_value, (x+22, y), font, 0.4, (255, 0, 0), 1, cv2.LINE_8)
            cv2.putText(img, mean_values, (x+22, y+22), font, 0.4, (255, 255, 255), 1, cv2.LINE_8)
            cv2.putText(img, ' '*35 + std_dev_values, (x+22, y+22), font, 0.4, (255, 255, 0), 1, cv2.LINE_8)

            cv2.imshow('Rectangle', window)
            cv2.imshow('Image', img)

    cv2.setMouseCallback('Image', move_event)

    plt.show()


if __name__ == '__main__':
    image = cv2.imread('./laboratory_work_1/img/image_1.png')
    cv2.imshow('Image', image)
    show(image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
