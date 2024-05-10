from builder.base import (
    ContentTag,
    EmptyTag,
    build_child,
    build_classes,
    build_name,
    build_props,
    build_style,
)


def test_case_1():
    """It is expected that it will be possible to build the props"""
    result = build_props(
        {"john": "wick", "is_true": True, "is_false": False, "number": 2469}
    )
    assert result == ' john="wick" is-true number="2469"'


def test_case_2():
    """It is expected that it will be possible to build the classes"""
    result = build_classes([f"class_{n + 1}" for n in range(5)])
    assert result == ' class="class_1 class_2 class_3 class_4 class_5"'


def test_case_3():
    """It is expected that it will be possible to build the styles"""
    result = build_style({"margin": "auto", "padding": "16px"})
    assert result == ' style="margin:auto;padding:16px;"'


def test_case_4():
    """It is expected that if the child is a text, the result will be itself"""
    result = build_child("teste")
    assert result == "teste"


def test_case_5():
    """It is expected that if the child is a tag, the result will be an HTML tag"""

    class Test(ContentTag): ...

    result = build_child(Test())
    assert result == "<test></test>"


def test_case_6():
    """It is expected that if the child is an empty tag, the result will be an empty HTML tag"""

    class Test(EmptyTag): ...

    result = build_child(Test())
    assert result == "<test/>"


def test_case_7():
    """Classes are expected to render correctly in the HTML tag"""

    class TestContent(ContentTag): ...

    class TestEmpty(EmptyTag): ...

    result_content = TestContent(classes=[f"class_{n + 1}" for n in range(5)]).build()
    result_empty = TestEmpty(classes=[f"class_{n + 1}" for n in range(5)]).build()
    assert (
        result_content
        == '<test-content class="class_1 class_2 class_3 class_4 class_5"></test-content>'
    )
    assert (
        result_empty == '<test-empty class="class_1 class_2 class_3 class_4 class_5"/>'
    )


def test_case_8():
    """Styles are expected to be rendered correctly in the HTML tag"""

    class TestContent(ContentTag): ...

    class TestEmpty(EmptyTag): ...

    result_content = TestContent(style={"margin": "auto", "padding": "16px"}).build()
    result_empty = TestEmpty(style={"margin": "auto", "padding": "16px"}).build()
    assert (
        result_content
        == '<test-content style="margin:auto;padding:16px;"></test-content>'
    )
    assert result_empty == '<test-empty style="margin:auto;padding:16px;"/>'


def test_case_9():
    """Props are expected to render correctly in the HTML tag"""

    class TestContent(ContentTag): ...

    class TestEmpty(EmptyTag): ...

    result_content = TestContent(
        john="wick", is_true=True, is_false=False, number=2469
    ).build()
    result_empty = TestEmpty(
        john="wick", is_true=True, is_false=False, number=2469
    ).build()
    assert (
        result_content
        == '<test-content john="wick" is-true number="2469"></test-content>'
    )
    assert result_empty == '<test-empty john="wick" is-true number="2469"/>'


def test_case_10():
    """Children are expected to be rendered correctly in the HTML tag"""

    class Test(ContentTag): ...

    class Test2(ContentTag): ...

    result = Test(children=[Test2()]).build()
    assert result == "<test><test2></test2></test>"


def test_case_11():
    """It is expected that the name is constructed correctly"""
    result = build_name("TestNameIsCorrect")
    assert result == "test-name-is-correct"


def test_case_12():
    """The name is expected to be rendered correctly in the HTML tag"""

    class TestNameIsCorrectContent(ContentTag): ...

    class TestNameIsCorrectEmpty(EmptyTag): ...

    result_content = TestNameIsCorrectContent().build()
    result_empty = TestNameIsCorrectEmpty().build()
    assert (
        result_content
        == "<test-name-is-correct-content></test-name-is-correct-content>"
    )
    assert result_empty == "<test-name-is-correct-empty/>"
