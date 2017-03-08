# Common logic for data processing, after the data is read

NUM_MOVIES = 1682


def ratings_for_movies(Y):
    """
    :param Y: List of (user, movie, rating) lists.
    :return: ratings_for_movies, where ratings_for_movies[i] is the list of
        all ratings for the movie with id i.
    """
    ratings = [[] for i in range(NUM_MOVIES)]
    for user_id, movie_id, rating in Y:
        ratings[movie_id].append(rating)
    return ratings