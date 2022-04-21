# cython-sample

Cython と setuptools を使ってパッケージをビルドする時の現時点(Apr. 2022)でのベストプラクティス。
(ベストじゃないかもしれん)

ディレクトリはいわゆる src-layout な構成にしている(好みの問題)。

最近は pyproject.toml を使うのが良さそうなのでここでもそれにのっかっている。

## ビルド方法

setuptools の Quickstart に書いてあるまま。

https://setuptools.pypa.io/en/latest/userguide/quickstart.html

```shell
pip install build
pip -m build
```

## setup.cfg と setup.py

できれば setup.cfg だけで管理したい。
しかし、Cython でビルドするモジュールの指定は setup.py でなければできなさそう。
そのため Cython にかかわる部分だけ setup.py に書いて、残りは setup.cfg に書く。

## .pyx ファイル

`pip -m build` しても、なぜか Cython のソースファイル(.pyx)が sdist に含まれない。なので wheel のビルド時点で .pyx がないというエラーになる。

```txt
ValueError: 'src/sample/foo.pyx' doesn't match any files
```

setup.cfg の `package_data` に `*.pyx` を含めればよい、といった話もチラホラあるようだが、そこに入れると wheel パッケージの中にも .pyx ファイルが含まれてしまう。
sdist には .pyx を含めたいが、wheel には含めたくない。

そこで、MANIFEST.in で sdist に .pyx を含めるように指定する。
こうすると最終的な wheel パッケージは .pyx が含まれないので、パッケージをインストールした場合に .pyx が一緒にインストールされてしまうようなことがない。

