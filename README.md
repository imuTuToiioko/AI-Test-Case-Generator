# AI 测试用例生成器 (Vibe Coding Demo)

这是一个基于 **Python + Flet** 开发的移动端 AI 测试用例生成器 Demo。

## ✨ 项目背景
结合本人原有的 Linux/Web 自动化测试背景，针对本次面试岗位（Native 开发实习生）要求，通过 **Vibe Coding（AI 辅助编程）** 模式，快速实现了一个跨端 App 原型。

## 🚀 核心功能
- 输入功能需求（如：用户登录）。
- 调用大模型 API（DeepSeek），自动生成覆盖正常、异常、边界场景的测试用例。
- 极简移动端 UI，支持响应式渲染。

## 🛠 技术栈
- 前端：Python Flet (基于 Flutter)
- 后端：DeepSeek API (OpenAI 兼容格式)

## 💡 Vibe Coding 实践心得
本项目全程使用 AI 编写界面与请求逻辑。我负责定义需求、设计 Prompt 和调试接口，极大体验了 AI 工具带来的效率提升。结合我本地的 **Ollama** 环境，我对端侧大模型部署也有了初步的实践经验。

## ⚙️ 本地运行方式
```bash
pip install flet requests
python main.py
