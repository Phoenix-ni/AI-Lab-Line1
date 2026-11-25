from openai import OpenAI
import json

client = OpenAI(
    api_key="sk-xxgjbqhigbwkldksmjqtvlmarbxbecrdmtenpjqoscthabqj",
    base_url="https://api.siliconflow.cn/v1"
)

# 1. 计算器工具函数
def calculator(expression: str):
    """
    计算数学表达式，仅支持英文半角 () + - * /
    :param expression: 数学算式字符串，例如 "12 + 34 * 2"
    :return: 计算结果或者报错信息
    """
    try:
        res = eval(expression)
        return f"计算结果：{expression} = {res}"
    except Exception as e:
        return f"计算失败，错误信息：{str(e)}"

# 2. 给大模型看的工具描述（function schema）
tools = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "用于计算数学四则表达式，支持括号、加减乘除，表达式符号必须是英文半角",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "待计算的数学表达式"
                    }
                },
                "required": ["expression"]
            }
        }
    }
]

def run_agent(user_query: str):
    messages = [
        {
            "role": "system",
            "content": "你是一个AI助手，可以使用calculator工具进行数学计算。需要计算的时候调用工具，不要自己口算。不需要计算就直接回答用户。"
        },
        {
            "role": "user",
            "content": user_query
        }
    ]

    # 第一轮：模型判断是否调用工具
    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3",
        messages=messages,
        tools=tools
    )
    msg = response.choices[0].message

    # 如果模型选择调用工具
    if msg.tool_calls:
        for tool_call in msg.tool_calls:
            func_name = tool_call.function.name
            func_args = json.loads(tool_call.function.arguments)
            # 执行工具
            if func_name == "calculator":
                calc_result = calculator(func_args["expression"])
                # 把工具返回结果塞回对话历史
                messages.append(msg)
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": calc_result
                })
        # 第二轮：模型拿到计算结果，整理成自然语言回答
        final_resp = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3",
            messages=messages,
            tools=tools
        )
        return final_resp.choices[0].message.content
    else:
        # 不需要工具，直接返回模型回答
        return msg.content


if __name__ == "__main__":
    print("=== Task06 原生Function Call Agent ===")
    print("输入问题，输入 exit 退出\n")
    while True:
        user_input = input("你：")
        if user_input.strip() == "exit":
            print("Agent：程序退出")
            break
        answer = run_agent(user_input)
        print(f"Agent：{answer}\n")
