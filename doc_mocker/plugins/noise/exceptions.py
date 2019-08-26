class InvalidNoiseParameters(ValueError):
    def __init__(self, param):
        super().__init__(f"NoiseError: Invalid number of parameters provided [{param}]")


class UnknownNoiseFilter(ValueError):
    def __init__(self, name):
        super().__init__(f"NoiseError: Unknown noise filter [{name}]")
