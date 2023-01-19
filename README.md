# SongMatch

# Introduction

SongMatch is a program that returns some suggested songs from a user-inputted song based on a variety of attributes provided by Spotify's API.
The attributes used for the algorithm are tempo, time signature, valence, key, mode, loudness, instrumentalness, and acousticness.

# Methods
The program uses multidimensional k-means clustering to determine song recommendations. To standardize the numerical measures of each attribute, min-max normalization was used (as certain attributes had different ranges).

# Requirements
- Download file 'tracks1.csv'
- Note that user input for song name is case-sensitive.

# Notes:
The dataset was adjusted and refined from Yamac Eren Ay's dataset available on Kaggle. This dataset contains approximately 600,000 songs on Spotify, with release dates ranging from 1922 to April 2021.
