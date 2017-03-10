import data_readers, data_proc
import prob2utils as off_da_shelf
import numpy as np
import matplotlib.pyplot as plt

from collections import Counter
from numpy.linalg import norm

def project(A, num_cols, U, V):
    if len(A) == 0:
        return

    if num_cols < 0 or num_cols > len(A[:, 0]):
        print "things might break rip you"

    A_proj = A[:, 0:num_cols]
    
    new_V = np.matmul(A_proj.transpose(), V)
    # new_U = np.matmul(A_proj.transpose())

    return new_V


def main():
    Y = data_readers.read_file_to_np_array('./data/data.txt')
    titles, genres = data_readers.read_movies()

    users = Y[:, 0]
    movies = Y[:, 1]
    ratings = Y[:, 2]

    M = int(max(users) - min(users) + 1)

    N = int(max(movies) - min(movies) + 1) 

    #print M, N

    K = 20
    eta = 0.03
    reg = 10**-2

     
    U = np.random.uniform(low=-0.5, high=0.5, size=(K, M))
    V = np.random.uniform(low=-0.5, high=0.5, size=(K, N))

    #U, V, err = off_da_shelf.train_model(M, N, K, eta, reg, Y)
    # print U
    # print V


    # nrm = norm(V, axis=1, ord=1)
    for i in range(len(V)):
        V[i] = V[i] - (sum(V[i]) / len(V[i]))
    

    # print V

    A, sig, B = np.linalg.svd(V)
    # print A
    # print A.shape

    nV = project(A, 2, U, V)

    # print nU
    # print nU.shape
    #print nV
    #print nV.shape

    # 10 random movie ids
    rng_idxs = np.random.choice(nV.shape[1], size=10, replace=False)
    visualize(nV, titles, rng_idxs)

    # 10 most popular movie ids
    popular_idxs = [e[0] for e in Counter([r[1]-1 for r in Y]).most_common(10)]
    visualize(nV, titles, popular_idxs)

    # 10 best rated movie ids
    Y[:, 1] -= 1
    ratings_lists = data_proc.ratings_for_movies(Y)
    avg_ratings = [float(sum(ratings_list) + sum(list(range(1, 6))))
                   / (len(ratings_list) + len(list(range(1, 6))))
                   for ratings_list in ratings_lists]
    best_idxs = data_proc.top_indices(avg_ratings, 10)
    visualize(nV, titles, best_idxs)

    # 10 genre 1 movie ids
    genre_idxs = [movies[i] for i in range(len(titles)) if np.asarray(genres)[i, 1] == 1]
    genre_idxs = np.random.choice(genre_idxs, size=10, replace=False)
    visualize(nV, titles, genre_idxs)

    # 10 genre 2 movie ids
    genre_idxs = [movies[i] for i in range(len(titles)) if np.asarray(genres)[i, 2] == 1]
    genre_idxs = np.random.choice(genre_idxs, size=10, replace=False)
    visualize(nV, titles, genre_idxs)
    
    # 10 genre 3 movie ids
    genre_idxs = [movies[i] for i in range(len(titles)) if np.asarray(genres)[i, 3] == 1]
    genre_idxs = np.random.choice(genre_idxs, size=10, replace=False)
    visualize(nV, titles, genre_idxs)

    plt.show()

def visualize(nV, titles, idxs):
    fig = plt.figure()
    sub = fig.add_subplot('111')

    for i in idxs:
        plt.plot(nV[0, i], nV[1, i], "o")
        sub.annotate('%s' % titles[i], xy=(nV[0,i], nV[1,i]), xytext=(40, 20),
        textcoords='offset points', ha='right', va='bottom',
        bbox=dict(boxstyle='round,pad=0.5', fc='purple', alpha=0.5))
    
    sub.spines['left'].set_position('zero')
    sub.spines['right'].set_color('none')
    sub.spines['bottom'].set_position('zero')
    sub.spines['top'].set_color('none')
    
    #plt.show()



if __name__ == '__main__':
    main()
