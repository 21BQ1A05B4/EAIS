def dfs(a):
    print(a, end="->")
    for i in con[a]:
        if i not in visited:
            visited.append(i)
            dfs(i)
n = int(input("enter the number of nodes:"))
con = []
for i in range(n):
    con.append(list(map(int, input(f"enter the conn from {i}:").split())))
s = int(input("enter the start node:"))
visited = []
visited.append(s)
dfs(s)