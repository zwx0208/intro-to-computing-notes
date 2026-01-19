count = 1
while count <= 5:
    print(f"当前数字: {count}")
    count += 1
    if count == 3:
        count += 1
        continue  # 跳过 3 的输出
