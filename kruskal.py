wgt_list=[]
cost=[[0 for x in range(30)]for y in range(30)]
size=int(input("no of vertices:"))
edges=int(input("no of edges:"))
for i in range(edges):
	print("Enter an edge:")
	u=int(input("First vertex"))
	v=int(input("Next vertex"))
	w=int(input("Enter the weight between them"))
	wgt_list.append(w)	
	cost[u][v]=w
	cost[v][u]=w
wgt_list.sort()
print(wgt_list)

count=0

component=[]
for i in range(size):
	component.append(i)


while count<size-1:
	if len(wgt_list)!=0:
		ek=wgt_list.pop(0)
		for u in range(size):
			for v in range(size):
				if cost[u][v]==ek and  component[u]!=component[v]:
					print("U----->V",u,v)
					count=count+1
					for j in range(size):
						if component[j]==component[v]:
							for k in range(size):
								if component[k]==component[u]:
									component[k]=component[j]
							

				

				

