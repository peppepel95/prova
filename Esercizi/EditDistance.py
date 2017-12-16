
def editDistance (s1, s2):

    n, m = len(s1), len(s2)

    M = [[0] * (m+1) for k in range(n+1)] #matrice n+1 x m+1

    for k in range(1,n+1):
        M[k][0] = k
    for k in range(1,m+1):
        M[0][k] = k

    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                t = 0
            else:
                t = 1
            M[i+1][j+1] = min(M[i][j] + t, M[i][j+1] + 1, M[i+1][j] + 1)

    return M

def printMatriceED(M):
    for i in range(len(M) - 1):
        print(M[i])
    print("[", end="")
    for j in range(len(M[-1])):
        if j == len(M[-1]) - 1:
            print('\033[91m', M[-1][j], '\033[0m', end="", sep="")
        else:
            print(M[-1][j] , ",", end=" ", sep="")
    print("]\n")

printMatriceED(editDistance("casa","capa"))