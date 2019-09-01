from random import randint, random
from typing import Tuple

from PIL.Image import Image

from . import Noise


class BaseNoise:
    limits = None

    def __init__(self, high=30, low=0):
        self.low, self.high = sorted([float(low), float(high)])

    def process_page(self, page):
        level = (random() * (self.high - self.low) + self.low) / 100
        page.writer.apply_filter(Filter(level, self.limits))


@Noise.register("pepper")
class PepperNoise(BaseNoise):
    limits = (0, 199)


@Noise.register("salt")
class SaltNoise(BaseNoise):
    limits = (200, 255)


class Filter:
    def __init__(self, level: float, limits: Tuple[int, int]):
        self.level = level
        self.limits = limits

    def apply(self, image):
        if isinstance(image, Image):
            self.filter_pil_image(image)
        else:
            return TypeError(f"{type(image)} not supported")

    def filter_pil_image(self, image: Image):
        pixels = image.load()
        for y in range(image.height):
            for x in range(image.width):
                if random() < self.level:
                    pixels[x, y] = randint(*self.limits)
