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
            page = processor.process_page(page)
        return page

    @classmethod
    def register(cls, name: str) -> Callable:
        def register_class(class_: Type) -> Type:
            cls._classes[name] = class_
            return class_

        return register_class


arguments = [
    (
        ("--noise",),
        {
            "help": "Apply multiple noise filters. Supported: `pepper[:n][:m]`",
            "nargs": "+",
            "default": [],
        },
    )
]

cls = Noise

__import__("doc_mocker.plugins.noise.pepper")
