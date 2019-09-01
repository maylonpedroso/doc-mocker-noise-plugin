from argparse import Namespace
from typing import Type, Callable

from doc_mocker.plugins.noise.exceptions import (
    InvalidNoiseParameters,
    UnknownNoiseFilter,
)


class Noise:
    _classes = {}

    def __init__(self, args: Namespace) -> None:
        self._processors = []
        for noise in args.noise:
            name, *options = noise.split(":")
            try:
                self._processors.append(self._classes[name](*options))
            except TypeError:
                raise InvalidNoiseParameters(noise)
            except KeyError:
                raise UnknownNoiseFilter(name)

    def process_page(self, page):
        for processor in self._processors:
            processor.process_page(page)

    @classmethod
    def register(cls, name: str) -> Callable:
        def register_class(class_: Type) -> Type:
            cls._classes[name] = class_
            return class_

        return register_class

    @classmethod
    def noises(cls):
        return cls._classes.keys()


__import__("doc_mocker.plugins.noise.salt_pepper")

arguments = [
    (
        ("--noise",),
        {
            "help": f"Apply multiple noise filters. Supported: {', '.join(Noise.noises())}",
            "nargs": "+",
            "default": [],
        },
    )
]

cls = Noise
