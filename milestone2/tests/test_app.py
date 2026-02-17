import pytest
import requests
import json
from app.app import app as flask_app

# 初始化测试客户端，模拟请求
@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client

# 测试1：健康检查接口可用性
def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}

# 测试2：推理接口-合法输入，验证输出格式
def test_infer_valid_input(client):
    input_data = {"input": [[1,2,3], [4,5,6]]}
    response = client.post('/infer', json=input_data)
    assert response.status_code == 200
    # 验证输出包含指定字段
    assert "predictions" in response.json
    assert "confidence" in response.json
    # 验证输出格式为列表
    assert isinstance(response.json["predictions"], list)
    assert isinstance(response.json["confidence"], list)
    # 验证预测结果和置信度长度一致
    assert len(response.json["predictions"]) == len(response.json["confidence"])

# 测试3：推理接口-无input字段，验证400错误
def test_infer_missing_input(client):
    input_data = {"data": [[1,2,3]]} # 无input字段
    response = client.post('/infer', json=input_data)
    assert response.status_code == 400
    assert "error" in response.json

# 测试4：推理接口-空列表输入，验证值错误
def test_infer_empty_input(client):
    input_data = {"input": []} # 空列表
    response = client.post('/infer', json=input_data)
    assert response.status_code == 400
    assert "输入必须为非空列表" in response.json["error"]

# 测试5：推理接口-非列表输入，验证错误处理
def test_infer_invalid_input_type(client):
    input_data = {"input": "test"} # 非列表
    response = client.post('/infer', json=input_data)
    assert response.status_code == 400
    assert "error" in response.json