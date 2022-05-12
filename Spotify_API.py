import spotipy
import pandas as pd
import numpy as np
import sys
from pprint import pprint
import re, doctest
from spotipy.oauth2 import SpotifyClientCredentials

def read_data(file):
    '''
    Purpose: Reads in the csv file at pathname 'file' parameter. Turns the csv into a data frame and returns
    Input: 'file' - String pathname
    Return: 'df'  - Pandas dataframe
    '''
    data = pd.read_csv(file)
    return data
    
def add_popularity(df):
    '''
    Purpose: This file takes a df containing dates, concerts and performing artist(s) and adds a column
    titled 'Mean Popularity' which is the mean of each artist's popularity
    Input: 'df'  - Pandas dataframe, formatted with an 'Artists' column. Multiple artists per row separated
                   by a comma and no white space (unless intended to be part of artist name.
                   Ex: Luke Brycan,Drake
    Return: 'df' - Pandas dataframe
    '''
    artist_list = [i.split(",") for i in df['Artist']]
    popularity = []
    for j in artist_list:
        popularity.append(np.mean([calc_popularity(k) for k in j]))
    df['Mean Popularity'] = pd.DataFrame(popularity)
    return df

def calc_popularity(artist):
    '''
    Purpose: This function calculates the popularity of an artist given their name
    Input: 'artist' - String object, name of the artist whos popularity will be calculated
    Output: A float valued number 0-100 representing artist popularity
    '''
    print(artist)
    cid = # cid
    secret_cid = # secret
    spotify_session = spotipy.Spotify(client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret_cid))
    results = spotify_session.search(q=artist, limit=50)
    URI_Pattern = re.compile(r"'id': '.{100}")
    if re.search(URI_Pattern, str(results)):
        potential_URI = (URI_Pattern.findall(str(results)))
        for i in range(len(potential_URI)):
            if potential_URI[i][33:37] == 'name':
                if str(potential_URI[i][41:41+len(artist)]).capitalize() == artist.capitalize():
                    URI = potential_URI[i][7:29]
                    urn = 'spotify:artist:' + URI
                    info = spotify_session.artist(urn)
        
                    #print('Name: ',end = '')
                    #pprint(info['name'])
                    #print('Followers: ',end = '')
                    #pprint(info['followers']['total'])
                    #print('Popularity: ',end='')
                    #pprint(info['popularity'])
                    return info['popularity']
            if i == len(potential_URI)-1:
                return 0.4
                
    else:
        return 0.4

def main():
    # Two major functionalities:
    # 1. Read through a file and assign popularities to lists of artists
    # 2. Calculate and return a specific artist popularity
    
    #Functionality: List iteration
    #file = # PATHNAME
    #df = read_data(file)
    #df = add_popularity(df)
    
    #Functionality: Specific popularity calculation, given user inputed name
    print("Welcome to the Spotify API artist info generator")
    artist = input("Please input the name of the artist you wish to search here. (Case sensative)")
    print("The popularity of ",artist," is: ",calc_popularity(artist))

    
if __name__ == '__main__':
    main()


   
