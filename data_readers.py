# For stuff that reads data from files in data/


def read_data(filename='data/data.txt'):
    """Read file of (user, movie, rating) data.
    :param filename: Filename of data file in user, movie, rating format.
    :return: Y, List of (user, movie, rating) lists.
        IMPORTANT: Users and movies are 0-indexed.
    """
    Y = []

    with open(filename, 'r') as f:
        for line in f:
            rating_strs = line.strip().split('\t')
            rating = list(map(int, rating_strs))

            # User and movie numbers are 1-indexed in the dataset.
            # Make them 0-indexed.
            rating[0] -= 1
            rating[1] -= 1

            Y.append(rating)

    return Y
