# ML Service Containerization & CI/CD (Milestone 2)
MLOps Course Module 3 Milestone 2 - 容器化ML服务+GitHub Actions CI/CD流水线

## CI/CD Status
<!-- 替换为你的仓库地址，自动显示工作流状态 -->
![ML Service CI/CD Pipeline](https://github.com/jane872/UIC/UIC-ids568-milestone2/workflows/ML%20Service%20CI/CD%20Pipeline/badge.svg)

## 快速开始
### 本地开发运行
```bash
# 克隆仓库
git clone <你的仓库地址>
cd <仓库名>/UIC-ids568-milestone2
# 安装依赖
pip install -r app/requirements.txt
# 启动服务
python app/app.py
# 或使用docker-compose本地启动
docker-compose up -d