from itertools import permutations

def calculate_cost(p):
    cost=0
    for i in range(1,n+1):
        c=0
        if i!=n:
            c=costs[p[i-1]][p[i]]# cost adding
        else:
            c=costs[p[n-1]][p[0]] # going back to start
        if c==0:
            break
        cost+=c
    return cost
def find(s):
    paths=list(range(n))
    paths.remove(s)
    paths=list(permutations(paths))
    min=float('inf')
    path=[]
    for i in paths:
        i=[s]+list(i)+[s]
        c=calculate_cost(i)
        if c:
            if c<min:
                min=c
                path=i
    return [path,min]
    
n=int(input("enter the no of nodes:"))#4
costs=[]
print("enter the adjacency matrix directed or undirated(0 if no edge or self cost):")
for i in range(n):
    costs.append(list(map(int,input().split())))
#example adjacency matsx
# costs=[[0 ,10, 15, 20],
#     [10 ,0 ,35 ,25],
#     [15, 35, 0 ,30], 
#     [20 ,25, 30, 0]]
s=int(input("enter the start(nodes start with index 0 not 1):"))
a=find(s)
print(a)
