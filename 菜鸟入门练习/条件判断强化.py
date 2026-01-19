# 要求：输入身高(m)和体重(kg)，计算BMI并判断健康状况
# BMI = 体重 / (身高^2)
# 判断标准：
# BMI < 18.5：偏瘦
# 18.5 ≤ BMI < 24：正常
# 24 ≤ BMI < 28：超重
# BMI ≥ 28：肥胖
height=float(input('请输入身高（米）'))
weight=int(input('请输入体（千克）'))
BMI=weight/(height**2)
if BMI<18.5:
    print('偏瘦')
elif 18.5<=BMI<24:
    print('正常')
elif 24<=BMI<28:
    print('超重')
else:print('肥胖')