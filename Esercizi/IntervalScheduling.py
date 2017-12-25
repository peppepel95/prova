from queue import PriorityQueue

def intervalScheduling(tasks = {}):
    if len(tasks) is 0:
        return

    pq = PriorityQueue()
    ordered = {}
    solution = []
    for task in tasks.keys():
        pq.put((tasks[task][1], (task, tasks[task])))

    i = 0
    while not pq.empty():
        key, ordered[i] = pq.get()
        i += 1

    i = 0
    curr_f = 0
    while i < len(ordered):
        while ordered[i][1][0] < curr_f:
            i += 1
        solution.append(ordered[i][0])
        curr_f = ordered[i][1][1]
        i += 1

    return solution



tasks = {}

tasks["a"] = (0,6)
tasks["b"] = (1,4)
tasks["c"] = (3,5)
tasks["d"] = (3,8)
tasks["e"] = (4,7)
tasks["f"] = (5,9)
tasks["g"] = (6,10)
tasks["h"] = (8,11)

print(intervalScheduling(tasks))