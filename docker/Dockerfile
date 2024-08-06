# python:3.9の公式 image をベースの image として設定
FROM python:3.9
# 作業ディレクトリの作成
RUN mkdir /mysite
# 作業ディレクトリの設定（以後の RUN は WORKDIR で実行）
WORKDIR /mysite
# カレントディレクトリにある資産をコンテナ上の指定のディレクトリにコピーする
ADD web /mysite
# pipでrequirements.txtに指定されているパッケージを追加する
RUN pip install --upgrade pip
RUN pip install -r requirements.txt