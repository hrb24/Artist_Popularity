import spotipy
import sys
from pprint import pprint
import re, doctest
from spotipy.oauth2 import SpotifyClientCredentials



def main():
    print("Welcome to the Spotify API artist info generator")
    print("Please input the name of the artist you wish to search here. (Case sensative)")
    artist = 'Luke Bryan'
    cid = #
    secret_cid = #
    spotify_session = spotipy.Spotify(client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret_cid))
    
    results = spotify_session.search(q=artist, limit=50)
    
    URI_Pattern = re.compile(r"['id': '].{33}'" + re.escape(artist) + r"'")
    if re.search(URI_Pattern, str(results)):
        URI = (URI_Pattern.findall(str(results)))[0][1:23]
    else:
        print("Did not find URI")
    
    urn = 'spotify:artist:' + URI
    info = spotify_session.artist(urn)
    print('Name: ',end = '')
    pprint(info['name'])
    print('Followers: ',end = '')
    pprint(info['followers']['total'])
    print('Popularity: ',end='')
    pprint(info['popularity'])
   
   
   
   
if __name__ == '__main__':
    main()


   
