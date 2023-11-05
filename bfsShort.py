n=int(input("enter no of nodes: "))
cons=[]
for i in range(n):
    cons.append(list(map(int,input(f"enter connection from node {i}: ").split())))

s=int(input("enter start node: "))

visited=[s]
queue=[s]
while queue:
    a=queue.pop(0)
    visited.append(a)
    print(a,end="->")
    for i in cons[a]:
        if i not in visited:
            queue.append(i)