from collections import defaultdict

def dfs_visit(node, graph, color, time, d, f):
    time+=1
    color[node] = 'Gray'
    d[node] = time
    for neighbour in graph[node]:
        if(color[neighbour]=='Black'):
            continue
        elif(color[neighbour]=='Gray'):
            return True
        elif(dfs_visit(neighbour, graph, color, time, d, f)==True):
            return True

    color[node] = 'Black'
    time+=1
    f[node] = time
    return False



def isCyclic(n, graph):
    color = ['White']*(n+1)
    d = [0]*(n+1)
    f = [0]*(n+1)

    for i in range(n+1):
        if(color[i]=='White'):
            if(dfs_visit(i,graph,color, 0, d, f)):
                return True

    return False


d = defaultdict(list)

d[0].append(0)
d[0].append(1)

# print(d)

print(isCyclic(2,d))