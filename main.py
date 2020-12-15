'''
edge class:
  u : from vertex
  v : to vertex
  w : weight of edge
  vis : boolean for if visited
  id : unique integer for the edge
'''


class edge:
    def __init__(self, u, v, w, vis, id):
        self.u = u
        self.v = v
        self.w = w
        self.vis = vis
        self.id = id


def swap(a, b):
    return b, a


def fill_edges(G):
    edges = []
    counter = 0
    for i in range(len(G)):
        for j in range(i + 1, len(G)):
            temp = edge(i, j, G[i][j], False, counter)
            edges.append(temp)
            counter += 1

    edges.sort(key=lambda x: x.w)
    return edges


'''
find_set, union_sets and make_set are all based on a generic 
disjoint union data structure
https://cp-algorithms.com/graph/mst_kruskal_with_dsu.html
'''


def find_set(v, parent):
    if (v == parent[v]):
        return v
    return find_set(parent[v], parent)


def union_sets(a, b, rank, parent):
    a = find_set(a, parent)
    b = find_set(b, parent)
    if (a != b):
        if (rank[a] < rank[b]):
            a, b = swap(a, b)
        parent[b] = a
        if (rank[a] == rank[b]):
            rank[a] += 1


def make_set(n):
    parent = [0] * n
    rank = [0] * n
    for i in range(n):
        parent[i] = i
        rank[i] = 1

    return parent, rank


# This algorithm follows the principles in the example used on this website: https://cp-algorithms.com/graph/mst_kruskal_with_dsu.html
'''
- Sort the edges in decreasing order by their weights
- The make_set() function is called to assign a set to every edge
- find_set iterates through and checks if beginning vertex != end vertex
- If the vertices are not in the same set, append the edge to a list of edges and call union_sets() to combine them into one set
- Check if tree length == N-1 and if the tree already exists in the list 
- If the tree is not already in the list, add the tree and its cost to the list
'''


def kruskal(edges, n):
    results = []
    costs = []
    cost = 0
    all_paths = []
    num_visited = len(edges) - 1
    for i in range(n):
        parent, rank = make_set(n)
        for e in range(0, len(edges)):
            if i != edges[e].id:
                if find_set(edges[e].u, parent) != find_set(edges[e].v, parent):
                    cost += edges[e].w
                    if not edges[e].vis:
                        edges[e].vis = True
                        num_visited -= 1
                    results.append(edges[e].id)
                    union_sets(edges[e].u, edges[e].v, rank, parent)
        if len(results) == n - 1:
            if results not in all_paths:
                costs.append(cost)
                all_paths.append(results)
        cost = 0
        results = []

    return costs


def fill_array(input_file_path):
    inputfile = open(input_file_path)
    n = int(float(inputfile.readline()))
    a = list()
    for i in range(n):
        row = inputfile.readline().split(',')
        for j in range(n):
            row[j] = int(row[j])
            # print(row)
        a.append(row)
    return a, n


def first_second_third_mst(input_file_path, output_file_path):
    G, n = fill_array(input_file_path)
    edges = fill_edges(G)

    result = kruskal(edges, n)
    result.sort(key=lambda x: x)
    if (len(result)) > 3:
        result = result[0:3]
    print(result)

    with open(output_file_path, "w") as file:
        for i in result:
            file.write(str(i) + "\n")

    return

#print(first_second_third_mst(".in", ".out"))
