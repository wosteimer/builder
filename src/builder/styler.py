import hashlib
from collections.abc import Callable
from functools import wraps
from typing import Concatenate, Optional
from uuid import uuid4

import sass
from minify_html import minify

type Classes = Optional[list[str]]
type Contructor[**P, R] = Callable[Concatenate[Classes, P], R]


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
        return minify(sass.compile(string=result), minify_css=True)

    @staticmethod
    def stylize[**P, R](tag: Contructor[P, R], style: str):
        class_name = f"bu-{hashlib.sha1(style.encode("UTF-8")).hexdigest()[:8]}"
        Styler.__data[class_name] = style

        @wraps(tag)
        def wrapper(classes: Classes = None, *args: P.args, **kwargs: P.kwargs) -> R:
            classes = [class_name, *classes] if classes != None else [class_name]
            return tag(classes, *args, **kwargs)

        return wrapper
