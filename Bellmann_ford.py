def minimum(a,b):
    if a < b:
        return a
    else:
        return b
def bf(adj_list,n,s):
    distance = [100000 for i in range(n+1)]
    distance[s] = 0
    edges = []
    for i in adj_list:
        #print(i)
        for pair in adj_list[i]:
            temp = [i,pair[0],pair[1]]
            edges.append(temp)
    for i in range(n-1):
        for pair in edges:
            distance[pair[1]] = minimum(distance[pair[1]],distance[pair[0]]+pair[2])
    del(distance[0])
    print(distance)

def main():
    n = int(input("Enter the number of vertices:"))
    m = int(input("Enter the number of edges:"))
    adj_list = {}
    for i in range(n):
        adj_list[i+1] = []
    for i in range(m):
        vertex1 = int(input())
        vertex2 = int(input())
        weight = int(input())
        temp = (vertex2,weight)
        adj_list[vertex1].append(temp)
        #temp = (vertex1,weight)
        #adj_list[vertex2].append(temp)
    #print(adj_list)
    source = int(input("Enter a source:"))
    bf(adj_list,n,source)

main()
