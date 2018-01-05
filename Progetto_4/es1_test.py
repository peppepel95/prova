from Utilities import generateGraph
import cProfile

G = generateGraph(50, 300)

print("Random graph generated")

vertex_cover = None

cProfile.run("vertex_cover = G.mvc()")


sum = 0
if vertex_cover is not None:
    for v in vertex_cover:
        if vertex_cover[v]:
            sum += 1
    print(sum)


G = generateGraph(50, 300)

print("Random graph generated")

vertex_cover = None

cProfile.run("vertex_cover = G.mvc()")


sum = 0
if vertex_cover is not None:
    for v in vertex_cover:
        if vertex_cover[v]:
            sum += 1
    print(sum)


G = generateGraph(50, 300)

print("Random graph generated")

vertex_cover = None

cProfile.run("vertex_cover = G.mvc()")


sum = 0
if vertex_cover is not None:
    for v in vertex_cover:
        if vertex_cover[v]:
            sum += 1
    print(sum)

G = generateGraph(50, 300)

print("Random graph generated")

vertex_cover = None

cProfile.run("vertex_cover = G.mvc()")


sum = 0
if vertex_cover is not None:
    for v in vertex_cover:
        if vertex_cover[v]:
            sum += 1
    print(sum)

G = generateGraph(50, 300)

print("Random graph generated")

vertex_cover = None

cProfile.run("vertex_cover = G.mvc()")


sum = 0
if vertex_cover is not None:
    for v in vertex_cover:
        if vertex_cover[v]:
            sum += 1
    print(sum)
