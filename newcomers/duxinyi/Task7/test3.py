def calculate(prices,**kwargs):
    """
    根据原价，计算折扣、税率和其他费用后的总价
    输入：原价列表，其他参数
    输出：总价列表
    """
    discount = kwargs.get('discount', 1.0)
    tax_rate = kwargs.get('tax_rate', 1.0)
    others = kwargs.get('others', 0)
    total_list = []
    for price in prices:
        total_list.append(price * discount * tax_rate + others)
    return total_list

base_prices = []
while True:
    price = float(input("请输入商品原价（输入0退出）："))
    if price == 0:
        break
    base_prices.append(price)

print("-----商品总价计算-----")
a = float(input("请输入折扣（如0.8表示八折，默认为1）：") or 1)
b = float(input("请输入税率（如1.2表示加20%税，默认为1）：") or 1)
c = float(input("请输入其他费用（单位默认为0）：") or 0)

totals = calculate(base_prices, discount=a, tax_rate=b, others=c)
for i, total in enumerate(totals):
    print(f"商品 {i+1} 的总价为：{total:.2f}")