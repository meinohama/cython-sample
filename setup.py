from Cython.Build import cythonize
from setuptools import Extension, setup

extensions = [
    Extension(
        "sample.bootstrap",
        [
            "src/sample/bootstrap.pyx",
            "src/sample/foo.pyx",
            "src/sample/foo_sub.c",
            "src/sample/bar.pyx",
        ],
        depends=[
            "src/sample/foo_sub.h",
        ],
    ),
]

setup(
    ext_modules=cythonize(
        extensions,
        compiler_directives={
            "language_level": "3",
        },
        build_dir="build",
    )
)
