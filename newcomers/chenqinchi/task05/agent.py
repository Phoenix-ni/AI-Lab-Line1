from openai import OpenAI

# 初始化客户端（SiliconFlow）
client = OpenAI(
    api_key="sk-xxgjbqhigbwkldksmjqtvlmarbxbecrdmtenpjqoscthabqj",
    base_url="https://api.siliconflow.cn/v1"
)

# 工具：计算器
def calculator(expression: str) -> str:
    """计算数学表达式，例如 "2 + 3 * 5" """
    try:
        result = eval(expression)
        return f"✅ 计算器工具调用成功：{expression} = {result}"
    except Exception as e:
        return f"❌ 计算出错：{str(e)}"

# 系统提示词，告诉模型可以调用计算器
system_prompt = """
你是一个会使用计算器工具的AI助手。
当用户提问包含数学计算时，调用calculator函数，把表达式传给它。
不需要计算的问题直接正常回答。
"""

def agent_chat(user_input: str):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]
    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3",
        messages=messages
    )
    reply = response.choices[0].message.content
    return reply


if __name__ == "__main__":
    print("=== Task05 计算器Agent（DeepSeek-V3）启动 ===")
    print("输入你的问题，输入 exit 退出")
    while True:
        user_text = input("\n你：")
        if user_text.strip() == "exit":
            print("Agent：程序退出")
            break
        # 简单规则：检测到算式直接调用计算器
        if any(c in user_text for c in "+-*/"):
            cal_result = calculator(user_text)
            print(f"Agent：{cal_result}")
        else:
            ans = agent_chat(user_text)
            print(f"Agent：{ans}")
