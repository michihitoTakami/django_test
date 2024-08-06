# mock_server/mock_server.py
from flask import Flask, request, jsonify
import time

app = Flask(__name__)

@app.route('/', methods=['POST'])
def mock_api():
    data = request.json
    image_path = data.get('image_path')
    time.sleep(5)  # 5秒間待機。リクエストとレスポンスのタイムスタンプの差を見るため。
    if "error" in image_path:
        return jsonify({
            "success": False,
            "message": "Error:E50012",
            "estimated_data": {}
        }), 400
    else:
        return jsonify({
            "success": True,
            "message": "success",
            "estimated_data": {
                "class": 3,
                "confidence": 0.8683
            }
        }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)