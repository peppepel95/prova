from Progetto_4.Utilities import generateGraph
import cProfile
import pstats

for i in range(50):


    print('\033[1;31m_____________________________i =\033[1;m',i)

    print('\033[1;31m_____________________________min_vertex_cover\033[1;m')
    G = generateGraph(50, 250 + i*15)

    print("Random graph generated")

    vertex_cover = []
    cProfile.run("vertex_cover = G.min_vertex_cover()", "test")
    p = pstats.Stats('test')
    p.files.pop(0)
    p.print_stats(0)
    print(len(vertex_cover))

    """

    print('\033[1;31m______________________________min_vertex_cover\033[1;m')

    vertex_cover = None

    cProfile.run("vertex_cover = G._min_vertex_cover()")

    print(len(vertex_cover))
    """