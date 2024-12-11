# 実行環境の作成

macとimacではプリインストールのpythonのバージョンが違うので、
brew install python
brew install python-tk
で最新のpythonを入れてバージョンを揃えておく。

python3 -m venv .venv
. .venv/bin/actvate

pip install -r requirements.txt
でモジュールをインストールする。
pandsは依存関係でインストールできないので、バージョン部分を削除して実行する。
