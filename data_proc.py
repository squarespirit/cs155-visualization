# Common logic for data processing, after the data is read

NUM_MOVIES = 1682
# GENRE_NAMES[i] is the name of genre i
GENRE_NAMES = 'Unknown, Action, Adventure, Animation, Childrens, Comedy, Crime, Documentary, Drama, Fantasy, Film-Noir, Horror, Musical, Mystery, Romance, Sci-Fi, Thriller, War, Western'.split(', ')


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


def top_indices(lst, num_indices):
    """
    :return: Indices of the top 'num_indices' elements in list, sorted by
        largest element first.
    """
    return sorted(
        range(len(lst)), key=lambda i: lst[i], reverse=True
    )[:num_indices]