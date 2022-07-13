"""
Data Mining Assignment 2
Muhammad Waleed
20B-115-SE 
SE-B
"""
###########################################

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('anime.csv')
print(df.head())


cols = [col for col in df.columns]
print(cols)
print("-------------------------")

anime_values = df.values
print(df.shape)

anime_types = []
for i in range(len(df)):
    if anime_values[i][3] not in anime_types:
        anime_types.append(anime_values[i][3])

print(anime_types)
print("-------------------------")
for anime_type in anime_types:
    print(f'Total {anime_type}: {len(df[df.type == anime_type])}')

print("-------------------------")

anime_data = df[df.type == 'TV']
movie_data = df[df.type == 'Movie']
print(anime_data.shape)
print(movie_data.shape)
anime_data['episodes'] = anime_data['episodes'].replace('Unknown', np.nan)

print("-------------------------")

best_tv_by_rating = anime_data.sort_values(by='rating', ascending=False)
best_tv_by_members = anime_data.sort_values(by='members', ascending=False)
best_tv_by_episodes = anime_data.sort_values(by='episodes', ascending=False)

best_movies_by_rating = movie_data.sort_values(by='rating', ascending=False)
best_movies_by_members = movie_data.sort_values(by='members', ascending=False)
best_movies_by_episodes = movie_data.sort_values(by='episodes', ascending=False)



print("-------------------------")
print(best_tv_by_rating.head(10))
print("-------------------------")
print(best_tv_by_members.head(10))
print("-------------------------")
print(best_tv_by_episodes.head(10))

print("-------------------------")
print(best_movies_by_rating.head(10))
print("-------------------------")
print(best_movies_by_members.head(10))
print("-------------------------")
print(best_movies_by_episodes.head(10))

plt.figure(figsize=(15,15))
plt.barh(best_tv_by_rating['name'].head(10),best_tv_by_rating['rating'].head(10))
plt.title('Best Anime Series by Rating')
plt.xlabel('Rating')
plt.ylabel('Anime')
plt.show()

plt.figure(figsize=(15,15))
plt.barh(best_movies_by_members['name'].head(10),best_movies_by_members['rating'].head(10))
plt.title('Best Anime Movies by Rating')
plt.xlabel('Rating')
plt.ylabel('Anime')
plt.show()


