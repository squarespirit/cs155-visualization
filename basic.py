# Code for basic visualizations

import data_readers, data_proc
import matplotlib.pyplot as plt
from collections import Counter
import seaborn as sns


def bar_count_ratings(Y, plot_title):
    """Plot bar chart of counts of each rating.
    You have to call plt.show() afterward.
    :param Y: List of (user, movie, rating) triples.
    :param plot_title
    """
    # Ratings
    ratings = [rating_list[2] for rating_list in Y]

    # Possible rating values
    rating_values = list(range(1, 6))

    # count_ratings[i] is the number of ratings with value rating_values[i]
    count_ratings = [ratings.count(value) for value in rating_values]

    plt.bar(rating_values, count_ratings, align='center',
            tick_label=rating_values)
    plt.ylabel('Count')
    plt.xlabel('Rating')
    plt.title(plot_title)


def all_ratings(Y):
    """Plot histogram of all ratings.
    :param Y: List of (user, movie, rating) lists.
    """
    bar_count_ratings(Y, 'Rating distribution for all movies')
    plt.show()


def ratings_most_popular(Y, titles):
    """Plot ratings of 10 most popular movies."""
    # Movies
    movie_ids = [rating_list[1] for rating_list in Y]

    # 10 most popular movie ids
    result = Counter(movie_ids).most_common(10)
    popular_ids = [elt_and_count[0] for elt_and_count in result]
    popular_titles = [titles[id] for id in popular_ids]

    # Possible rating values
    rating_values = list(range(1, 6))

    # popular_ratings[i][j] is the number of rating_values[j] ratings for
    # movie with id i
    popular_ratings = \
        [[sum([rating_list[1] == id and rating_list[2] == rating_val
               for rating_list in Y])
          for rating_val in rating_values]
         for id in popular_ids]

    sns.heatmap(popular_ratings,
                annot=True, fmt='d',  # Annotate data values
                yticklabels=popular_titles, xticklabels=rating_values)
    plt.yticks(rotation=0)  # Rotate yticks horizontally
    plt.xlabel('Rating')
    plt.title('Ratings of most popular movies')
    plt.tight_layout()  # Make room for long ytick labels
    plt.show()


def ratings_best(Y, titles):
    """Plot ratings of 10 best (highest-rated) movies."""
    ratings_lists = data_proc.ratings_for_movies(Y)

    # Possible rating values
    rating_values = list(range(1, 6))

    # avg_ratings[i] = average rating of movie i
    # avg_ratings = [float(sum(ratings_list)) / len(ratings_list)
    #                for ratings_list in ratings_lists]
    # Disfavor highly rated movies with few ratings:
    # http://stats.stackexchange.com/a/6361
    avg_ratings = [float(sum(ratings_list) + sum(rating_values))
                   / (len(ratings_list) + len(rating_values))
                   for ratings_list in ratings_lists]
    best_ids = data_proc.top_indices(avg_ratings, 10)
    best_titles = [titles[id] for id in best_ids]

    # ratings_table[i][j] is the number of rating_values[j] ratings for
    # movie with id i
    ratings_table = \
        [[sum([rating_list[1] == id and rating_list[2] == rating_val
               for rating_list in Y])
          for rating_val in rating_values]
         for id in best_ids]

    sns.heatmap(ratings_table,
                annot=True, fmt='d',  # Annotate data values
                yticklabels=best_titles, xticklabels=rating_values)
    plt.yticks(rotation=0)  # Rotate yticks horizontally
    plt.xlabel('Rating')
    plt.title('Ratings of highest rated movies')
    plt.tight_layout()  # Make room for long ytick labels
    plt.show()


def ratings_genre(Y, genres, genre_id):
    """Plot rating distribution for all movies of the given genre."""
    # Filter Y for only ratings of movies in the genre.
    genre_Y = filter(
        lambda user_movie_rating: genres[user_movie_rating[1]][genre_id], Y
    )
    bar_count_ratings(genre_Y, 'Rating distribution for {} movies'.format(
        data_proc.GENRE_NAMES[genre_id]
    ))


def ratings_genres(Y, genres):
    """Plot rating distribution for 3 genres."""
    plt.subplot(311)
    ratings_genre(Y, genres, 1)
    plt.subplot(312)
    ratings_genre(Y, genres, 2)
    plt.subplot(313)
    ratings_genre(Y, genres, 3)
    plt.tight_layout()
    plt.show()


def main():
    Y = data_readers.read_data()
    titles, genres = data_readers.read_movies()
    # all_ratings(Y)
    # ratings_most_popular(Y, titles)
    # ratings_best(Y, titles)
    ratings_genres(Y, genres)


main()