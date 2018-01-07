import urllib.request,urllib.error, urllib.parse, urllib
from bs4 import BeautifulSoup
import spotipy
import sys, pprint
import spotipy.util as util
import json
import requests
#The spotipy and requests libraries are 
#external, not part of Python

''' ===Getting the artist name and track title from the Youtube url==='''
url = input('Enter the url: ')
try:
    handle = urllib.request.urlopen(url)
except:
    print('Invalid URL, please try again')
    exit()
artist = dict()
track = str()
soup = BeautifulSoup(handle, 'html.parser')
#the title of the song is in the watch-title tag
        

try:
    title = soup.find(class_= 'watch-title')
except:
    p
#we want to just get the string with artist and song name
try:
   string = str(title.find(text = True))
   string = string.split('-')
#These strings have 4 blank spaces at the beginning, so we just replace them
except:
    print('Could not find the information from the given url :(')


try:
    artist = string[0].replace('\n', '').replace(' ', '', 4)
    track = string[1].replace(" ", '', 1)
except IndexError:
    print('could not find the information. Try somehting that is formatted a little different maybe :)')
    exit()
    

print('We detected the artist is:', artist)
print('We detected the track is:' , track)



'''===Now that we have the artist and track title, we can use that information to connect to the Spotify API==='''

#client_id = '29ed730a97614d47855056f3f71ff371'



#Our secret id number is in the other file, this loop will make secret_id that number
#this client id is the one givent to my app when registering on Spotify

#this mehtod will automatically renew tokens if it's expired
token = util.prompt_for_user_token(username = 'andrew15818', scope='user-read-private' , client_id = '29ed730a97614d47855056f3f71ff371', client_secret = 'f1656e76e32e4d3b922f23c1ee5416a4', redirect_uri = 'http://localhost:8888/callback')

if token:
    print('successfully connected to Spotify.')

'''We first need to find the artists unique id url, and we do that by sending another request to spotify'''

def get_artist_id(artist):
    artist_endpoint = 'https://api.spotify.com/v1/search?'
    
    #encoding the information so it is sent in the correct format during the request    
    encode_info = (("q",artist),("type","artist"))
    encode_info = urllib.parse.urlencode(encode_info)
    
    #just getting the request format in order
    request_url = artist_endpoint + encode_info
    header = {'Authorization': 'Bearer '+token}
    response = requests.get(request_url, headers = header)
    
    try:
        '''We parse the json to arrive at the id of our aritst'''
        response = response.json()
        artist_url = ( response['artists']['items'][0]['external_urls']['spotify'] )
        artist_url = artist_url.split('/')[4]
        return (artist_url)
    except json.JSONDecodeError:
        print ('Sorry, there was a mistake in retrieving data from Spotify')
        
artist_id = get_artist_id(artist)
print(artist_id)
'''Now that we have the artist id, we can look for similar artists'''
def get_similar_artists(artist_id):
    #the process is similar as getting the id
    endpoint_uri = 'https://api.spotify.com/v1/artists/{id}/related-artists'
    header = {'Authorization': 'Bearer '+token}
    
    final_url = endpoint_uri.format( id = artist_id)
    
    similar_artists = requests.get(final_url, headers = header)
    #pprint.pprint(similar_artists.json())
    
    similar_artists = similar_artists.json()
    
    print(similar_artists['artists'][0]['name'])
    
    
get_similar_artists(artist_id)
