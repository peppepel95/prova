from Progetto_4.Utilities import generateGraph
import cProfile
import pstats

G = generateGraph(10, 20)

vertex_cover = []
cProfile.run("vertex_cover = G.min_vertex_cover()", "test")
p = pstats.Stats('test')
p.files.pop(0)
p.print_stats(0)
str = p.get_top_level_stats()
print(len(vertex_cover))