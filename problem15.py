def grid_routes(n, i, j):
    if path_count_map[i][j] != 0: return path_count_map[i][j]
    path_count_map[i][j] = grid_routes(n, i+1, j) + grid_routes(n, i, j+1)
    return path_count_map[i][j]

# Setup the map
n = 500
path_count_map  = []
for i in range(n+1):
    path_count_map.append([])
    for j in range(n+1):
        path_count_map[i].append(0)
        if i == n or j == n: path_count_map[i][j] = 1

grid_routes(n, 0, 0)
print path_count_map[0][0]
# for arr in path_count_map:
#     print arr