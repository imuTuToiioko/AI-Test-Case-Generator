import asyncio
import flet as ft
import requests

API_URL = "https://api.deepseek.com/chat/completions"
API_KEY = "sk-42c0a9e6deea44ac8f0975bec4b71bfd"  # ← 记得保留引号，填你自己的
MODEL_NAME = "deepseek-chat"

SYSTEM_PROMPT = "你是一名资深软件测试工程师。请用纯文本输出测试用例，覆盖正常、异常、边界情况。"

def call_llm(requirement: str) -> str:
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"功能需求：{requirement}"}
        ],
    }
    resp = requests.post(API_URL, headers=headers, json=payload, timeout=60)
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]

def main(page: ft.Page):
    page.title = "AI 测试用例生成器"
    page.bgcolor = "#F2F3F5"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # 标题
    title = ft.Text("AI 测试用例生成器", size=24, weight=ft.FontWeight.BOLD, color="black")
    
    # 输入框
    input_field = ft.TextField(
        hint_text="请输入功能需求（例如：用户登录）",
        multiline=True, min_lines=1, max_lines=3,
        filled=True, fill_color="white", border_radius=10,
        color="black" # 输入文字黑色
    )

    # 按钮兼容
    try:
        btn = ft.Button("生成测试用例", bgcolor="#4C6FFF", color="white", width=400)
    except AttributeError:
        btn = ft.ElevatedButton("生成测试用例", bgcolor="#4C6FFF", color="white", width=400)

    # 结果展示区（重点：加上了 color="black"）
    result_box = ft.TextField(
        multiline=True,
        read_only=True,
        min_lines=10,
        max_lines=15,
        hint_text="生成结果将显示在这里...",
        bgcolor="white",
        border_radius=10,
        text_size=14,
        color="black"  # 结果文字黑色
    )

    async def on_click(e):
        req = input_field.value.strip()
        if not req:
            page.snack_bar = ft.SnackBar(ft.Text("请先输入功能需求"))
            page.snack_bar.open = True
            page.update()
            return
        
        btn.disabled = True
        btn.text = "正在生成..."
        page.update()

        try:
            text = await asyncio.to_thread(call_llm, req)
            result_box.value = text
        except Exception as ex:
            result_box.value = f"请求失败: {ex}"
        finally:
            btn.disabled = False
            btn.text = "生成测试用例"
            page.update()

    btn.on_click = on_click

    page.add(
        ft.Container(
            width=400,
            padding=20,
            content=ft.Column(
                spacing=20,
                controls=[title, input_field, btn, result_box],
            )
        )
    )

if __name__ == "__main__":
    if hasattr(ft, "run"):
        ft.run(main)
    else:
        ft.app(main)