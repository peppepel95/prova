def dp_coin_change(amount, coins= [0, 1, 2, 5, 10, 20, 50]): #coins[0] non è usato
    nc = len(coins)
    m = [[0]*(amount+1) for _ in range(1,nc+1)]

    for r in range(amount+1):
        m[1][r] = r

    for i in range(2,len(coins)):
        for r in range(1,amount+1):
            if coins[i] == r:
                m[i][r] = 1
            elif coins[i] > r:
                m[i][r] = m[i-1][r]
            else:
                m[i][r] = min(m[i-1][r], m[i][r-coins[i]]+1)

    return m, m[-1][-1] #m[nc][amout]

def printChange(m, coins= [0, 1, 2, 5, 10, 20, 50]):
    nc = len(coins) - 1
    amount = len(m[0]) - 1
    sol = []

    if m[-1][-1] == 0:
        return

    while amount > 0:
        temp = m[nc][amount]
        while m[nc-1][amount] <= temp and m[nc-1][amount] is not 0:
            nc -= 1
        if nc is not 0:
            sol.append(coins[nc])
        amount = amount - coins[nc]

    return sol


def printMatrice(M):
    for i in range(len(M)):
        print("[", end="")
        for j in range(len(M[i])):
            if j == len(M[i]) - 1:
                print("{:3}".format(M[i][j]), end="")
            else:
                print("{:3}{}".format(M[i][j], ","), end="")
        print("]\n")
    print()


m, s = dp_coin_change(289)

printMatrice(m)

print(s)

print(printChange(m))