## Generate data first

import numpy as np

## Calculate the distance between two people
def distance(x, y):
    d = 0
    n_movies = len(x)
    for i in range(n_movies):
        d += abs(x[i] - y[i])
    return d

def get_similarity(data, u):
    n_users = data.shape[0]
    similarity = np.zeros(n_users)
    for v in range(n_users):
        if (v != u):
            similarity[v] = np.exp(-distance(data[u], data[v]))
    return similarity / np.sum(similarity)
        
def generate_random_data(n_users, n_movies, gamma):
    data = np.zeros([n_users, n_movies])
    rating_dist = [0.1, 0.2, 0.3, 0.3, 0.1]
    for u in range(n_users):
        n_ratings = np.random.geometric(gamma)
        ratings = np.random.permutation(range(n_movies))[0:n_ratings]
        for m in ratings:
            data[u,m] = 1 + np.random.choice(5,1, p=rating_dist)
    return data


def infer_ratings(data, linkage):
    n_users = data.shape[0]
    n_movies = data.shape[1]
    inferred_ratings = data
    for u in range(n_users):
        w = get_similarity(data, u)
        for m in range(n_movies):
            if (data[u, m] == 0):
                inferred_ratings[u, m] = data[:,m].dot(w)
    return inferred_ratings


    
