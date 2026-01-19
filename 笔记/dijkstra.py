import heapq

def dijkstra(start_x, start_y, end_x, end_y, grid):
    n, m = len(grid), len(grid[0])

    # 初始化距离
    dist = [[float('inf')] * m for _ in range(n)]
    dist[start_x][start_y] = 0

    # 优先队列 (距离, x, y) 距离优先的最小堆
    pq = [(0, start_x, start_y)]
    heapq.heapify(pq)

    while pq:
        d, x, y = heapq.heappop(pq)

        # 找到终点
        if (x, y) == (end_x, end_y):
            return d

        # 优化：如果当前距离大于记录的距离，跳过
        if d > dist[x][y]:
            continue

        # 遍历四个方向
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and 不是障碍:
                # 计算新距离（根据题目要求）
                new_dist = d + 权重计算(grid[x][y], grid[nx][ny])

                # 如果找到更短路径
                if new_dist < dist[nx][ny]:
                    dist[nx][ny] = new_dist
                    heapq.heappush(pq, (new_dist, nx, ny))  #入堆

    return -1  # 无法到达