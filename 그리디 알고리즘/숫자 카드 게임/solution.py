col, row = map(int, input().split(" "))

graph = [list(map(int, input().split(" "))) for _ in range(col)]

minimun = min(graph[0])
for i in range(1, col, 1):
    if minimun < min(graph[i]):
        minimun = min(graph[i])
print(minimun)

# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

# 2 4
# 7 3 1 8
# 3 3 3 4