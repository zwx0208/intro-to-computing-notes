def exist(board, word):
    m, n = len(board), len(board[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 上下左右

    def dfs(x, y, index):
        # ========== 终止条件（容易漏！） ==========
        # 1. 成功：匹配完所有字符
        if index == len(word):
            return True

        # 2. 越界检查（必须放在前面！）
        if x < 0 or x >= m or y < 0 or y >= n:
            return False

        # 3. 已访问或不匹配
        if visited[x][y] or board[x][y] != word[index]:
            return False
        # =======================================

        # 选择
        visited[x][y] = True
        # 四个方向探索
        for dx, dy in directions:
            if dfs(x + dx, y + dy, index + 1):  #递归
                return True  # 找到了就返回并结束
        # 回溯，撤销选择
        visited[x][y] = False

        return False  # 四个方向都不行

    # 主程序：尝试每个起点
    visited = [[False] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:  # 首字母匹配才需要搜索
                if dfs(i, j, 0):
                    return True

    return False