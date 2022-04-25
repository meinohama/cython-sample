cdef extern from "foo_sub.h":
    void foo_sub_print(char *message)

from sample cimport bar

cdef void foo_c_print(str message):
    message = "foo_c_print: " + message
    foo_sub_print(message.encode(encoding="UTF-8", errors="replace"))

def foo_print(message: str) -> None:
    message = "foo_print: " + message
    foo_c_print(message)

def foo_bar_c_print(message: str) -> None:
    message = "foo_bar_c_print: " + message
    bar.bar_c_print(message)

def hello() -> str:
    return "Hello"
