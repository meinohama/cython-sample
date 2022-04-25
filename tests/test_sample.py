from sample import foo, bar


def test_foo() -> None:
    foo.foo_print("test_foo")


def test_foo_bar_c() -> None:
    foo.foo_bar_c_print("test_foo_bar_c")


def test_bar() -> None:
    bar.bar_print("test_bar")


def test_bar_foo_c() -> None:
    bar.bar_foo_c_print("test_bar_foo_c")
