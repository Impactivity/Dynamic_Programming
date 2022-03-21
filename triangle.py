# _max = 0
#
#
# def dfs(inx, j, tot, triangle):
#     global _max
#     if inx == len(triangle):
#         _max = max(_max, tot)
#         return
#
#     for i in range(j, j + 2):
#         if i < len(triangle[inx]):
#             tmp = dfs(inx + 1, i, tot + triangle[inx][i], triangle)
#
#
# def solution(triangle):
#     dfs(0, 0, 0, triangle)
#
#     return


from collections import deque


def solution(triangle):
    queue = deque()
    visited = [[0] * i for i in range(1, len(triangle) + 1)]
    queue.append((0, 0))
    visited[0][0] = triangle[0][0]
    dx = [1, 1]
    dy = [0, 1]
    while queue:
        x, y = queue.popleft()

        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(triangle):
                if 0 <= ny < len(triangle[nx]):
                    if visited[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + triangle[nx][ny]
                        queue.append((nx, ny))

    print(visited)
    print(max(visited[len(triangle) - 1]))

    return