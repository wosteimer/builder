from collections.abc import Callable
from functools import wraps
from typing import Concatenate, Optional
from uuid import uuid4

import sass

from builder.base import Tag

type Classes = Optional[list[str]]
type Contructor[**P] = Callable[Concatenate[Classes, P], Tag]


class Styler:
    __globals = ""
    __data = dict[str, str]()

    @staticmethod
    def set_globals(globals: str):
        Styler.__globals = globals

    @staticmethod
    def build_stylesheet() -> str:
        result = Styler.__globals
        result += "".join(
            [
                f".{class_name}{{{content}}}"
                for class_name, content in Styler.__data.items()
            ]
        )
        return sass.compile(string=result)

    @staticmethod
    def stylize[**P](tag: Contructor[P], style: str):
        class_name = f"bu-{str(uuid4()).split("-")[0]}"
        Styler.__data[class_name] = style

        @wraps(tag)
        def wrapper(classes: Classes = None, *args: P.args, **kwargs: P.kwargs):
            if classes != None:
                classes = [class_name, *classes]
            else:
                classes = [class_name]

            return tag(classes, *args, **kwargs)

        return wrapper
