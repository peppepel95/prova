from Progetto_4.Utilities import generateGraph
import cProfile

G = generateGraph(40, 120)

vertex_cover = None

cProfile.run("vertex_cover = G.min_vertex_cover()")


sum = 0
if vertex_cover is not None:
    for v in vertex_cover:
        if vertex_cover[v]:
            sum += 1
    print(sum)