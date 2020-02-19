from collections import defaultdict
from heapq import *

def dijakstra(n, edges, s):
    """
    Dijakstra: BFS with weights considered, in BFS weight 1 is taken
    Steps:
    1. Initialize a distance array with INF or -1
    2. Set the distance of source to 0
    3. Using a Priority queue get the smallest weight node
    4. Update the distance if new distance is smaller

    Time Complexity: O(VlogV+E). ->> logV for priority sort in each node.
    """
    # Initializing Distance
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
            # If -1 or INF
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
    n, m = map(int, input().split())

    graph = defaultdict(list)

    for _ in range(m):
        u,v,w = map(int, input().split())
        graph[u].append([v,w])
        graph[v].append([u,w])


    parent, _ = dijakstra(n, graph, 1)

    if(parent[n]==-1):
        print(-1)
    else:
        print(*backtrace(parent,1,n))