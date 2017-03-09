import data_readers, data_proc
import prob2utils as off_da_shelf
import numpy as np

def project(A, num_cols, U, V):
    if len(A) == 0:
        return

    if num_cols < 0 or num_cols > len(A[:, 0]):
        print "things might break rip you"

    A_proj = A[:, 0:num_cols]
    
    new_V = np.matmul(A_proj.transpose(), V)
    new_U = np.matmul(A_proj.transpose(), U)

    return new_U, new_V


def main():
    Y = data_readers.read_file_to_np_array('./data/data.txt')
    titles, genres = data_readers.read_movies()

    users = Y[:, 0]
    movies = Y[:, 1]
    ratings = Y[:, 2]

    M = int(max(users) - min(users) + 1)

    N = int(max(movies) - min(movies) + 1) 

    print M, N

    K = 20
    eta = 0.03
    reg = 10**-2

     
    U = np.random.uniform(low=-0.5, high=0.5, size=(K, M))
    V = np.random.uniform(low=-0.5, high=0.5, size=(K, N))

    # U, V, err = off_da_shelf.train_model(M, N, K, eta, reg, Y)
    # print U
    # print V

    A, sig, B = np.linalg.svd(V)
    # print A
    # print A.shape

    nU, nV = project(A, 2, U, V)

    print nV
    print nV.shape



if __name__ == '__main__':
    main()
