from builder.base import (
    ContentTag,
    EmptyTag,
    build_child,
    build_classes,
    build_props,
    build_style,
)


def test_case_1():
    result = build_props(
        {"john": "wick", "is_true": True, "is_false": False, "number": 2469}
    )
    assert result == ' john="wick" is-true number="2469"'


def test_case_2():
    result = build_classes([f"class_{n + 1}" for n in range(5)])
    assert result == ' class="class_1 class_2 class_3 class_4 class_5"'


def test_case_3():
    result = build_style({"margin": "auto", "padding": "16px"})
    assert result == ' style="margin:auto;padding:16px;"'


def test_case_4():
    result = build_child("teste")
    assert result == "teste"


def test_case_5():
    class Test(ContentTag): ...

    result = build_child(Test())
    assert result == "<test></test>"


def test_case_6():
    class Test(EmptyTag): ...

    result = build_child(Test())
    assert result == "<test/>"


def test_case_7():
    class Test(ContentTag): ...

    result = build_child(Test(hello="world"))
    assert result == '<test hello="world"></test>'


def test_case_8():
    class Test(EmptyTag): ...

    result = build_child(Test(hello="world"))
    assert result == '<test hello="world"/>'


def test_case_9():
    class Test(ContentTag): ...

    result = Test(classes=[f"class_{n + 1}" for n in range(5)]).build()
    assert result == '<test class="class_1 class_2 class_3 class_4 class_5"></test>'


def test_case_10():
    class Test(EmptyTag): ...

    result = Test(classes=[f"class_{n + 1}" for n in range(5)]).build()
    assert result == '<test class="class_1 class_2 class_3 class_4 class_5"/>'


def test_case_11():
    class Test(ContentTag): ...

    result = Test(style={"margin": "auto", "padding": "16px"}).build()
    assert result == '<test style="margin:auto;padding:16px;"></test>'


def test_case_12():
    class Test(EmptyTag): ...

    result = Test(style={"margin": "auto", "padding": "16px"}).build()
    assert result == '<test style="margin:auto;padding:16px;"/>'


def test_case_13():
    class Test(ContentTag): ...

    result = Test(john="wick", is_true=True, is_false=False, number=2469).build()
    assert result == '<test john="wick" is-true number="2469"></test>'


def test_case_14():
    class Test(EmptyTag): ...

    result = Test(john="wick", is_true=True, is_false=False, number=2469).build()
    assert result == '<test john="wick" is-true number="2469"/>'


def test_case_15():
    class Test(ContentTag): ...

    class Test2(ContentTag): ...

    result = Test(children=[Test2()]).build()
    assert result == "<test><test2></test2></test>"
