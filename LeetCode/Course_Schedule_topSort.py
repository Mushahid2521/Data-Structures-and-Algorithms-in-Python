def canFinish(numCourses, prerequisites):
    '''
    TopSort is used to arrange the sequence of dependent tasks
    1. We first count the number of In Degrees from the Graph (edges entering in a node)
    2. We push the 0 indegrees nodes to the queue
    3. We loop through the adjacent nodes and then decrease the indegrees
    4. If after decreasing it become 0 then we push it to the queue

    Time Complexity: O(N^2)
    '''
    graph = {i: [] for i in range(0, numCourses)}
    inDegree = {i: 0 for i in range(0, numCourses)}
    vis = {i:False for i in range(0, numCourses)}
    res = []


    for reqs in prerequisites:
        graph[reqs[1]].append(reqs[0])
        inDegree[reqs[0]]+=1


    queue = []
    for i in range(numCourses):
        if(inDegree[i]==0):
            queue.append(i)

    while queue:
        now = queue.pop(0)
        res.append(now)
        for neighbour in graph[now]:
            if vis[neighbour]==False:
                inDegree[neighbour]-=1
                if(inDegree[neighbour]==0):
                    vis[neighbour] = True
                    queue.append(neighbour)

    for key in inDegree.keys():
        if(inDegree[key]>0):
            return []

    return res




print(canFinish(2, [[1,0]]))