def isCycleUtil(i, graph, vis, parent, ar, flag):
    vis[i] = True
    ar.append(i)
    for neighbour in graph[i]:
        if(vis[neighbour]==False):
            if (len(graph[i]) != 2):
                flag = 1
            if(isCycleUtil(neighbour, graph, vis, i, ar, flag)):
                return True
        elif(neighbour!=parent):
            if(flag==0):
                return True

    return False


def isCycle(graph, vis, n):
    """
    1. Loop through the graph
    2. Take an Unvisited node as starting point to find cycle
    3. If a neighbouring node is Visited and not the parent then there is cycle

    Time Complexity = O(V+E)
    """
    c = 0
    for i in range(1,n+1):
        if(vis[i]==False):
            if(isCycleUtil(i, graph, vis, -1, [], 0)):
                c+=1

    return c



if __name__=="__main__":
    n,m = map(int, input().split())
    graph = {i:[] for i in range(1,n+1)}
    vis = {i:False for i in range(1,n+1)}
    for _ in range(m):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)

    print(isCycle(graph, vis, n))
