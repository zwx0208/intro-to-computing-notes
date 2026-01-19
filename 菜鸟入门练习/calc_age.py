import datetime

birth_year = int(input("请输入你的出生年份（例如 1990）："))
current_year = datetime.datetime.now().year   # 自动获取当前年份
age = current_year - birth_year
print(f"你今年 {age} 岁。")
for i in range(1, 6):  # 1~5
    future_year = current_year + i
    age_in_future = age + i
    print(f"{future_year} 年，你将 {age_in_future} 岁。")
