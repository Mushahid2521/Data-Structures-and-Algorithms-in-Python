"""
    Given the dependencies of each tasks, print the possible order of accomplishment
"""

while True:
    n, m = map(int, input().split())
    if(n==m==0):
        break

    graph = {i:[] for i in range(1,n+1)}
    inDegree = {i:0 for i in range(1,n+1)}
    task_order = []

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        inDegree[v]+=1


    queue = []
    for i in range(1,n+1):
        if(inDegree[i]==0):
            queue.append(i)

    while queue:
        now = queue.pop(0)
        task_order.append(now)
        for idx in graph[now]:
            if(inDegree[idx]>0):
                inDegree[idx]-=1
                if(inDegree[idx]==0):
                    queue.append(idx)


    # while len(task_order)<n:
    #     dm = []
    #     for i in range(1,n+1):
    #         if(inDegree[i]==0):
    #             dm.append(i)
    #
    #     for i in dm:
    #         inDegree[i]=-1
    #         task_order.append(i)
    #         for idx in graph[i]:
    #             inDegree[idx]-=1



    print(task_order)


