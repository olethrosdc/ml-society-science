## Generate data first

import numpy as np

## Calculate the distance between two people
## (helper function, if necessary)
def distance(x, y):
    return np.sum((x-y)**(x-y))

## Get the similarity between two people.
## I recommend that this actually retunrs a similarity vector that sums to 1, and has a zero value for the user himself
def get_similarity(data, u):
    n_users = data.shape[0]
    n_movies = data.shape[1]
    similarity = np.zeros(n_users)
    for k in range(n_users):
        if (u!=k):
            similarity[k] = np.exp(-0.01*distance(data[u], data[k]))
    return similarity / np.sum(similarity)

## data[u,m] = 0 if somebody hasn't watched a movie
def infer_ratings(data):
    n_users = data.shape[0]
    n_movies = data.shape[1]
    inferred_ratings = data.copy()
    for u in range(n_users):
        raw_similarity = get_similarity(data, u)
        for m in range(n_movies):
            ## Only calculate for movies we haven't rated
            if (data[u,m]==0):
                similarity_m = np.zeros(n_users)
                ## Ignore 0s
                for j in range(n_users):
                    if (data[j,m] > 0):
                        similarity_m = raw_similarity
                ##similarity_m(data==0) = 0 ?
                similarity_m /= np.sum(similarity_m)

                inferred_ratings[u,m] = similarity_m.dot(data[:,m])
    return inferred_ratings

    
        
def generate_random_data(n_users, n_movies, gamma):
    data = np.zeros([n_users, n_movies])
    rating_dist = [0.1, 0.2, 0.3, 0.3, 0.1]
    for u in range(n_users):
        n_ratings = 3; #np.random.geometric(gamma)
        ratings = np.random.permutation(range(n_movies))[0:n_ratings]
        for m in ratings:
            data[u,m] = 1 + np.random.choice(5,1, p=rating_dist)
    return data

data = generate_random_data(4, 5, 0.1)

inferred_data = infer_ratings(data)

print(data)
print(inferred_data)

