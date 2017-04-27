def maximum(a,b):
    if a >= b:
        return a
    else:
        return b
def Subset(n,w,W):
    M = [[0 for i in range(W+1)] for j in range(n+1)]
    i = 1
    while i <= n:
        x = 1
        while x <= W:
            if w[i] > x:
                M[i][x] = M[i-1][x]
            else:
                M[i][x] = maximum(M[i-1][x],w[i]+M[i-1][x-w[i]])
            #print(i,x,M[i][x],sep=' ')
            x = x + 1
        i = i + 1
    return M
def Knapsack(M,n,W,w):
    i = n
    k = W
    contents = []
    while i > 0 and k > 0 :
        #print(i,k,w[i],sep=' ')
        #print(M[i][k],M[i-1][k],sep='   ')
        if M[i][k] != M[i-1][k] and M[i][k] > 0:
            contents.append(i)
            #print(contents)
            k = k - w[i]
            i = i -1
        else:
            i = i - 1
    return contents
def main():
    n = int(input("Enter the number of items:"))
    w = [0]
    for i in range(n):
        temp = int(input("Weight of item {0} :".format(i+1)))
        w.append(temp)
    W = int(input("Max_weight:"))
    M = Subset(n,w,W)
    print(" The maximum weight the bag can contain is : {0}".format(M[n][W]))
    contents = Knapsack(M,n,W,w)
    print("The contents of the bag are : {0}".format(contents))
    return
main()