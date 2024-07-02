import pandas as pd


class Song:
    max_score = 1010000
    records: list = []
    name: str = None
    levels: list = []

    def __init__(self, name: str, levels: list):
        self.name = name
        self.levels = levels

    def set_record(self, records: list):
        self.records = records

    def __str__(self):
        return f"{self.name}\t{self.levels}\t{self.records}"


def create_songs() -> list:
    songs_data = pd.read_excel("my_songs_information.xlsx", "levels")
    songs_data = songs_data.drop("曲绘", axis=1)
    songs_data.columns = ["name", "level1", "level2", "level3", "level4",
                          "record1", "record2", "record3", "record4"]
    number = len(songs_data.index)
    songs = []  # 曲库列表
    for i in range(number):
        song = Song(songs_data.loc[i, "name"],
                    [songs_data.loc[i, "level1"],
                     songs_data.loc[i, "level2"],
                     songs_data.loc[i, "level3"],
                     songs_data.loc[i, "level4"]])

        song.set_record([songs_data.loc[i, "record1"],
                         songs_data.loc[i, "record2"],
                         songs_data.loc[i, "record3"],
                         songs_data.loc[i, "record4"]])
        songs.append(song)

    return songs


songs: list = create_songs()
print("songs")
