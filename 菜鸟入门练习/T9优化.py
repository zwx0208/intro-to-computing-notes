for j in range(1, 10):
    for i in range(1, j + 1):  # 只需循环到j即可
        print(f'{i}*{j}={i*j} ', end='')
    print()  # 每行结束后换行（*重要*）