def solve_subset_sum (v, target, solution, k, rest, x):
    rest -= v[k]
    # caso 1: non considero xk nella soluzione
    x[k] = 0
    xc = x.copy()

    if solution + rest >= target and solution + v[k+1] <= target:
        solve_subset_sum(v, target, solution, k + 1, rest, xc)

    # caso 1: considero xk nella soluzione
    x[k] = 1
    xc1 = x.copy()
    if solution + v[k] == target:
        print(x)
        return
    else:
        solution += v[k]
        if solution + v[k+1] <= target:
            solve_subset_sum(v, target, solution, k + 1, rest, xc1)

def subset_sum (v, target):
    x = [0] * len(v)
    solve_subset_sum(v, target, 0, 0, sum(v), x)

valori = [7,11,13,24]
M = 31
subset_sum(valori, M)
