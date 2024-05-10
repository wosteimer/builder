from typing import Literal, Optional, Sequence, TypedDict
from typing_extensions import Unpack
from builder.base import (
    ContentTag,
    EmptyTag,
    Prop,
    Tag,
)


class GlobalProps(TypedDict, total=False):
    accesskey: str
    contenteditable: Literal["true", "false"]
    dir: Literal["ltr", "rtl", "auto"]
    draggable: Literal["true", "false", "auto"]
    enterkeyhint: str
    hidden: bool
    id: str
    inert: bool
    inputmode: Literal[
        "decimal",
        "email",
        "none",
        "numeric",
        "search",
        "tel",
        "text",
        "url",
    ]
    lang: str
    popover: bool
    spellcheck: Literal["true", "false"]
    tabindex: int
    title: str
    translate: Literal["yes", "no"]


class WindowEventProps(TypedDict, total=False):
    onafterprint: str
    onbeforeprint: str
    onbeforeunload: str
    onerror: str
    onhashchange: str
    onload: str
    onmessage: str
    onoffline: str
    ononline: str
    onpagehide: str
    onpageshow: str
    onpopstate: str
    onresize: str
    onstorage: str
    onunload: str


class EventProps(TypedDict, total=False):
    onblur: str
    onchange: str
    oncontextmenu: str
    onfocus: str
    oninput: str
    oninvalid: str
    onreset: str
    onsearch: str
    onselect: str
    onsubmit: str
    onkeydown: str
    onkeypress: str
    onkeyup: str
    onclick: str
    ondblclick: str
    onmousedown: str
    onmousemove: str
    onmouseout: str
    onmouseover: str
    onmouseup: str
    onwheel: str
    ondrag: str
    ondragend: str
    ondragenter: str
    ondragleave: str
    ondragover: str
    ondragstart: str
    ondrop: str
    onscroll: str
    oncopy: str
    oncut: str
    onpaste: str
    onabort: str
    oncanplay: str
    oncanplaythrough: str
    oncuechange: str
    ondurationchange: str
    onemptied: str
    onended: str
    onerror: str
    onloadeddata: str
    onloadedmetadata: str
    onloadstart: str
    onpause: str
    onplay: str
    onplaying: str
    onprogress: str
    onratechange: str
    onseeked: str
    onseeking: str
    onstalled: str
    onsuspend: str
    ontimeupdate: str
    onvolumechange: str
    onwaiting: str
    ontoggle: str


class DefaultProps(GlobalProps, EventProps, total=False, closed=True):
    __extra_items__: Prop


class DefaultContentTag(ContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        **props: Unpack[DefaultProps],
    ):
        super().__init__(children, classes, style, **props)


class DefaultEmptyTag(EmptyTag):
    def __init__(
        self,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        **props: Unpack[DefaultProps],
    ):
        super().__init__(classes, style, **props)
