while True:
    n=int(input())
    if n==0:
        break
    hotels=[tuple(map(int,input().split())) for _ in range(n)]
    hotels.sort(key=lambda x:(x[0],x[1]))  #先看第一项（距离从小到大），距离相同时看第二项（价格升序）
    candidates=1                           #第一个一定满足条件，因为距离最小
    max_cost_so_far=hotels[0][1]
    for i in range(n):
        if hotels[i][1]<max_cost_so_far:   #如果价格比前面酒店都低说明：比他便宜的都比他远（也可能没有），比他更近的（前面的）都比他更贵
            candidates+=1
            max_cost_so_far=hotels[i][1]
    print(candidates)
 #太巧妙了