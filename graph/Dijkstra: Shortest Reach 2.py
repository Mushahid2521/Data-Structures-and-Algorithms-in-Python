from heapq import *
from collections import defaultdict


def shortestReach(n, edges, s):
    distance = [-1]*(n+1)
    distance[s] = 0
    q = [(distance[s], s)]

    visited = [False]*(n+1)
    while(q):
        now_dis, now_node = heappop(q)
        if(visited[now_node]==True):
            continue
        visited[now_node] = True
        for neighbour in edges[now_node]:
            curr_weight, curr_node = neighbour[1], neighbour[0]
            if(distance[curr_node]==-1):
                distance[curr_node] = distance[now_node] + curr_weight
                heappush(q, (distance[curr_node], curr_node))
            elif(distance[now_node]+curr_weight < distance[curr_node]):
                distance[curr_node] = distance[now_node] + curr_weight
                heappush(q, (distance[curr_node], curr_node))

    del distance[s]
    return distance[1:]


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        graph = defaultdict(list)


        for _ in range(m):
            u,v,w = map(int, input().split())
            graph[u].append([v,w])
            graph[v].append([u,w])

        s = int(input())

        result = shortestReach(n, graph, s)

        print(result)



