import numpy as np


def AlgoFloyd(L):
    # La matrice P appelée la matrice des prédécesseurs est telle que le terme Pij représente le numéro du sommet prédécesseur immédiat de j sur le plus court chemin entre i et j
    n, m = L.shape
    if n != m:
        raise ValueError("La matrice des coûts n'est pas carrée")

    A = L
    P = np.zeros((n, n))
    for i in range(n):
        P[i, :] = i * np.ones(n)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if A[i, k] + A[k, j] < A[i, j]:
                    A[i, j] = A[i, k] + A[k, j]
                    P[i, j] = P[k, j]
    return A, P


# Matrice des coûts



def CheminFloyd(A, P, dep, arv):
    if A[dep, arv] == np.inf:
        print(f"Il n'existe pas de chemin entre les sommets depart = {dep} et arrive = {arv}")
    else:
        j = arv
        chemin = [j]
        while j != dep:
            j = int(P[dep, j])
            chemin = [j] + chemin
        print(f"Le plus court chemin entre les sommets depart = {dep} et arrive = {arv}")
        print(chemin)
    return chemin

C = np.array([[0, 15, np.inf, np.inf, 4],
              [np.inf, 0, np.inf, np.inf, np.inf],
              [np.inf, 3, 0, 2, np.inf],
              [10, 3, np.inf, 0, np.inf],
              [np.inf, np.inf, 7, 5, 0]])
A, P = AlgoFloyd(C)

y = CheminFloyd(A, P, 0, 1)
