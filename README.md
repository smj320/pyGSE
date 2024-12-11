# 実行環境の作成

macとimacではプリインストールのpythonのバージョンが違うので、
brew install python@3.12
brew install python-tk@3.12
で最新のpythonを入れてバージョンを揃えておく。
3.12以下でないとpandasでエラーがでる。

python3 -V で3.12系が出ない場合はデフォルトのpythonになっている可能性が高いので、
brew unlink python@3.12 && brew link python@3.12
とかででリンクkを張り直す。

# 仮想環境の作り方
python3 -m venv .venv
. .venv/bin/actvate

pip install -r requirements.txt
でモジュールをインストールする。

