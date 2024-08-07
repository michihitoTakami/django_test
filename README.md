## 何者か？
とあるテストです。

## 環境の立ち上げ方
```:shell
cd docker
docker compose build
docker compose up
```

### 注意点
- 初回の`docker compose up`でエラーになります
  - 初回はDBのCREATEが行われるが、作られる前にDjangoがDBを読みに行ってしまう為。
- MySQLコンテナが立ち上がった後、一度`docker compose stop`等で落としてもらって、再度`docker compose up`してみてください。多分上手く行きます。

## 使い方
### 成功用
```:shell
curl -X POST http://localhost:8000/ai_analysis/ -H "Content-Type: application/json" -d '{"image_path": "hoge/hoge.jpg"}'
```

### 失敗用
```:shell
curl -X POST http://localhost:8000/ai_analysis/ -H "Content-Type: application/json" -d '{"image_path": "hoge/error.jpg"}'
```

### データの確認方法
```:shell
curl -X GET http://localhost:8000/ai_analysis_logs/?date=20240807
```
data=%Y%m%dの形式で付与します。
パラメータがない場合は本日の日付のデータを返します。

### 注意点
- 成功と失敗の通信の違いは、image_pathの値の中に`error`の文字列が含まれているかどうかです
- `/ai_analysis/`のレスポンスが遅いですが、わざと5秒のディレイを入れています。
  - ※requestとresponseの時間の差分を明確にする為

## 後片付け
```:shell
cd docker
docker compose down --rmi all --volume
docker volume prune
``` 

## 各種コメント

- Djangoはじめ、Pythonのフレームワーク初心者ですのでお作法がなっていない等、いろいろあるかもしれませんが、ご容赦ください。
- 一応、静的解析ツールとしてRuffを入れてみました。仕様とかは勉強中で、とりあえず導入したレベルです。
- こだわりポイント
  - mockサーバーをflaskで立ち上げてみました
  - docker composeで各種設定してみました
  - 敢えてMySQL使ってみました
  - エラーの分岐等もちょっと頑張ってみました
- あくまでも課題なので容赦してほしいポイント
  - 特に影響はないと思い、リポジトリはパブリックです
  - 認証とかその手の物は作っていません
  - 製品化や、大規模開発を想定したファイル、ディレクトリ構造
    - settings.pyは本来、development,staging,productionなど環境に応じて分ける
    - models.py、views.py、serializers.pyなどは、ディレクトリの中にClassごとにファイルを作成し、メイン側でimportする
    - など
  - 最低限のユニットテスト
- その他ご不明点があれば、ご連絡ください
