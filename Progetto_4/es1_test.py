from Progetto_4.Utilities import generateGraph
import cProfile

for i in range(50):


    print('\033[1;31m_____________________________i =\033[1;m',i)

    print('\033[1;31m_____________________________mvc\033[1;m')
    G = generateGraph(50, 20)

    print("Random graph generated")

    vertex_cover = None

    cProfile.run("vertex_cover = G.min_vertex_cover()")


    sum = 0
    if vertex_cover is not None:
        for v in vertex_cover:
            if vertex_cover[v]:
                sum += 1
        print(sum)

    print('\033[1;31m_____________________________min_vertex_cover\033[1;m')

    vertex_cover = None

    cProfile.run("vertex_cover = G._min_vertex_cover()")

    sum = 0
    if vertex_cover is not None:
        for v in vertex_cover:
            if vertex_cover[v]:
                sum += 1
        print(sum)