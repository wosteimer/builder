from datetime import datetime as Datetime
from typing import Literal, Optional, Sequence

from typing_extensions import Unpack

from builder.base import ContentTag, EmptyTag, Prop, Tag

from .default import (
    DefaultContentTag,
    DefaultEmptyTag,
    DefaultProps,
    EventProps,
    GlobalProps,
    WindowEventProps,
)


class H1(DefaultContentTag): ...


class H2(DefaultContentTag): ...


class H3(DefaultContentTag): ...


class H4(DefaultContentTag): ...


class H5(DefaultContentTag): ...


class H6(DefaultContentTag): ...


class AProps(GlobalProps, EventProps, closed=True, total=False):
    download: str
    href: str
    hreflang: str
    media: str
    ping: str
    referrerpolicy: Literal[
        "no-referrer",
        "no-referrer-when-downgrade",
        "origin",
        "origin-when-cross-origin",
        "same-origin",
        "strict-origin-when-cross-origin",
        "unsafe-url",
    ]
    rel: Literal[
        "alternate",
        "author",
        "bookmark",
        "external",
        "help",
        "license",
        "next",
        "nofollow",
        "noreferrer",
        "noopener",
        "prev",
        "search",
        "tag",
    ]
    target: Literal[
        "_blank",
        "_parent",
        "_self",
        "_top",
    ]
    type: str
    __extra_items__: Prop


class A(ContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        extra_props: Optional[dict[str, Prop]] = None,
        **props: Unpack[AProps],
    ):
        super().__init__(children, classes, style, extra_props, **props)


class Abbr(DefaultContentTag): ...


class Address(DefaultContentTag): ...


class AreaProps(GlobalProps, EventProps, closed=True, total=False):
    alt: str
    coords: str
    download: str
    href: str
    hreflang: str
    media: str
    referrerpolicy: Literal[
        "no-referrer",
        "no-referrer-when-downgrade",
        "origin",
        "origin-when-cross-origin",
        "same-origin",
        "strict-origin-when-cross-origin",
        "unsafe-url",
    ]
    rel: Literal[
        "alternate",
        "author",
        "bookmark",
        "help",
        "license",
        "next",
        "nofollow",
        "noreferrer",
        "prefetch",
        "prev",
        "search",
        "tag",
    ]
    shape: Literal[
        "default",
        "rect",
        "circle",
        "poly",
    ]
    target: (
        Literal[
            "_blank",
            "_parent",
            "_self",
            "_top",
        ]
        | str
    )
    type: str
    __extra_items__: Prop


class Area(EmptyTag):
    def __init__(
        self,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        extra_props: Optional[dict[str, Prop]] = None,
        **props: Unpack[AreaProps],
    ):
        super().__init__(classes, style, extra_props, **props)


class Article(DefaultContentTag): ...


class Aside(DefaultContentTag): ...


class AudioProps(GlobalProps, EventProps, closed=True, total=False):
    autoplay: bool
    controls: bool
    loop: bool
    muted: bool
    preload: Literal[
        "auto",
        "metadata",
        "none",
    ]
    src: str
    __extra_items__: Prop


class Audio(ContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        extra_props: Optional[dict[str, Prop]] = None,
        **props: Unpack[AudioProps],
    ):
        super().__init__(children, classes, style, extra_props, **props)


class B(DefaultContentTag): ...


class BaseProps(GlobalProps, EventProps, closed=True, total=False):
    href: str
    target: Literal[
        "_blank",
        "_parent",
        "_self",
        "_top",
    ]
    __extra_items__: Prop


class Base(EmptyTag):
    def __init__(
        self,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        extra_props: Optional[dict[str, Prop]] = None,
        **props: Unpack[BaseProps],
    ):
        super().__init__(classes, style, extra_props, **props)


class Bdi(DefaultContentTag): ...


class Bdo(DefaultContentTag): ...


class BlockquoteProps(GlobalProps, EventProps, closed=True, total=False):
    cite: str
    __extra_items__: Prop


class Blockquote(ContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        extra_props: Optional[dict[str, Prop]] = None,
        **props: Unpack[BlockquoteProps],
    ):
        super().__init__(children, classes, style, extra_props, **props)


class BodyProps(GlobalProps, WindowEventProps, EventProps, closed=True, total=False):
    __extra_items__: Prop


class Body(ContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        extra_props: Optional[dict[str, Prop]] = None,
        **props: Unpack[BodyProps],
    ):
        super().__init__(children, classes, style, extra_props, **props)


class Br(DefaultEmptyTag): ...


class ButtonProps(GlobalProps, EventProps, closed=True, total=False):
    autofocus: bool
    disabled: bool
    form: str
    formaction: str
    formenctype: Literal[
        "application/x-www-form-urlencoded",
        "multipart/form-data",
        "text/plain",
    ]
    formmethod: Literal["get", "lost"]
    formnovalidate: bool
    formtarget: (
        Literal[
            "_blank",
            "_self",
            "_parent",
            "_top",
        ]
        | str
    )
    popovertarget: str
    popovertargetaction: Literal[
        "hide",
        "show",
        "toggle",
    ]
    name: Literal[
        "button",
        "reset",
        "submit",
    ]
    type: str
    value: str
    __extra_items__: Prop


class Button(ContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        extra_props: Optional[dict[str, Prop]] = None,
        **props: Unpack[ButtonProps],
    ):
        super().__init__(children, classes, style, extra_props, **props)


class CanvasProps(GlobalProps, EventProps, closed=True, total=False):
    width: int
    height: int
    __extra_items__: Prop


class Canvas(ContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        extra_props: Optional[dict[str, Prop]] = None,
        **props: Unpack[CanvasProps],
    ):
        super().__init__(children, classes, style, extra_props, **props)


class Caption(DefaultContentTag): ...


class Cite(DefaultContentTag): ...


class Code(DefaultContentTag): ...


class ColProps(GlobalProps, EventProps, closed=True, total=False):
    span: int
    __extra_items__: Prop


class Col(EmptyTag):
    def __init__(
        self,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        extra_props: Optional[dict[str, Prop]] = None,
        **props: Unpack[ColProps],
    ):
        super().__init__(classes, style, extra_props, **props)


class Colgroup(ContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        extra_props: Optional[dict[str, Prop]] = None,
        **props: Unpack[ColProps],
    ):
        super().__init__(children, classes, style, extra_props, **props)


class DataProps(GlobalProps, EventProps, closed=True, total=False):
    value: str
    __extra_items__: Prop


class Data(ContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        extra_props: Optional[dict[str, Prop]] = None,
        **props: Unpack[DataProps],
    ):
        super().__init__(children, classes, style, extra_props, **props)


class Datalist(DefaultContentTag): ...


class Dd(DefaultContentTag): ...


class Del(DefaultContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        datetime: Optional[Datetime] = None,
        extra_props: Optional[dict[str, Prop]] = None,
        **props: Unpack[DefaultProps],
    ):
        if datetime:
            props = {
                "datetime": datetime.replace(microsecond=0).astimezone().isoformat(),
                **props,
            }
        super().__init__(children, classes, style, extra_props, **props)


class DetailsProps(GlobalProps, WindowEventProps, EventProps, closed=True, total=False):
    open: bool
    __extra_items__: Prop


class Details(ContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        extra_props: Optional[dict[str, Prop]] = None,
        **props: Unpack[DetailsProps],
    ):
        super().__init__(children, classes, style, extra_props, **props)


class Dfn(DefaultContentTag): ...


class DialogProps(GlobalProps, EventProps, closed=True, total=False):
    open: bool
    __extra_items__: Prop


class Dialog(DefaultContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        extra_props: Optional[dict[str, Prop]] = None,
        **props: Unpack[DialogProps],
    ):
        super().__init__(children, classes, style, extra_props, **props)


class Div(DefaultContentTag): ...


class Dl(DefaultContentTag): ...


class Dt(DefaultContentTag): ...


class Em(DefaultContentTag): ...


class EmbedProps(GlobalProps, EventProps, closed=True, total=False):
    width: int
    height: int
    src: str
    type: str
    __extra_items__: Prop


class Embed(DefaultEmptyTag):
    def __init__(
        self,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        extra_props: Optional[dict[str, Prop]] = None,
        **props: Unpack[EmbedProps],
    ):
        super().__init__(classes, style, extra_props, **props)


class FieldsetProps(
    GlobalProps, WindowEventProps, EventProps, closed=True, total=False
):
    disabled: bool
    form: str
    name: str
    __extra_items__: Prop


class Fieldset(ContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        extra_props: Optional[dict[str, Prop]] = None,
        **props: Unpack[FieldsetProps],
    ):
        super().__init__(children, classes, style, extra_props, **props)


class Figcaption(DefaultContentTag): ...


class Figure(DefaultContentTag): ...


class Footer(DefaultContentTag): ...


class FormProps(GlobalProps, EventProps, closed=True, total=False):
    accept_charset: str
    action: str
    autocomplete: Literal["on", "off"]
    enctype: Literal[
        "application/x-www-form-urlencoded",
        "multipart/form-data",
        "text/plain",
    ]
    method: Literal["get", "post"]
    name: str
    novalidate: bool
    rel: Literal[
        "external",
        "help",
        "license",
        "next",
        "nofollow",
        "noopener",
        "noreferrer",
        "opener",
        "prev",
        "search",
    ]
    target: Literal[
        "_blank",
        "_self",
        "_parent",
        "_top",
    ]
    __extra_items__: Prop


class Form(ContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        extra_props: Optional[dict[str, Prop]] = None,
        **props: Unpack[FormProps],
    ):
        super().__init__(children, classes, style, extra_props, **props)


class Head(ContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        extra_props: Optional[dict[str, Prop]] = None,
        **props: Unpack[GlobalProps],
    ):
        super().__init__(children, classes, style, extra_props, **props)


class Header(DefaultContentTag): ...


class Hgroup(DefaultContentTag): ...


class Hr(DefaultEmptyTag): ...


class HtmlProps(GlobalProps, closed=True, total=False):
    xmlns: str
    __extra_items__: Prop


class Html(ContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        extra_props: Optional[dict[str, Prop]] = None,
        **props: Unpack[HtmlProps],
    ):
        super().__init__(children, classes, style, extra_props, **props)


class I(DefaultContentTag): ...


class IframeProps(GlobalProps, EventProps, closed=True, total=False):
    allow: str
    allowfullscreen: Literal["true", "false"]
    allowpaymentrequest: Literal["true", "false"]
    width: int
    height: int
    loading: Literal["eager", "lazy"]
    name: str
    referrerpolicy: Literal[
        "no-referrer",
        "no-referrer-when-downgrade",
        "origin",
        "origin-when-cross-origin",
        "same-origin",
        "strict-origin-when-cross-origin",
        "unsafe-url",
    ]
    sandbox: Literal[
        "allow-forms",
        "allow-pointer-lock",
        "allow-popups",
        "allow-same-origin",
        "allow-scripts",
        "allow-top-navigation",
    ]
    src: str
    srcdoc: str
    __extra_items__: Prop


class Iframe(ContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        extra_props: Optional[dict[str, Prop]] = None,
        **props: Unpack[IframeProps],
    ):
        super().__init__(children, classes, style, extra_props, **props)


class ImgProps(GlobalProps, EventProps, closed=True, total=False):
    alt: str
    crossorigin: Literal["anonymous", "use-credentials", ""]
    width: int
    height: int
    ismap: bool
    loading: Literal["eager", "lazy"]
    longdesc: str
    referrerpolicy: Literal[
        "no-referrer",
        "no-referrer-when-downgrade",
        "origin",
        "origin-when-cross-origin",
        "same-origin",
        "strict-origin-when-cross-origin",
        "unsafe-url",
    ]
    sizes: str
    src: str
    srcset: str
    usemap: str
    __extra_items__: Prop


class Img(EmptyTag):
    def __init__(
        self,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        extra_props: Optional[dict[str, Prop]] = None,
        **props: Unpack[ImgProps],
    ):
        super().__init__(classes, style, extra_props, **props)


class InputProps(GlobalProps, EventProps, closed=True, total=False):
    accept: str
    alt: str
    autocomplete: Literal["on", "off"]
    autofocus: bool
    checked: bool
    dirname: str
    disabled: bool
    form: str
    formaction: str
    formenctype: Literal[
        "application/x-www-form-urlencoded",
        "multipart/form-data",
        "text/plain",
    ]
    formmethod: Literal["get", "post"]
    formnovalidate: bool
    formtarget: (
        Literal[
            "_blank",
            "_self",
            "_parent",
            "_top",
        ]
        | str
    )
    height: int
    list: str
    max: int | str
    maxlength: int
    min: int | str
    minlength: int
    multiple: bool
    name: str
    pattern: str
    placeholder: str
    popovertarget: str
    popovertargetaction: Literal[
        "hide",
        "show",
        "toggle",
    ]
    readonly: bool
    required: bool
    size: int
    src: str
    step: int
    type: Literal[
        "button",
        "checkbox",
        "color",
        "date",
        "datetime-local",
        "email",
        "file",
        "hidden",
        "image",
        "month",
        "number",
        "password",
        "radio",
        "range",
        "reset",
        "search",
        "submit",
        "tel",
        "text",
        "time",
        "url",
        "week",
    ]
    value: str
    width: int
    __extra_items__: Prop


class Input(EmptyTag):
    def __init__(
        self,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        extra_props: Optional[dict[str, Prop]] = None,
        **props: Unpack[InputProps],
    ):
        super().__init__(classes, style, extra_props, **props)


class InsProps(GlobalProps, EventProps, closed=True, total=False):
    cite: str
    __extra_items__: Prop


class Ins(ContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        datetime: Optional[Datetime] = None,
        extra_props: Optional[dict[str, Prop]] = None,
        **props: Unpack[InsProps],
    ):
        if datetime:
            props = {
                "datetime": datetime.replace(microsecond=0).astimezone().isoformat(),
                **props,
            }
        super().__init__(children, classes, style, extra_props, **props)


class Kbd(DefaultContentTag): ...


class LabelProps(GlobalProps, EventProps, closed=True, total=False):
    for_: str
    form: str
    __extra_items__: Prop


class Label(ContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        extra_props: Optional[dict[str, Prop]] = None,
        **props: Unpack[LabelProps],
    ):
        if "for_" in props:
            props["for"] = props.pop("for_")
        super().__init__(children, classes, style, extra_props, **props)


class Legend(DefaultContentTag): ...


class LiProps(GlobalProps, EventProps, closed=True, total=False):
    value: int
    __extra_items__: Prop


class Li(ContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        extra_props: Optional[dict[str, Prop]] = None,
        **props: Unpack[LiProps],
    ):
        super().__init__(children, classes, style, extra_props, **props)


class LinkProps(GlobalProps, EventProps, closed=True, total=False):
    crossorigin: Literal["anonymous", "use-credentials", ""]
    href: str
    hreflang: str
    media: str
    referrerpolicy: Literal[
        "no-referrer",
        "no-referrer-when-downgrade",
        "origin",
        "origin-when-cross-origin",
        "unsafe-url",
    ]
    rel: Literal[
        "alternate",
        "author",
        "dns-prefetch",
        "help",
        "icon",
        "license",
        "next",
        "pingback",
        "preconnect",
        "prefetch",
        "preload",
        "prerender",
        "prev",
        "search",
        "stylesheet",
    ]
    sizes: str
    title: str
    type: str
    __extra_items__: Prop


class Link(EmptyTag):
    def __init__(
        self,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        extra_props: Optional[dict[str, Prop]] = None,
        **props: Unpack[LinkProps],
    ):
        super().__init__(classes, style, extra_props, **props)


class Main(DefaultContentTag): ...


class MapProps(GlobalProps, EventProps, closed=True, total=False):
    name: str
    __extra_items__: Prop


class Map(DefaultContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        extra_props: Optional[dict[str, Prop]] = None,
        **props: Unpack[MapProps],
    ):
        super().__init__(children, classes, style, extra_props, **props)


class Mark(DefaultContentTag): ...


class Menu(DefaultContentTag): ...


class MetaProps(GlobalProps, EventProps, closed=True, total=False):
    charset: str
    content: str
    http_equiv: Literal[
        "content-security-policy",
        "content-type",
        "default-style",
        "refresh",
    ]
    name: Literal[
        "application-name",
        "author",
        "description",
        "generator",
        "keywords",
        "viewport",
        "theme-color",
    ]
    __extra_items__: Prop


class Meta(EmptyTag):
    def __init__(
        self,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        **props: Unpack[MetaProps],
    ):
        super().__init__(classes, style, **props)


class MeterProps(GlobalProps, EventProps, closed=True, total=False):
    form: str
    high: int
    low: int
    max: int
    min: int
    optimum: int
    value: int
    __extra_items__: Prop


class Meter(ContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        **props: Unpack[MeterProps],
    ):
        super().__init__(children, classes, style, **props)


class Nav(DefaultContentTag): ...


class Noscript(ContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        **props: Unpack[GlobalProps],
    ):
        super().__init__(children, classes, style, **props)


class ObjectProps(GlobalProps, EventProps, closed=True, total=False):
    data: str
    form: str
    width: int
    height: int
    name: str
    type: str
    typemustmatch: Literal["true", "false"]
    usemap: str
    __extra_items__: Prop


class Object(ContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        **props: Unpack[ObjectProps],
    ):
        super().__init__(children, classes, style, **props)


class OlProps(GlobalProps, EventProps, closed=True, total=False):
    reversed: bool
    start: int
    type: Literal[
        "1",
        "A",
        "a",
        "I",
        "i",
    ]
    __extra_items__: Prop


class Ol(ContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        **props: Unpack[OlProps],
    ):
        super().__init__(children, classes, style, **props)


class OptgroupProps(GlobalProps, EventProps, closed=True, total=False):
    disabled: bool
    label: str
    __extra_items__: Prop


class Optgroup(ContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        **props: Unpack[OptgroupProps],
    ):
        super().__init__(children, classes, style, **props)


class OptionProps(GlobalProps, EventProps, closed=True, total=False):
    disabled: bool
    label: str
    selected: bool
    value: str
    __extra_items__: Prop


class Option(ContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        **props: Unpack[OptionProps],
    ):
        super().__init__(children, classes, style, **props)


class OutputProps(GlobalProps, EventProps, closed=True, total=False):
    for_: str
    form: str
    name: str
    __extra_items__: Prop


class Output(ContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        **props: Unpack[OutputProps],
    ):
        if "for_" in props:
            props["for"] = props.pop("for_")
        super().__init__(children, classes, style, **props)


class P(DefaultContentTag): ...


class ParamProps(GlobalProps, EventProps, closed=True, total=False):
    name: str
    value: str
    __extra_items__: Prop


class Param(EmptyTag):
    def __init__(
        self,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        **props: Unpack[ParamProps],
    ):
        super().__init__(classes, style, **props)


class Picture(DefaultContentTag): ...


class Pre(DefaultContentTag): ...


class ProgressProps(GlobalProps, EventProps, closed=True, total=False):
    max: int
    value: int
    __extra_items__: Prop


class Progress(ContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        **props: Unpack[ProgressProps],
    ):
        super().__init__(children, classes, style, **props)


class QProps(GlobalProps, EventProps, closed=True, total=False):
    cite: str
    __extra_items__: Prop


class Q(ContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        **props: Unpack[QProps],
    ):
        super().__init__(children, classes, style, **props)


class Rp(DefaultContentTag): ...


class Rt(DefaultContentTag): ...


class Ruby(DefaultContentTag): ...


class S(DefaultContentTag): ...


class Samp(DefaultContentTag): ...


class ScriptProps(GlobalProps, EventProps, closed=True, total=False):
    async_: bool
    crossorigin: Literal["anonymous", "use-credentials", ""]
    defer: bool
    integrity: str
    nomodule: bool
    referrerpolicy: Literal[
        "no-referrer",
        "no-referrer-when-downgrade",
        "origin",
        "origin-when-cross-origin",
        "same-origin",
        "strict-origin",
        "strict-origin-when-cross-origin",
        "unsafe-url",
    ]
    src: str
    type: str
    __extra_items__: Prop


class Script(ContentTag):
    def __init__(
        self,
        script: Optional[str] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        **props: Unpack[ScriptProps],
    ):
        super().__init__([script] if script else None, classes, style, **props)


class Search(DefaultContentTag): ...


class Section(DefaultContentTag): ...


class SelectProps(GlobalProps, EventProps, closed=True, total=False):
    autofocus: bool
    disabled: bool
    form: str
    multiple: bool
    name: str
    required: bool
    size: int
    __extra_items__: Prop


class Select(ContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        **props: Unpack[SelectProps],
    ):
        super().__init__(children, classes, style, **props)


class Small(DefaultContentTag): ...


class SourceProps(GlobalProps, EventProps, closed=True, total=False):
    media: str
    sizes: str
    src: str
    srcset: str
    type: str
    __extra_items__: Prop


class Source(EmptyTag):
    def __init__(
        self,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        **props: Unpack[SourceProps],
    ):
        super().__init__(classes, style, **props)


class Span(DefaultContentTag): ...


class Strong(DefaultContentTag): ...


class StyleProps(GlobalProps, EventProps, closed=True, total=False):
    media: str
    type: str
    __extra_items__: Prop


class Style(ContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        **props: Unpack[StyleProps],
    ):
        super().__init__(children, classes, style, **props)


class Sub(DefaultContentTag): ...


class Summary(DefaultContentTag): ...


class Sup(DefaultContentTag): ...


class Svg(DefaultContentTag): ...


class Table(DefaultContentTag): ...


class Tbody(DefaultContentTag): ...


class TdProps(GlobalProps, EventProps, closed=True, total=False):
    colspan: int
    headers: str
    rowspan: int
    __extra_items__: Prop


class Td(ContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        **props: Unpack[TdProps],
    ):
        super().__init__(children, classes, style, **props)


class Template(DefaultContentTag): ...


class TextareaProps(GlobalProps, EventProps, closed=True, total=False):
    autofocus: bool
    cols: int
    dirname: str
    disabled: bool
    form: str
    maxlength: int
    name: str
    placeholder: str
    readonly: bool
    required: bool
    rows: int
    wrap: Literal["hard", "soft"]
    __extra_items__: Prop


class Textarea(ContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        **props: Unpack[TextareaProps],
    ):
        super().__init__(children, classes, style, **props)


class Tfoot(DefaultContentTag): ...


class ThProps(GlobalProps, EventProps, closed=True, total=False):
    abbr: str
    colspan: int
    headers: str
    rowspan: int
    scope: Literal[
        "col",
        "colgroup",
        "row",
        "rowgroup",
    ]
    __extra_items__: Prop


class Th(ContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        **props: Unpack[ThProps],
    ):
        super().__init__(children, classes, style, **props)


class Thead(DefaultContentTag): ...


class Time(ContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        datetime: Optional[Datetime] = None,
        extra_props: Optional[dict[str, Prop]] = None,
        **props: Prop,
    ):
        if datetime:
            props = {
                "datetime": datetime.replace(microsecond=0).astimezone().isoformat(),
                **props,
            }
        super().__init__(children, classes, style, extra_props, **props)


class Title(ContentTag):
    def __init__(
        self,
        content: str,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        extra_props: Optional[dict[str, Prop]] = None,
        **props: Unpack[GlobalProps],
    ):
        super().__init__([content], classes, style, extra_props, **props)


class Tr(DefaultContentTag): ...


class TrackProps(GlobalProps, EventProps, closed=True, total=False):
    default: bool
    kind: Literal[
        "captions",
        "chapters",
        "descriptions",
        "metadata",
        "subtitles",
    ]
    label: str
    src: str
    srclang: str
    __extra_items__: Prop


class Track(EmptyTag):
    def __init__(
        self,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        extra_props: Optional[dict[str, Prop]] = None,
        **props: Unpack[TrackProps],
    ):
        super().__init__(classes, style, extra_props, **props)


class U(DefaultContentTag): ...


class Ul(DefaultContentTag): ...


class Var(DefaultContentTag): ...


class VideoProps(GlobalProps, EventProps, closed=True, total=False):
    autoplay: bool
    controls: bool
    width: int
    height: int
    loop: bool
    muted: bool
    poster: str
    preload: Literal[
        "auto",
        "metadata",
        "none",
    ]
    src: str
    __extra_items__: Prop


class Video(ContentTag):
    def __init__(
        self,
        children: Optional[Sequence[Tag | str]] = None,
        classes: Optional[Sequence[str]] = None,
        style: Optional[dict[str, str]] = None,
        extra_props: Optional[dict[str, Prop]] = None,
        **props: Unpack[VideoProps],
    ):
        super().__init__(children, classes, style, extra_props, **props)


class Wbr(DefaultEmptyTag): ...
