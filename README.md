## 何者か？
とあるテストです。

## 環境の立ち上げ方
```:shell
cd docker
docker compose up --build
```

## 使い方
### 成功用の通信の方法
```:shell
curl -X POST http://localhost:8000/ai_analysis/ -H "Content-Type: application/json" -d '{"image_path": "hoge/hoge.jpg"}'
```

### 失敗用の通信の方法
```:shell
curl -X POST http://localhost:8000/ai_analysis/ -H "Content-Type: application/json" -d '{"image_path": "hoge/error.jpg"}'
```
※image_pathの値の中に`error`の文字列が含まれていたら、エラー出力を返します。

### データの確認方法
```
curl -X GET http://127.0.0.1:8000/ai_analysis_logs/?date=20240807
```
data=%Y%m%dの形式で付与します。
パラメータがない場合は本日の日付のデータを返します。

### 