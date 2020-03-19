#from collections import defaultdict

result = set()

def ap_find(graph, u, visited, d, low, time, parent, start):
    global result

    time = time+1
    d[u] = time
    low[u] = time
    visited[u] = True
    no_of_childs = 0

    for v in graph[u]:
        if(v==parent[u]):
            continue
        elif(visited[v]):
            low[u] = min(low[u], d[v])
        elif(not visited[v]):
            parent[v] = u
            ap_find(graph, v, visited, d, low, time, parent, start)

            low[u] = min(low[u], low[v])

            if(low[v]>=d[u] and u!=start):
                result.add(u)

            no_of_childs+=1
        if(no_of_childs>1 and u==start):
            result.add(u)




if __name__=="__main__":
    while True:
        n = int(input())
        if(n==0):
            break

        graph = {i:[] for i in range(1,n+1)}

        while True:
            l = list(map(int, input().split()))
            if(len(l)==1):
                break

            for i in range(1, len(l)):
                graph[l[0]].append(l[i])
                graph[l[i]].append(l[0])

        visited = [False]*(n+1)
        d = [0]*(n+1)
        low = [0]*(n+1)
        time = 0
        parent = [-1]*(n+1)

        ap_find(graph, 1, visited, d, low, time, parent, 1)

        print(len(result))
        result = set()

