# Code for basic visualizations

import data_readers
import matplotlib.pyplot as plt


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


def main():
    Y = data_readers.read_data()
    titles, genres = data_readers.read_movies()
    all_ratings(Y)


main()