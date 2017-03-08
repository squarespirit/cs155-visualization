# For stuff that reads data from files in data/

import io


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


def read_movies(filename='data/movies.txt'):
    """Read file of (movie_id, movie_title, genres...) data.
    :return movie_titles, genres.
        titles: titles[i] is the title of movie with id i.
        genres: genres[i] is the one-hot genre vector for the movie with id i.
        IMPORTANT: movie ids are 0-indexed.
    """
    titles = []
    genres = []

    with io.open(filename, 'r', encoding='utf8') as f:
        for line in f:
            strings = line.strip().split('\t')
            titles.append(strings[1])
            genres.append(
                [int(genre_str) for genre_str in strings[2:]]
            )

    return titles, genres


print read_movies()