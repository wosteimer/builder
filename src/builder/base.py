from __future__ import annotations
from abc import ABC, abstractmethod
from html import escape
from typing import (
    Optional,
    Sequence,
    override,
)

type Prop = float | int | bool | str


class Tag(ABC):
    @abstractmethod
    def build(self) -> str: ...


class ContentTag(Tag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        extra_props: Optional[dict[str, Prop]] = None,
        **props: Prop,
    ):
        self.__classes = classes
        self.__style = style
        self.__props = props
        self.__extra_props = extra_props
        self.__children = children

    @override
    def build(self) -> str:
        name = build_name(self.__class__.__name__)
        props = ""
        if self.__classes:
            props += build_classes(self.__classes)
        if self.__style:
            props += build_style(self.__style)
        if self.__extra_props:
            props += build_extra_props(self.__extra_props)
        props += build_props(self.__props)
        children = ""
        if self.__children:
            children = "".join([build_child(child) for child in self.__children])
        return f"<{name}{props}>{children}</{name}>"


class EmptyTag(Tag):
    def __init__(
        self,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        extra_props: Optional[dict[str, Prop]] = None,
        **props: Prop,
    ):
        self.__classes = classes
        self.__extra_props = extra_props
        self.__style = style
        self.__props = props

    @override
    def build(self) -> str:
        name = build_name(self.__class__.__name__)
        props = ""
        if self.__classes:
            props += build_classes(self.__classes)
        if self.__style:
            props += build_style(self.__style)
        if self.__extra_props:
            props += build_extra_props(self.__extra_props)
        props += build_props(self.__props)
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
    output = ""
    for key, value in props.items():
        if isinstance(value, bool):
            output += (" " + key.replace("_", "-")) if value else ""
        else:
            output += " " + key.replace("_", "-") + "=" + f'"{value}"'
    return output


def build_extra_props(props: dict[str, Prop]) -> str:
    output = ""
    for key, value in props.items():
        if isinstance(value, bool):
            output += " " + key if value else ""
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


def build_child(child: Tag | str, use_escape: bool = True) -> str:
    # fmt: off
    match child:
        case Tag(): return child.build()
        case str(): return (escape(child) if use_escape else child)
    # fmt: on
