import urllib.request, urllib.parse, urllib.error

site = input('What website do you want to connect to?\n')
try:
    hola = urllib.request.urlopen('http://' + site)
except urllib.error.URLError:
    print('can\'t open file bro.')
    exit()
count = 0

for line in hola:
    while count <= 3000:
        print( line.decode().strip())
        count += len(line)
        #print('\n', 'length of each line', len(line))
    if count > 3000:
        break


    if (len(line) <1):
        break
print('Received: ',count ,'character(/s)')