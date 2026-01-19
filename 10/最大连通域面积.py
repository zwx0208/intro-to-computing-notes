def dfs(x,y,panel,visited,n,m):
    if x<0 or x>=n or y<0 or y>=m:
        return 0
    if visited[x][y] or panel[x][y]!='W':
        return 0
    visited[x][y]=True
    area=1
    directions=[[1,1],[1,0],[1,-1],[0,1],[0,-1],[-1,1],[-1,0],[-1,-1]]
    for dx,dy in directions:
        area+=dfs(x+dx,y+dy,panel,visited,n,m)
    return area
def main():
    t=int(input())
    for _ in range(t):
        n,m=map(int,input().split())
        panel=[]
        for _ in range(n):
            panel.append(list(input().strip()))
        max_area=0
        visited=[[False]*m for _ in range(n)]
        for x in range(n):
            for y in range(m):
                if panel[x][y] and not visited[x][y]:
                    area=dfs(x,y,panel,visited,n,m)
                    max_area=max(area,max_area)
        print(max_area)
if __name__=='__main__':
    main()