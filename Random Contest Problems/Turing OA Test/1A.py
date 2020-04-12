from collections import defaultdict
from heapq import *

def dijakstra(n, edges, s):
    distance = [-1]*(n+1)
    # Initializing Source Distance
    distance[s] = 0
    # Pushing to queue
    q = [(distance[s], s)]
    # For storing path
    parent = {i: -1 for i in range(1, n + 1)}
    # Initialize visited
    visited = [False]*(n+1)

    while(q):
        now_dis, now_node = heappop(q)
        if(visited[now_node]==True):
            continue
        visited[now_node] = True
        for neighbour in edges[now_node]:
            curr_weight, curr_node = neighbour[1], neighbour[0]
            if(distance[curr_node]==-1):
                parent[curr_node] = now_node
                distance[curr_node] = distance[now_node] + curr_weight
                heappush(q, (distance[curr_node], curr_node))

            elif(distance[now_node]+curr_weight < distance[curr_node]):
                # store parent
                parent[curr_node] = now_node
                # Update weight
                distance[curr_node] = distance[now_node] + curr_weight
                # Push current node
                heappush(q, (distance[curr_node], curr_node))

    return parent, distance

# Function to get path using parent
def backtrace(parent, start, end):
    path = [end]
    while(path[-1]!=start and path[-1]>0):
        path.append(parent[path[-1]])
    path.reverse()
    return path


if __name__=="__main__":
    graph = defaultdict(list)


    source = int(input())
    dest = int(input())

    for i in range(10):
        ls = list(map(int, input()))
        for wiz in ls:
            graph[i].append([wiz, abs(wiz-i)**2])


    parent, distance = dijakstra(10, graph, source)

    path = backtrace(parent, source, dest)
    result = str(distance[dest]) + " " + "".join([str(elem) for elem in path])
    print(result)