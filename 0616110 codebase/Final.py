import urllib.request,urllib.error, urllib.parse, urllib
from bs4 import BeautifulSoup
import spotipy
import spotipy.util as util
import json
import requests
#The spotipy and requests libraries are 
#external, not part of Python

''' ===Getting the artist name and track title from the Youtube url==='''
print('Use me to get recommendations for artists and songs:)')
url = input('Enter the url: ')
try:
    handle = urllib.request.urlopen(url)
except:
    print('Invalid URL, please try again')
    exit()
artist = str()
track = str()
soup = BeautifulSoup(handle, 'html.parser')
#the title of the song is in the watch-title tag
        

try:
    title = soup.find(class_= 'watch-title')
except:
    print("could not open the url")
    exit()
#we want to just get the string with artist and song name
try:
   string = str(title.find(text = True))
   
   if 'Official Music Video' in string:
    cutoff = string.find('Official Music Video')
    string = string.replace(string[cutoff-1:],"")
   
   elif 'Official Video' in string:
    cutoff = string.find('Official Video')
    string = string.replace(string[cutoff-1:],"")
   
   string = string.split('-')
#These strings have 4 blank spaces at the beginning, so we just replace them
except:
    print('Could not find the information from the given url :(')
    exit()


try:
    artist = string[0].replace('\n', '').replace(' ', '', 4)
    track = string[1].replace(" ", '', 1)
except IndexError:
    print('could not find the information. Try somehting that is formatted a little different maybe :)')
    exit()
    

print('\nWe detected the artist is:', artist)
print('We detected the track is:' , track)



'''===Now that we have the artist and track title, we can use that information to connect to the Spotify API==='''
#For more effectiveness and to avoid errors, it is recommended to use the format artist-song
#If the url does not have this format, then there is a chance that there may not be a track id to use 



#this client id is the one givent to my app when registering on Spotify
#this mehtod will check for a valid token, if there is none it will request one using my account and app information
token = util.prompt_for_user_token(username = 'andrew15818', scope='user-read-private' , client_id = '29ed730a97614d47855056f3f71ff371', client_secret = 'f1656e76e32e4d3b922f23c1ee5416a4', redirect_uri = 'http://localhost:8888/callback')

if token:
    print('\nsuccessfully connected to Spotify.\n')

'''We first need to find the artists unique id url, and we do that by sending another request to spotify'''
'''This header provides our authorization information to be put in the url we will send'''
header = {'Authorization': 'Bearer '+token}
def get_artist_id(artist):
    artist_endpoint = 'https://api.spotify.com/v1/search?'
    
    #encoding the information so it is sent in the correct format during the request    
    encode_info = (("q",artist),("type","artist"))
    encode_info = urllib.parse.urlencode(encode_info)
    
    #just getting the request format in order
    request_url = artist_endpoint + encode_info
    response = requests.get(request_url, headers = header)
    #print(response.status_code)
    #print(response.json())
    
    
    try:
        #We parse the json to arrive at the id of our aritst
        response = response.json()
        artist_url = ( response['artists']['items'][0]['external_urls']['spotify'] )
        artist_url = artist_url.split('/')[4]
        return (artist_url)
    except:
        print ('Sorry, the artist/s do not have a valid spotify artist url.')
        exit()

#because we need track and artist id's to make any other requests, we first have to request them
#since the code can get a little hard to read, I decided to separate the requests for tracks and artists
def get_track_id(track):
    track_endpoint = 'https://api.spotify.com/v1/search?'
    
    encode_info = (('q',track), ('type','track'))
    encode_info = urllib.parse.urlencode(encode_info)
   
    track_url = track_endpoint+encode_info
    
    try:
        results = requests.get(track_url, headers = header)
        results = results.json()
        results = results['tracks']['items'][0]['uri']
        track_id = results.split(':')[2]
        return(track_id)
    except:
        print('Sorry, could not get track id from spotify')
        exit()
        

artist_id = get_artist_id(artist)
track_id = get_track_id(track)
#print(artist_id, track_id)
'''Now that we have the artist id, we can look for similar artists'''


def get_similar_artists(artist_id):
    #the process is similar as getting the id
    endpoint_uri = 'https://api.spotify.com/v1/artists/{id}/related-artists'
    
    final_url = endpoint_uri.format( id = artist_id)
    
    similar_artists = requests.get(final_url, headers = header)

    similar_artists = similar_artists.json()

    print('if you liked '+artist+', you might also enjoy:')
    for item in similar_artists['artists']:
        print('\t',item['name'])

    
def get_track_recommendations(track_id, artist_id):
    ''' The same process as before, however now we send both the artist and track id as seeds, and
    receive a response with many tracks, artists, and albums, but we are only interested in the tracks.'''
    endpoint = 'https://api.spotify.com/v1/recommendations?'
    seed_artists = '&seed_artists='+artist_id
    seed_tracks = 'seed_tracks='+track_id
    url = endpoint+seed_tracks+seed_artists
    results = requests.get(url, headers = header)
    results = results.json()
    print('Here are  some other songs similar to '+track+':')
    try:
        for items in results['tracks']:
            print('\t',items['name'])  
    except:
        print('Recommended tracks unavailable. Sorry:(')
    
get_similar_artists(artist_id)
get_track_recommendations(track_id, artist_id)
