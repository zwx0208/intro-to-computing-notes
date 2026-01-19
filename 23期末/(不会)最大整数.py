from functools import cmp_to_key


def main():
    m = int(input())  # 最大位数
    n = int(input())  # 数字个数
    nums = input().split()  # 数字列表（字符串）

    # 1. 按拼接比较规则排序
    def cmp(a, b):
        return -1 if a + b > b + a else 1 if a + b < b + a else 0

    nums.sort(key=cmp_to_key(cmp))

    # 2. DP：dp[j] = 恰好用 j 位能组成的最大数字
    dp = [""] * (m + 1)

    for num in nums:
        L = len(num)
        for j in range(m, L - 1, -1):  # 01背包倒序
            if dp[j - L] != "" or j - L == 0:  # 前j-L位有解
                cand = dp[j - L] + num
                # 选更大的（先比长度，再比字典序）
                if len(cand) > len(dp[j]) or (len(cand) == len(dp[j]) and cand > dp[j]):
                    dp[j] = cand

    # 3. 找出所有位数 ≤ m 中最大的
    ans = ""
    for j in range(1, m + 1):
        if len(dp[j]) > len(ans) or (len(dp[j]) == len(ans) and dp[j] > ans):
            ans = dp[j]

    print(ans)


if __name__ == "__main__":
    main()