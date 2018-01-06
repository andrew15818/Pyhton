import urllib.request,urllib.error, urllib.parse
from bs4 import BeautifulSoup
import spotipy
import sys
import spotipy.util as util
#The only new library is the Spotify library, called spotipy for Python

''' This section gets the title of the track and artist from the website'''
'''url = input('Enter the url: ')
try:
    handle = urllib.request.urlopen(url)
except:
    print('Invalid URL, please try again')
    exit()


soup = BeautifulSoup(handle, 'html.parser')
#print(soup.prettify())
#the title of the song is in the watch-title tag
title = soup.find(class_= 'watch-title')
#print(title)
#we want to just get the string with artist and song name

string = str(title.find(text = True))

string = string.split('-')
#print(string)
try:
    artist = string[0].replace('\n', '').replace(' ', '', 4)
    track = string[1].replace(" ", '', 1)
except IndexError:
    print('could not find the information. Try somehting that is formatted a little different maybe :)')
    exit()

print(artist)
print(track)
# print(string)

#These strings have 4 blank spaces at the beginning, so we just replace them

print('artist name :', artist)
print('track name: ', track)'''


'''Now that we have the artist and track title, we can use that information to connect to the Spotify API'''

client_id = '29ed730a97614d47855056f3f71ff371'
#we need this key for authorization, plus another private key which I saved in the secret.txt file



#that's my name :)


#Our secret id number is in the other file, this loop will make secret_id that number
#this client id is the one givent to my app when registering on Spotify

token = util.prompt_for_user_token(username = 'andrew15818',  client_id = '29ed730a97614d47855056f3f71ff371', client_secret = 'f1656e76e32e4d3b922f23c1ee5416a4', redirect_uri = 'http://localhost/')
if token:
    print ('hola')