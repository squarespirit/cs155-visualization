# For stuff that reads data from files in data/
# Put additional data processing logic in data_proc.py--I think this is a
# good organization, let me know

import io
import csv
import numpy as np


def read_data(filename='data/data.txt'):
    """Read file of (user, movie, rating) data.
    :param filename: Filename of data file in user, movie, rating format.
    :return: Y, List of (user, movie, rating) lists.
        IMPORTANT: Users and movies are 0-indexed.
    """
    Y = []

    with io.open(filename, 'r', encoding='utf8') as f:
        for line in f:
            rating_strs = line.strip().split('\t')
            rating = list(map(int, rating_strs))

            # User and movie numbers are 1-indexed in the dataset.
            # Make them 0-indexed.
            rating[0] -= 1
            rating[1] -= 1

            Y.append(rating)

    return Y

def read_file_to_np_array(file_path):
    '''
    Does the same thing as the function above but returns it as
    a matrix. I suck. I know.
    :return: data_array: a matrix of (user, movie, rating) tuples
    '''
    # Parse csv and convert to array
    with io.open(file_path, 'r', encoding='utf8') as dest_f:
        data_iter = csv.reader(dest_f, delimiter='\t', quotechar='"')
        data = [data for data in data_iter]

    data_array = np.asarray(data, dtype=int)

    return data_array


def read_movies(filename='data/movies.txt'):
    """Read file of (movie_id, movie_title, genres...) data.
    :return movie_titles, genres.
        titles: titles[i] is the title of movie with id i.
        genres: genres[i] is the one-hot genre vector for the movie with id i.
        IMPORTANT: movie ids are 0-indexed.
    """
    titles = []
    genres = []

    with io.open(filename, 'r', encoding='ISO-8859-1') as f:
        for line in f:
            strings = line.strip().split('\t')

            # Strip " around title, if they are there
            title = strings[1]
            titles.append(title.strip('"'))

            genres.append(
                [int(genre_str) for genre_str in strings[2:]]
            )

    return titles, genres
