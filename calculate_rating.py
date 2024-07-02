import pandas

import songs
import pandas as pd
import dataframe_image as dfi
import numpy as np


class Rating:
    name: str = None
    level: int = 0
    level_num: float = 0.0
    score: int = 0
    rating: float = 0

    def __init__(self, song: songs.Song, level: int):
        self.name = song.name
        self.level = level
        self.level_num = song.levels[level - 1]
        self.score = song.records[level - 1]

    def __str__(self):
        # return "%.1f" % self.rating
        return "%s\t%d\t%f\t%f" % (self.name, self.level, self.level_num, self.rating)

    def __lt__(self, other):
        return self.rating < other.rating

    def __gt__(self, other):
        return self.rating > other.rating

    def __eq__(self, other):
        return self.rating == other.rating

    def calculate_rating(self):
        boundary = [songs.Song.max_score, 1008000, 1004000, 1000000, 980000, 950000, 900000, 500000]
        if self.score >= boundary[0]:  # 1010000
            self.rating = self.level_num + 3.6

        elif self.score >= boundary[1]:
            self.rating = self.level_num + 3.4 + (self.score - boundary[1]) / 10000

        elif self.score >= boundary[2]:
            self.rating = self.level_num + 2.4 + (self.score - boundary[2]) / 4000

        elif self.score >= boundary[3]:
            self.rating = self.level_num + 2.0 + (self.score - boundary[3]) / 10000

        elif self.score >= boundary[4]:
            self.rating = self.level_num + 1.0 + (self.score - boundary[4]) / 20000

        elif self.score >= boundary[5]:
            self.rating = self.level_num + 0.0 + (self.score - boundary[5]) / 30000

        elif self.score >= boundary[6]:
            self.rating = self.level_num - 1.0 + (self.score - boundary[6]) / 50000

        elif self.score >= boundary[7]:
            self.rating = self.level_num - 5.0 + (self.score - boundary[7]) / 100000

        else:
            self.rating = 0


def generate_sorted_ratings() -> list:
    ratings = []
    for song in songs.songs:
        for i in [1, 2, 3, 4]:
            rating = Rating(song, i)
            rating.calculate_rating()
            ratings.append(rating)
    sorted_ratings = sorted(ratings, reverse=True)
    return sorted_ratings


def generate_best_frame(ratings) -> pandas.DataFrame:
    # number = 40
    names = []
    levels = []
    level_nums = []
    scores = []
    my_ratings = []
    for i in range(number):
        names.append(ratings[i].name)
        levels.append(ratings[i].level)
        level_nums.append(ratings[i].level_num)
        scores.append(ratings[i].score)
        my_ratings.append(ratings[i].rating)
    best_frame = pd.DataFrame({'歌名': names,
                               '难度': levels,
                               '定数': level_nums,
                               '分数': scores,
                               'Rating': my_ratings})
    best_frame.index = range(1, number + 1)
    return best_frame


def generate_frame_image(best_frame: pandas.DataFrame):
    dfi.export(best_frame, f'b{number}.png')


def generate_b30_value(sorted_ratings: list) -> float:
    rtn_number = []
    for rating_obj in sorted_ratings[0:29]:
        rtn_number.append(rating_obj.rating)
    return 0.7 * np.mean(rtn_number[0:9]) + 0.3 * np.mean(rtn_number[10:29])


def calculate_main():
    try:
        if number > 50:
            print("Please type in the right number.")
        else:
            ratings = generate_sorted_ratings()
            best_frame = generate_best_frame(ratings)
            generate_frame_image(best_frame)
            b30_value = generate_b30_value(ratings)
            print("The value of your best 30 is %.5f." % b30_value)
    except (NameError, TypeError):
        print("Please type in the right number.")


if __name__ == "__main__":
    calculate_main()

print("calculate")
try:
    number = int(input("Type in an integer no more than 50: "))
except ValueError:
    print("Please type in the right number.")
