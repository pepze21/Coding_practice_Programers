
# 플로이드 워셜

# 다익스트라

# 시간초과 96.7점
# from collections import defaultdict
#
# def dfs1(start, end, w, d, edge_w, n):
#     for e in edge_w[start]:
#         if (w + e[1] < d[e[0]]) and (w + e[1] < d[end]):
#             d[e[0]] = w + e[1]
#             dfs1(e[0], end, w + e[1], d, edge_w, n)
#
# def dfs2(start, search_range, w, d, edge_w, n):
#     for e in edge_w[start]:
#         if (w + e[1] < d[e[0]]) and (w + e[1] < search_range):
#             d[e[0]] = w + e[1]
#             dfs2(e[0], search_range, w + e[1], d, edge_w, n)
#
# def solution(n, s, a, b, fares):
#     edge_w = defaultdict(list)
#     for f in fares:
#         edge_w[f[0]].append([f[1], f[2]])
#         edge_w[f[1]].append([f[0], f[2]])
#
#     d = [0] * (n + 1)
#     da = [20000001] * (n + 1)
#     db = [20000001] * (n + 1)
#     ds = [20000001] * (n + 1)
#     da[a] = db[b] = ds[s] = 0
#
#     dfs1(a, s, 0, da, edge_w, n)
#     dfs1(b, s, 0, db, edge_w, n)
#     dfs2(s, da[s] + db[s], 0, ds, edge_w, n)
#
#     for i in range(len(d)):
#         d[i] = da[i] + db[i] + ds[i]
#
#     return min(d)

# 시간초과 85점
# from collections import defaultdict
#
# def dfs(node, w, d, edge_w, n, s, end1, end2):
#     for e in edge_w[node]:
#         if (w + e[1] < d[e[0]]) and max(end1, end2):
#             d[e[0]] = w + e[1]
#             dfs(e[0], w + e[1], d, edge_w, n, s, a, b)
#
# def solution(n, s, a, b, fares):
#     edge_w = defaultdict(list)
#     for f in fares:
#         edge_w[f[0]].append([f[1], f[2]])
#         edge_w[f[1]].append([f[0], f[2]])
#
#     d = [0] * (n + 1)
#     da = [20000001] * (n + 1)
#     db = [20000001] * (n + 1)
#     ds = [20000001] * (n + 1)
#     da[a] = db[b] = ds[s] = 0
#
#     dfs(a, 0, da, edge_w, n, s, b, s)
#     dfs(b, 0, db, edge_w, n, s, s, a)
#     dfs(s, 0, ds, edge_w, n, s, a, b)
#
#     for i in range(len(d)):
#         d[i] = da[i] + db[i] + ds[i]
#
#     return min(d)