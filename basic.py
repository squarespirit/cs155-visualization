# Code for basic visualizations

import data_readers
import matplotlib.pyplot as plt
from collections import Counter
import seaborn as sns


def all_ratings(Y):
    """Plot histogram of all ratings.
    :param Y: List of (user, movie, rating) lists.
    """
    # Ratings
    ratings = [rating_list[2] for rating_list in Y]

    # Possible rating values
    rating_values = list(range(1, 6))

    # count_ratings[i] is the number of ratings with value rating_values[i]
    count_ratings = [ratings.count(value) for value in rating_values]

    plt.bar(rating_values, count_ratings, align='center')
    plt.xticks(rating_values)  # I'm not sure why this works
    plt.ylabel('Count')
    plt.xlabel('Rating')
    plt.title('Histogram of all ratings')
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


def main():
    Y = data_readers.read_data()
    titles, genres = data_readers.read_movies()
    # all_ratings(Y)
    ratings_most_popular(Y, titles)


main()