from flask import Flask, request, jsonify
import numpy as np

# 初始化Flask应用（ML推理服务基础）
app = Flask(__name__)

# 模拟训练好的ML模型
def mock_ml_inference(input_data):
    """简单的推理函数，验证输入输出格式"""
    if not isinstance(input_data, list) or len(input_data) == 0:
        raise ValueError("输入必须为非空列表")
    # 模拟预测：返回分类结果和置信度
    pred = np.argmax(np.array(input_data), axis=1).tolist()
    confidence = np.random.uniform(0.8, 0.99, len(pred)).tolist()
    return {"predictions": pred, "confidence": confidence}

# 推理接口（POST方法，标准ML服务端点）
@app.route('/infer', methods=['POST'])
def infer():
    try:
        # 获取请求体
        data = request.get_json()
        if "input" not in data:
            return jsonify({"error": "请求体必须包含input字段"}), 400
        # 执行推理
        result = mock_ml_inference(data["input"])
        return jsonify(result), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"服务器内部错误：{str(e)}"}), 500

# 健康检查接口（用于服务可用性验证）
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    # 监听0.0.0.0，允许容器外部访问
    app.run(host="0.0.0.0", port=5000, debug=False) # 生产环境关闭debug