from __future__ import annotations

from abc import ABC, abstractmethod
from html import escape
from typing import Optional, Sequence, override

type Prop = float | int | bool | str


class Tag(ABC):
    @abstractmethod
    def build(self) -> str: ...


class Text(Tag):
    def __init__(self, text: str, escape: bool = True):
        self.__text = text
        self.__escape = escape

    @override
    def build(self) -> str:
        return escape(self.__text) if self.__escape else self.__text


class ContentTag(Tag):
    def __init__(
        self,
        classes: Optional[Sequence[str]] = None,
        children: Optional[Sequence[Tag]] = None,
        style: Optional[dict[str, str]] = None,
        extra_props: Optional[dict[str, Prop]] = None,
        **props: Prop,
    ):
        self.__children = children if children != None else list[Tag]()
        self.__classes = classes if classes != None else list[str]()
        self.__style = style if style != None else {}
        self.__props = props
        self.__extra_props = extra_props if extra_props != None else {}

    @override
    def build(self) -> str:
        name = build_name(self.__class__.__name__)
        props = ""
        props += build_classes(self.__classes)
        props += build_style(self.__style)
        props += build_props({**self.__extra_props, **self.__props})
        children = "".join([child.build() for child in self.__children])
        return f"<{name}{props}>{children}</{name}>"


class EmptyTag(Tag):
    def __init__(
        self,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        extra_props: Optional[dict[str, Prop]] = None,
        **props: Prop,
    ):
        self.__classes = classes if classes != None else list[str]()
        self.__style = style if style != None else {}
        self.__props = props
        self.__extra_props = extra_props if extra_props != None else {}

    @override
    def build(self) -> str:
        name = build_name(self.__class__.__name__)
        props = ""
        props += build_classes(self.__classes)
        props += build_style(self.__style)
        props += build_props({**self.__extra_props, **self.__props})
        return f"<{name}{props}/>"


def build_name(name: str) -> str:
    result = ""
    for index, letter in enumerate(name):
        if letter.isupper():
            if index == 0:
                result += letter.lower()
            else:
                result += f"-{letter.lower()}"
        else:
            result += letter

    return result


def build_props(props: dict[str, Prop]) -> str:
    if len(props) == 0:
        return ""
    output = ""
    for key, value in props.items():
        if isinstance(value, bool):
            output += (" " + key) if value else ""
        else:
            output += " " + key + "=" + f'"{value}"'
    return output


def build_classes(classes: Sequence[str]) -> str:
    if len(classes) == 0:
        return ""
    return " class=" + f'"{" ".join(classes)}"'


def build_style(style: dict[str, str]) -> str:
    if style == {}:
        return ""
    style_content = "".join([f"{key}:{value};" for key, value in style.items()])
    return " style=" + f'"{style_content}"'
