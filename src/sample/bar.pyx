from sample cimport foo

cdef void bar_c_print(str message):
    message = "bar_c_print: " + message
    print(message.encode(encoding="UTF-8", errors="replace"))

def bar_print(message: str) -> None:
    message = "bar_print: " + message
    bar_c_print(message)

def bar_foo_c_print(message: str) -> None:
    message = "bar_foo_c_print: " + message
    foo.foo_c_print(message)
