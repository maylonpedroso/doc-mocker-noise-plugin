from random import randint, random

from PIL.Image import Image

from . import Noise


@Noise.register("pepper")
class SaltNoise:
    def __init__(self, high=30, low=0):
        self.low, self.high = sorted([float(low), float(high)])

    def process_page(self, page):
        level = (random() * (self.high - self.low) + self.low) / 100
        page.writer.apply_filter(PepperFilter(level))


class PepperFilter:
    def __init__(self, level: float):
        self.level = level

    def apply(self, image):
        if isinstance(image, Image):
            self.filter_pil_image(image)
        else:
            return TypeError(f"{type(image)} not supported by pepper filter")

    def filter_pil_image(self, image: Image):
        pixels = image.load()
        for y in range(image.height):
            for x in range(image.width):
                if random() < self.level:
                    pixels[x, y] = randint(0, 200)
