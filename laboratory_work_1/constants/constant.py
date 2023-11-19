from dataclasses import dataclass


@dataclass
class Images:
    IMAGE_1 = './laboratory_work_1/img/image_1.png'


@dataclass
class RGB:
    WHITE = (255, 255, 255)
    RED = (0, 0, 255)
    GREEN = (0, 255, 0)
    BLUE = (255, 0, 0)
