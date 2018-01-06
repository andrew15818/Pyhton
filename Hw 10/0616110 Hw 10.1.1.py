import socket
site = input('What site do you want to connect to?\n')
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((site, 80))
except:
    print('cannot connect to website bro.')
    exit()

#cmd = 'GET / HTTP/1.1\nHost: '+site+'\n\n'
cmd = 'GET https://'+site+'HTTP/1.0\n\n'
sock.send(cmd.encode())
#print(len())
count = 0
while count <= 3000:
    if count > 3000:
        break
    hola = sock.recv(4096)
    count += len(hola)
    if len(hola) < 1:
        break
    print(hola.decode(), end=' ')
print('\nreceived: ', count ,'character(/s)')
sock.close()