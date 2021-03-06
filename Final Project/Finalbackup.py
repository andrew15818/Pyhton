import urllib.request,urllib.error, urllib.parse
from bs4 import BeautifulSoup
import spotipy
import sys
import spotipy.util as util
import json
#The only new library is the Spotify library, called spotipy for Python

''' ===Getting the artist name and track title from the Youtube url==='''
url = input('Enter the url: ')
try:
    handle = urllib.request.urlopen(url)
except:
    print('Invalid URL, please try again')
    exit()
artist = str()
track = str()
def get_song_information(handle):
	soup = BeautifulSoup(handle, 'html.parser')
	#the title of the song is in the watch-title tag
	
	try:
		title = soup.find(class_= 'watch-title')
	except:
		print('Could not find the information from the given url :(')
	
	#we want to just get the string with artist and song name

	string = str(title.find(text = True))
	string = string.split('-')
	
	#These strings have 4 blank spaces at the beginning, so we just replace them
	try:
    	artist = string[0].replace('\n', '').replace(' ', '', 4)
    	track = string[1].replace(" ", '', 1)
	except IndexError:
    	print('could not find the information. Try somehting that is formatted a little different maybe :)')
    	exit()
	

	print('artist name :', artist)
	print('track name: ', track)



'''Now that we have the artist and track title, we can use that information to connect to the Spotify API'''

#client_id = '29ed730a97614d47855056f3f71ff371'



#Our secret id number is in the other file, this loop will make secret_id that number
#this client id is the one givent to my app when registering on Spotify

#this mehtod will automatically renew tokens if it's expired
token = util.prompt_for_user_token(username = 'andrew15818', scope='user-read-private' , client_id = '29ed730a97614d47855056f3f71ff371', client_secret = 'f1656e76e32e4d3b922f23c1ee5416a4', redirect_uri = 'http://localhost:8888/callback')
if token:
	print(token)
