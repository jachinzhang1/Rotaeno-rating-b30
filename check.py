import pandas as pd
from songs import Song

new_songs = pd.read_excel("songs_information.xlsx", "levels")
new_songs = new_songs.drop("曲绘", axis=1)
saved_songs = pd.read_excel("songs_information.xlsx", "save")
saved_songs = saved_songs.drop("曲绘", axis=1)
# 注意文件名被修改，要先实验一下 ===================================================

num_new = len(new_songs.index)
num_save = len(saved_songs.index)

if num_new != num_save:
    new_names = list(new_songs['曲目'])
    saved_names = list(saved_songs['曲目'])
    for new_name in new_names:
        if new_name not in saved_names:
            i = new_names.index(new_name)
            the_new = Song(new_songs.loc[i, "曲目"],
                           [new_songs.loc[i, "难度I"],
                            new_songs.loc[i, "难度II"],
                            new_songs.loc[i, "难度III"],
                            new_songs.loc[i, "难度IV"]])
            # saved_songs = saved_songs.append()
            print(f"Update: {new_name}")
    saved_songs.to_excel("songs_information.xlsx", "save")
    print("The saved table has been updated.")

else:
    print("No updated information.")
print("check")

# [the_new.name,
#                                               the_new.levels[0],
#                                               the_new.levels[1],
#                                               the_new.levels[2],
#                                               the_new.levels[3],
#                                               0.0,  # 难度1的分数记录
#                                               0.0,  # 难度2的分数记录
#                                               0.0,  # 难度3的分数记录
#                                               0.0]