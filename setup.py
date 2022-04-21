from Cython.Build import cythonize
from setuptools import Extension, setup

extensions = [
    Extension("sample.foo", ["src/sample/foo.pyx"]),
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
