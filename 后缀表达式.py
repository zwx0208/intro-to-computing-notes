def main():
    import sys

    # 读取所有输入
    data = sys.stdin.read().strip().split('\n')
    if not data:
        return

    n = int(data[0])

    # 处理每个表达式
    for i in range(1, n + 1):
        expr = data[i]
        stack = []
        tokens = expr.split()

        for token in tokens:
            if token in '+-*/':
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    result = a + b
                elif token == '-':
                    result = a - b
                elif token == '*':
                    result = a * b
                elif token == '/':
                    result = a / b

                stack.append(result)
            else:
                stack.append(float(token))

        print(f"{stack[0]:.2f}")


if __name__ == "__main__":
    main()