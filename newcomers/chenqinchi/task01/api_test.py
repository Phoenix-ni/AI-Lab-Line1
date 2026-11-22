import requests

api_key = "sk-xxgjbqhigbwkldksmjqtvlmarbxbecrdmtenpjqoscthabqj"
url = "https://api.siliconflow.cn/v1/chat/completions"

payload = {
  "model": "Qwen/Qwen2.5-7B-Instruct",
  "messages": [{"role": "user", "content": "简单解释数列极限ε-N定义"}]
}
headers = {
  "Authorization": f"Bearer {api_key}",
  "Content-Type": "application/json"
}

res = requests.post(url, json=payload, headers=headers)
data = res.json()
print(data["choices"][0]["message"]["content"])