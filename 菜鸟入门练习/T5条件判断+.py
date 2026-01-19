# 要求：根据购物金额计算实际付款
# 折扣规则：
# 金额 < 100：无折扣
# 100 ≤ 金额 < 500：9折
# 500 ≤ 金额 < 1000：8折
# 金额 ≥ 1000：7折
# 示例：
# 输入：380
# 输出：原价380元，折后342.0元
price=int(input('金额'))
if 100<=price<500:
    pay=price*0.9
elif 500<=price<1000:
    pay=price*0.8
elif price>1000:
    pay=price*0.7
else:
    pay=price
print(f'原价{price}元，折后{pay:.2f}元。')