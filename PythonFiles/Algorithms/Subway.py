from sys import maxsize

def travelling_salesman_function(graph,subset,s):
    vertex = []
    path=[]
    temp=[]
    id=[]
    for node in subset:
        id.append(node.station_id-1)
    for i in range(len(graph)):
        if i != s and graph[s][i]>0 and i in id:
            vertex.append(i)
    print (vertex)
    min_path = maxsize
    check=min_path
    while True:
        current_cost = 0
        temp.clear()
        temp.append(s+1)
        k = s
        for i in range(len(vertex)):
            current_cost += graph[k][vertex[i]]
            temp.append(vertex[i]+1)
            k = vertex[i]
        current_cost += graph[k][s]
        temp.append(s+1)
        print (min_path)
        min_path = min(min_path, current_cost)
        if min_path<check:
            path=temp.copy()
            check=min_path
        

        if not next_perm(vertex):
            break
    return path

def next_perm(l):
    n = len(l)
    i = n-2

    while i >= 0 and l[i] > l[i+1]:
        i -= 1
    
    if i == -1:
        return False

    j = i+1
    while j < n and l[j] > l[i]:
        j += 1

    j -= 1

    l[i], l[j] = l[j], l[i]
    left = i+1
    right = n-1

    while left < right:
        l[left], l[right] = l[right], l[left]
        left += 1
        right -= 1
    return True
