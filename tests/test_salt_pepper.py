from unittest import TestCase

from doc_mocker.plugins.noise import Noise


class SaltPepperNoise(TestCase):
    def test_noise_are_registered(self):
        self.assertIn("salt", Noise._classes)
        self.assertIn("pepper", Noise._classes)
